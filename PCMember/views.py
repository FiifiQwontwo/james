from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from PCMember.models import *
from Attendance.models import *
from django.views.decorators.csrf import ensure_csrf_cookie
from PCMember.forms import CreateMemberForm
import datetime as dt
import pandas as pd
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.
# def member_list(request):
#     memlist = PcMember.objects.all().get()
#     context = {
#         'memlist': memlist
#     }
#     return render(request, 'listmember.html', contex


def member_list(request):
    memelist = PcMember.objects.all()
    context = {
        'memelist': memelist
    }
    return render(request, 'listmember.html', context)


def member_detail(request, slug):
    mem_det = get_object_or_404(PcMember, slug=slug)
    # mem_group = PCS.objects.filter(pcattendance__pc_member__slug=slug)

    context = {
        'mem_det': mem_det,
        # 'mem_group': mem_group,
    }
    return render(request, 'detailsmember.html', context)


@ensure_csrf_cookie
def create_pcmember(request):
    if not request.user.is_superuser or not request.user.is_staff:
        raise Http404
    mem_create = CreateMemberForm(request.POST or None, request.FILES)
    if mem_create.is_valid():
        instance = mem_create.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('Attendance:home page')
    context = {
        'mem_create': mem_create
    }
    return render(request, 'memcreate.html', context)


def Import_csv(request):
    print('s')
    try:
        if request.method == 'POST' and request.FILES['myfile']:

            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print(excel_file)
            empexceldata = pd.read_csv("." + excel_file, encoding='utf-8')
            print(type(empexceldata))
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():
                fromdate_time_obj = dt.datetime.strptime(dbframe.DOB, '%d-%m-%Y')
                obj = PcMember.objects.create(pcs_name=dbframe.pcs_name,
                                              pc_member_last_name=dbframe.pc_member_last_name,
                                              pc_member_first_name=dbframe.pc_member_first_name,
                                              pc_member_othername=dbframe.pc_member_othername,
                                              whats_phone=dbframe.whats_phone, pc_member_phone=dbframe.pc_member_phone,
                                              pc_member_gps_address=dbframe.pc_member_gps_address,
                                              pc_member_house_address=dbframe.pc_member_house_address)
                print(type(obj))
                obj.save()

            return render(request, 'importexcel.html', {
                'uploaded_file_url': uploaded_file_url
            })
    except Exception as identifier:
        print(identifier)

    return render(request, 'importexcel.html', {})

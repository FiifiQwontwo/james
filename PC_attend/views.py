from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

import PCMember
from PC_attend.models import PcAttendance
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from PC_attend.forms import CreateAttendanceForm
from django.views.generic import CreateView


# from PC_attend.forms import CreateMemberForm

@login_required(login_url='accounts:user_login')
def attendance_list(request):
    attlist = PcAttendance.objects.all().order_by('-created_at').reverse()
    context = {
        'attlist': attlist
    }
    return render(request, 'listattendance.html', context)


@login_required(login_url='accounts:user_login')
def detail_view_attendance(request, id):
    context = {}

    context["data"] = PcAttendance.objects.get(id=id)

    return render(request, "detailsattendance.html", context)


# def attendance_detail(request, slug):
#     mem_att = get_object_or_404(PcAttendance, slug=slug)
#     context = {
#         'mem_att': mem_att
#     }
#     return render(request, 'detailsattendance.html', context)


@csrf_exempt
def attendance_add(request):
    new_atts = CreateAttendanceForm(request.POST or None)
    errors = None
    if new_atts.is_valid():
        if request.user.is_authenticated:
            instance = new_atts.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('PC_attend:attendance_list')
    if new_atts.errors:
        errors = new_atts.errors
    context = {
        'new_atts': new_atts
    }
    return render(request, 'newattend.html', context)


def load_members(request):
    pc_name_id = request.GET.get('pcs_name')
    member = PCMember.objects.filter(pc_name_id=pc_name_id).order_by('pc_member_last_name')
    return render(request, 'loadmembers.html', {'member': member})

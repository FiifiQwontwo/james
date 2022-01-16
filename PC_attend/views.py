from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from PC_attend.models import PcAttendance
from django.views.decorators.csrf import ensure_csrf_cookie
from PC_attend.forms import CreateAttendanceForm


# from PC_attend.forms import CreateMemberForm


def attendance_list(request):
    attlist = PcAttendance.objects.all()
    context = {
        'attlist': attlist
    }
    return render(request, 'listattendance.html', context)


# def attendance_detail(request, slug):
#     mem_att = get_object_or_404(PcAttendance, slug=slug)
#     context = {
#         'mem_att': mem_att
#     }
#     return render(request, 'detailsattendance.html', context)


@ensure_csrf_cookie
def create_attendance(request):
    if not request.user.is_superuser or not request.user.is_staff:
        raise Http404
    att_create = CreateAttendanceForm(request.POST or None, request.FILES)
    if att_create.is_valid():
        instance = att_create.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('Attendance:home page')
    context = {
        'att_create': att_create
    }
    return render(request, 'newattend.html', context)

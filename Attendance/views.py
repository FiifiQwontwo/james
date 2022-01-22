from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from Attendance.models import PCS
from PCMember.models import PcMember
from accounts.models import User
from PC_attend.models import PcAttendance
from django.views.decorators.csrf import ensure_csrf_cookie
from Attendance.forms import CreatePCSForm


# Create your views here.

def index(request):
    pcs_count = PCS.objects.all().count()
    member_count = PcMember.objects.all().count()
    accounts_count = User.objects.all().exclude(is_superuser=True).count()
    attendance_count = PcAttendance.objects.filter(present=True).count()
    pcs_list = PCS.objects.order_by('-created_at')[:5]
    mem = PcMember.objects.order_by('-created_at')[:5]
    context = {
        'pcs_count': pcs_count,
        'member_count': member_count,
        'pcs_list': pcs_list,
        'accounts_count': accounts_count,
        'attendance_count': attendance_count,
        'mem': mem,

    }
    return render(request, 'basic_pages/index.html', context)


@login_required(login_url='accounts:user_login')
def list_pcs(request):
    pcslt = PCS.objects.all()
    context = {
        'pcslt': pcslt
    }
    return render(request, 'listpcs.html', context)


@login_required(login_url='accounts:user_login')
def pcs_detail(request, slug):
    pcs_det = get_object_or_404(PCS, slug=slug)
    pcs_member_count = PcMember.objects.filter(pcs_name__slug=slug).count()
    pcs_member = PcMember.objects.filter(pcs_name__slug=slug)
    context = {
        'pcs_det': pcs_det,
        'pcs_member': pcs_member,
        'pcs_member_count': pcs_member_count,
    }
    return render(request, 'pcsdetail.html', context)


@ensure_csrf_cookie
@login_required(login_url='accounts:user_login')
def create_pcs_name(request):
    if not request.user.is_superuser or not request.user.is_staff:
        raise Http404
    pcs_create = CreatePCSForm(request.POST or None, request.FILES)
    if pcs_create.is_valid():
        instance = pcs_create.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('Attendance:home page')
    context = {
        'pcs_create': pcs_create
    }
    return render(request, 'pcs_new.html', context)


@login_required(login_url='accounts:user_login')
def create_name_pcs(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    p_create = CreatePCSForm(request.POST or None, request.FILES)
    if p_create.is_valid():
        instance = p_create.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('Attendance:home page')
    context = {
        'p_create': p_create
    }
    return render(request, 'new_pcs.html', context)

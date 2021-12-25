from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from Attendance.models import PCS
from PCMember.models import PcMember
from django.views.decorators.csrf import ensure_csrf_cookie
from Attendance.forms import CreatePCSFOrm


# Create your views here.

def index(request):
    pcs_count = PCS.objects.all().count()
    member_count = PcMember.objects.all().count()
    pcs_list = PCS.objects.all()
    context = {
        'pcs_count': pcs_count,
        'member_count': member_count,
        'pcs_list': pcs_list,

    }
    return render(request, 'basic_pages/index.html', context)


def list_pcs(request):
    pcslt = PCS.objects.all()
    context = {
        'pcslt': pcslt
    }
    return render(request, 'listpcs.html', context)


def pcs_detail(request, slug):
    pcs_det = get_object_or_404(PCS, slug=slug)
    context = {
        'pcs_det': pcs_det
    }
    return render(request, 'pcsdetail.html', context)


@ensure_csrf_cookie
def create_pcs_name(request):
    if not request.user.is_superuser or not request.user.is_staff:
        raise Http404
    pcs_create = CreatePCSFOrm(request.POST or None, request.FILES)
    if pcs_create.is_valid():
        instance = pcs_create.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('Attendance:home page')
    context = {
        'pcs_create': pcs_create
    }
    return render(request, 'pcs_new.html', context)



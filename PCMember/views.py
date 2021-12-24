from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from PCMember.models import PcMember
from django.views.decorators.csrf import ensure_csrf_cookie
from Attendance.forms import CreatePCSFOrm


# Create your views here.
def member_list(request):
    memlist = PcMember.objects.all().get()
    context = {
        'memlist': memlist
    }
    return render(request, 'listmember.html', context)


def member_detail(request, slug):
    mem_det = get_object_or_404(PcMember, slug=slug)
    context = {
        'mem_det': mem_det
    }
    return render(request, 'detailsmember.html', context)


@ensure_csrf_cookie
def create_pcs_heads(request):
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

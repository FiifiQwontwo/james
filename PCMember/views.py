from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from PCMember.models import PcMember
from django.views.decorators.csrf import ensure_csrf_cookie
from PCMember.forms import CreateMemberForm


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

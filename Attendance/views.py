from django.http import Http404
from django.shortcuts import render, get_object_or_404
from Attendance.models import PCS
from PCMember.models import PcMember
from django.views.decorators.csrf import ensure_csrf_cookie


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


def pcs_detail(request, slug):
    pcs_det = get_object_or_404(PCS, slug=slug)
    context = {
        'pcs_det': pcs_det
    }
    return render(request, 'pcsdetail.html', context)


@ensure_csrf_cookie
def create_pcs_heads(request):
    if not request.user.is_superuser or not request.user.is_staff:
        raise Http404
    pcs_create =

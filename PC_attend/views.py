from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from PC_attend.models import PcAttendance
from django.views.decorators.csrf import ensure_csrf_cookie
from PC_attend.forms import CreateAttendanceForm
from django.views.generic import CreateView


# from PC_attend.forms import CreateMemberForm


def attendance_list(request):
    attlist = PcAttendance.objects.all().order_by('-created_at')
    context = {
        'attlist': attlist
    }
    return render(request, 'listattendance.html', context)


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

#
# class CreateAttendanceView(CreateView):
#     model = PcAttendance
#     form_class = CreateAttendanceForm
#     template_name = 'newattend.html'
#     success_url = reverse_lazy('home page')

# def get_form_kwargs(self):
#     kwargs = super(CreateAttendanceView, self).get_form_kwargs()
#     kwargs['request'] = self.request
#     # CreateAttendanceView().get_form()
#     return kwargs

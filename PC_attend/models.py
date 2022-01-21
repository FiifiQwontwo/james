from datetime import date
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
import random
import string
from django.utils.text import slugify
from Attendance.models import PCS
# from PCShead.models import Pchead
from PCMember.models import PcMember


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))


def no_future(value):
    today = date.today()
    if value > today:
        raise ValidationError('attendance date cannot be in the future.')


PRESENT = {
    ('Out of Town', 'Out of Town'),
    ('Sick', 'Sick'),
    ('Not_available', 'Not available'),
}


# Create your models here.
class PcAttendance(models.Model):
    pcs_name = models.ForeignKey(PCS, on_delete=models.DO_NOTHING)
    # pcs_head = models.ForeignKey(Pchead, on_delete=models.DO_NOTHING)
    pc_member = models.ManyToManyField(PcMember)
    service_date = models.DateField(help_text="Enter the date of Service", validators=[no_future])
    present = models.BooleanField(default=False)
    reason = models.CharField(choices=PRESENT, max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.service_date)

    def get_members(self):
        return "\n".join([m.pc_member_last_name for m in self.pc_member.all()])

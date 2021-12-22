from django.conf import settings
from django.db import models
import random
import string
from django.utils.text import slugify
from Attendance.models import PCS


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))


# Create your models here.
class Pchead(models.Model):
    pcs_name = models.ForeignKey(PCS, on_delete=models.DO_NOTHING)
    pc_head_last_name = models.CharField(max_length=100)
    pc_head_first_name = models.CharField(max_length=100, blank=True)
    pc_head_phone = models.CharField(max_length=15)
    pc_head_email = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, help_text='Enter any text', default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.pc_head_last_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.pc_head_last_name + "-" + rand_slug())
        super(Pchead, self).save(*args, **kwargs)

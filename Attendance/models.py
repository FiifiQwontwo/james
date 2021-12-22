from django.conf import settings
from django.db import models
import random
import string
from django.utils.text import slugify


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))


# Create your models here.
class PCS(models.Model):
    pcs_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, help_text='Enter any text', default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.pcs_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.pcs_name + "-" + rand_slug())
        super(PCS, self).save(*args, **kwargs)

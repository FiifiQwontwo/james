from django.conf import settings
from django.db import models
import random
import string
from django.utils.text import slugify
from Attendance.models import PCS


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))


Gender = {
    ('Male', 'Male'),
    ('Female', 'Female'),
}

MARITAL = {
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
    ('widow', 'widow'),

}

NAME_CHAPEL = {
    ('Proverbs', 'Proverbs'),
    ('Amos', 'Amos'),
    ('Jeremiah', 'Jeremiah'),
    ('Joshua', 'Joshua'),
    ('Mark', 'Mark'),
    ('Luke', 'Luke'),
    ('John', 'John'),
    ('Matthew', 'Matthew'),
    ('Ruth', 'Ruth'),
    ('Neremiah', 'Neremiah'),
    ('Genesis', 'Genesis'),
    ('Numbers', 'Numbers'),
    ('Daniel', 'Daniel'),
    ('Esther', 'Esther'),
    ('Ezekial', 'Ezekial'),
    ('Ephessians', 'Ephessians'),
    ('Ezra', 'Ezra'),
    ('Isaiah', 'Isaiah'),
    ('Joel', 'Joel'),
    ('Malachi', 'Malachi'),
    ('Psalms', 'Psalms'),
    ('Samuel', 'Samuel'),
    ('Acts/ Kings', 'Acts/Kings'),
    ('Revelation', 'Revelation'),

}


# Create your models here.
class PcMember(models.Model):
    pcs_name = models.ForeignKey(PCS, on_delete=models.DO_NOTHING)
    # pcs_head = models.ForeignKey(Pchead, on_delete=models.DO_NOTHING)
    pc_member_last_name = models.CharField(max_length=100)
    pc_member_first_name = models.CharField(max_length=100, blank=True)
    pc_member_othername = models.CharField(max_length=100, blank=True)
    whats_phone = models.CharField(max_length=100, blank=True)
    pc_member_phone = models.CharField(max_length=15, unique=True)
    pc_member_gps_address = models.CharField(max_length=15, blank=True)
    pc_member_house_address = models.CharField(max_length=200, blank=True)
    chapel = models.CharField(choices=NAME_CHAPEL, max_length=100, blank=True)
    slug = models.SlugField(unique=True, help_text='Enter any text', default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pcs_head = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.pc_member_last_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.pc_member_last_name + "-" + rand_slug())
        super(PcMember, self).save(*args, **kwargs)

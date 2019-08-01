from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

PARAGRAPH_CHOICES = (
    ('txtsimple', 'Texto Simple'),
    ('txtsimple-img', 'Texto con imagen'),
    ('txtimg-left', 'Texto con imagen a la izquierda'),
    ('txtimg-right', 'Texto con imagen a la derecha'),
)
RESOUCES_CHOICES = (
    ('align-left', 'Bloque Izquierdo'),
    ('align-right', 'Bloque Derecho'),
)

from django.utils.safestring import mark_safe

class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to="img/Avatars-Users", verbose_name="Imagen", blank=True, null=True, default = 'img/Avatars-Users/usuario.png')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Home(models.Model):
    title = models.CharField(max_length = 200)
    subtitle = models.CharField(max_length = 200, blank=True, null=True)
    text = models.TextField(max_length=1500)
    image = models.ImageField(upload_to="img/Home-articles", verbose_name="Imagen", blank=True, null=True)
    typeClass = models.CharField(max_length= 40, choices = PARAGRAPH_CHOICES, default = 'txtsimple')
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('admin_Home_Articles_List')

class HomeForm(ModelForm):
    class Meta:
        model = Home
        ##fields = '__all__'
        fields = 'title', 'subtitle', 'text', 'typeClass', 'image',
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Titulo'}),
            'subtitle': forms.TextInput(attrs={'placeholder': 'Subtitulo'}),
            'text': forms.Textarea(
                attrs={'placeholder': 'Todo el texto del parrafo'}),
        }

class Carreras(models.Model):
    name = models.CharField(max_length = 200)
    objetive = models.TextField(max_length=1500)
    review = models.TextField(max_length=1500)
    studyPlan = models.FileField(upload_to="documents/Careers-docs", verbose_name="Study Plan", blank=True, null=True)
    typeClass = models.CharField(max_length= 40, choices = PARAGRAPH_CHOICES, default = 'txtsimple')
    image = models.ImageField(upload_to="img/Careers-articles", verbose_name="Imagen", blank=True, null=True)
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('admin_Carrer_Articles_List')

class RecursosDestacados(models.Model):
    name = models.CharField(max_length = 200)
    resource = models.FileField(upload_to = "documents/Resource-Relevant", verbose_name = "Recurso")
    typeClass = models.CharField(max_length = 30, choices = RESOUCES_CHOICES, default = 'align-left')
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('admin_Resources_Articles_List')

class Evaluation(models.Model):
    name = models.CharField(max_length = 100)
    unityOne = models.TextField(max_length= 2500, blank=True, null=True)
    unityTwo = models.TextField(max_length= 2500, blank=True, null=True)
    unityThree = models.TextField(max_length= 2500, blank=True, null=True)
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('admin_Evaluation_Articles_List')

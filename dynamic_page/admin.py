from django.contrib import admin
from .models import Home, Carreras, RecursosDestacados, Evaluation, Profile
from django.contrib.auth.models import User

# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'text', 'image', 'typeClass')
    fields = ['title', 'subtitle', 'text', 'typeClass','image']

class CarrerasAdmin(admin.ModelAdmin):
    list_display = ('name', 'objetive', 'review', 'studyPlan')
    fields = ['name', 'objetive', 'review', 'studyPlan']

class RecursosDestacadosAdmin(admin.ModelAdmin):
    list_display = ('name', 'resource', 'typeClass')
    fields = ['name', 'resource', 'typeClass']
    
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('name', 'unityOne', 'unityTwo', 'unityThree')
    fields = ['name', 'unityOne', 'unityTwo', 'unityThree']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')
    fields = ['user', 'avatar']

admin.site.register(Home, HomeAdmin)
admin.site.register(Carreras, CarrerasAdmin)
admin.site.register(RecursosDestacados, RecursosDestacadosAdmin)
admin.site.register(Evaluation, EvaluationAdmin)
admin.site.register(Profile, ProfileAdmin)







































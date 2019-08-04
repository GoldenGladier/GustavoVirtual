from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Home, Carreras, RecursosDestacados, Evaluation, HomeForm, Profile
from django.template import loader
from django.views import generic, View
# from django.views import View
from django.views.generic import ListView

# from .models import HomeForm
from django import forms
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm, ContactForm



# Create your views here.
class HomeList(ListView):
    model = Home
    context_object_name = 'home_list'
    template_name = "index.html"

class ParagraphsList(ListView):
    model = Home
    context_object_name = 'paragraphs_list'
    template_name = "administration/admin_Home.html"
    paginate_by = 4
    queryset = Home.objects.all()


class AdminParagraphsList(LoginRequiredMixin, ListView):
    model = Home
    context_object_name = 'paragraphs_list'
    template_name = "administration/admin_Home.html"
    paginate_by = 4
    queryset = Home.objects.all()

class CarrerList(ListView):
    model = Carreras
    context_object_name = 'paragraphs_list'
    template_name = "carreras.html"

class AdminCarrerList(LoginRequiredMixin, ListView):
    model = Carreras
    context_object_name = 'paragraphs_list'
    template_name = "administration/admin_Carrer.html"
    success_url = 'admin_Carrer_Articles_List'
    paginate_by = 5
    queryset = Carreras.objects.all()

class ResourceList(ListView):
    model = RecursosDestacados
    context_object_name = 'resource_list'
    template_name = "recursos.html"

class AdminResourcesList(LoginRequiredMixin, ListView):
    model = RecursosDestacados
    context_object_name = 'admin_list'
    template_name = "administration/admin_Resources.html"
    form_class = HomeForm
    success_url = 'admin_Resources_Articles_List'
    paginate_by = 6
    queryset = RecursosDestacados.objects.all()



def post_new(request):
    form = HomeForm()
    return render(request, 'Gustavo_Virtual/AdminMaster.html', {'form': form})

from django.http import HttpResponseRedirect

@login_required 
def add_post_Home(request):
    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():
            new_post_home = form.save()

            return HttpResponseRedirect('/Gustavo_Virtual/AdminMaster/home-articles-list')
    else:
        form = HomeForm()
    return render(request, 'administration/admin_Home_Add_Article.html', {'form': form})

class HomeDelete(LoginRequiredMixin, DeleteView):
    model = Home
    template_name = "administration/home_confirm_delete.html"
    success_url = reverse_lazy('admin_Home_Articles_List')

class HomeUpdate(LoginRequiredMixin, UpdateView):
    model = Home
    fields = 'title', 'subtitle', 'text', 'typeClass', 'image',
    template_name = 'administration/home_form.html'

class CarrerCreate(LoginRequiredMixin, CreateView):
    model = Carreras
    fields =  '__all__' 
    template_name = 'administration/carrer_form.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(CarrerCreate, self).get_form(form_class)
        form.fields['name'].widget.attrs ={'placeholder': 'Nombre', 'class':'someclass'}
        form.fields['objetive'].widget.attrs ={'placeholder': 'Objetivo', 'class':'someclass'}
        form.fields['review'].widget.attrs ={'placeholder': 'Reseña', 'class':'someclass'}
        form.fields['studyPlan'].widget.attrs ={'placeholder': 'Nombre', 'class':'upload'}

        return form

class CarrerUpdate(LoginRequiredMixin, UpdateView):
    model = Carreras
    fields = '__all__'
    template_name = 'administration/carrer_form.html'
    
class CarrerDelete(LoginRequiredMixin, DeleteView):
    model = Carreras
    template_name = "administration/carrer_confirm_delete.html"
    success_url = reverse_lazy('admin_Carrer_Articles_List')


class ResourceCreate(LoginRequiredMixin, CreateView):
    model = RecursosDestacados
    fields =  '__all__' 
    template_name = 'administration/resources_form.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(ResourceCreate, self).get_form(form_class)
        form.fields['name'].widget.attrs ={'placeholder': 'Nombre'}
        return form

class ResourceUpdate(LoginRequiredMixin, UpdateView):
    model = RecursosDestacados
    fields = '__all__'
    template_name = 'administration/resources_form.html'
    
class ResourceDelete(LoginRequiredMixin, DeleteView):
    model = RecursosDestacados
    template_name = "administration/carrer_confirm_delete.html"
    success_url = reverse_lazy('admin_Resources_Articles_List')


class evaluationList(ListView):
   model = Evaluation
   template_name = 'evaluacion.html'

class AdminEvaluationList(LoginRequiredMixin, ListView):
    model = Evaluation
    context_object_name = 'evaluation_list'
    template_name = "administration/admin_Evaluation.html"
    paginate_by = 5
    queryset = Evaluation.objects.all()


class EvaluationCreate(LoginRequiredMixin, CreateView):
    model = Evaluation
    fields =  '__all__' 
    template_name = 'administration/evaluation_form.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(EvaluationCreate, self).get_form(form_class)
        form.fields['name'].widget.attrs ={'placeholder': 'Nombre'}
        form.fields['unityOne'].widget.attrs ={'placeholder': 'Evaluación de Primer parcial'}
        form.fields['unityTwo'].widget.attrs ={'placeholder': 'Evaluación de Segundo parcial'}
        form.fields['unityThree'].widget.attrs ={'placeholder': 'Evaluación de Tercer parcial'}

        return form

class EvaluationUpdate(LoginRequiredMixin, UpdateView):
    model = Evaluation
    fields = '__all__'
    template_name = 'administration/evaluation_form.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(EvaluationUpdate, self).get_form(form_class)
        form.fields['name'].widget.attrs ={'placeholder': 'Nombre'}
        form.fields['unityOne'].widget.attrs ={'placeholder': 'Evaluación de Primer parcial'}
        form.fields['unityTwo'].widget.attrs ={'placeholder': 'Evaluación de Segundo parcial'}
        form.fields['unityThree'].widget.attrs ={'placeholder': 'Evaluación de Tercer parcial'}

        return form
    
class EvaluationDelete(LoginRequiredMixin, DeleteView):
    model = Evaluation
    template_name = "administration/evaluation_confirm_delete.html"
    success_url = reverse_lazy('admin_Evaluation_Articles_List')

from django.contrib.auth.forms import UserCreationForm

@login_required 
def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return HttpResponseRedirect('/Gustavo_Virtual/AdminMaster/home-articles-list')
    else:
        form = UserCreationForm()
        profile_form = ProfileForm()
    return render(request, 'administration/user_form.html', {'form':form, 'profile_form': profile_form})


from django.contrib import messages


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, ('¡El perfil ah sido actualizado!'))
            return redirect('/Gustavo_Virtual/AdminMaster/home-articles-list')
        else:
            messages.error(request, ('Porfavor corrige el error.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'administration/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


class AdminUserList(LoginRequiredMixin, ListView):
    model = User
    context_object_name = 'user_list'
    template_name = "administration/admin_user.html"
    paginate_by = 5
    queryset = User.objects.all()   

@login_required
def update_profile_ID(request, id_user):
    usr = User.objects.get(id = id_user)
    if request.method == 'GET':
        user_form = UserForm(instance=usr)
        profile_form = ProfileForm(instance=usr.profile)
    else:
        user_form = UserForm(request.POST, instance=usr)
        profile_form = ProfileForm(request.POST, request.FILES, instance=usr.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        return redirect('/Gustavo_Virtual/AdminMaster/home-articles-list')
    return render(request, 'administration/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def delete_profile_ID(request, id_user):
    usr = User.objects.get(id = id_user)
    user_form = UserForm(instance=usr)
    profile_form = ProfileForm(instance=usr.profile)
    if request.method == 'POST':
        usr.delete()
        return redirect('admin_User_List')
    return render(request, 'administration/delete_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

from django.core.mail import EmailMessage
from django.template.loader import get_template


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            template = get_template('contact_template.txt')
                # plaintext = get_template('email.txt')

            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "Mensaje desde GustavoVirtual - Alguien quiere contactarte",
                content,
                "omar.fi.wwr@gmail.com" +'',
                ['omar.fi.wwr@gmail.com'],
                headers = {'Responder a:': contact_email }
            )
            email.send()
            return redirect('contacto.html')

    return render(request, 'contacto.html', {
        'form': form_class
    })
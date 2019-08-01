from django.urls import path
from django.conf.urls import url
from django import views
from . import views
from dynamic_page.views import ParagraphsList
from django.conf.urls import include
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.HomeList.as_view(), name= 'index.html'),
    path('index.html', views.HomeList.as_view(), name= 'index.html'),
    path('carreras.html', views.CarrerList.as_view(), name= 'carreras.html'),
    path('recursos.html', views.ResourceList.as_view(), name= 'recursos.html'),
    path('evaluacion.html', views.evaluationList.as_view(), name= 'evaluacion.html'),
    path('contacto.html', views.contact , name= 'contacto.html'),
    
    url(r'^formularios.html', TemplateView.as_view(template_name='formularios.html'), name='formularios.html'),
    url(r'^bibliografia.html', TemplateView.as_view(template_name='bibliografia.html'), name='bibliografia.html'),

    path('AdminMaster/', views.add_post_Home, name= 'admin_Home.html'),
    
    path('AdminMaster/home-articles-list', views.AdminParagraphsList.as_view(), name= 'admin_Home_Articles_List'),
    path('AdminMaster/home-articles-list/add', views.add_post_Home, name= '/add'),
    
    path('AdminMaster/carrer-articles-list', views.AdminCarrerList.as_view(), name= 'admin_Carrer_Articles_List'),
    path('AdminMaster/carrer-articles-list/add', views.CarrerCreate.as_view(), name= '/add-carrer'),

    path('AdminMaster/resources-articles-list', views.AdminResourcesList.as_view(), name= 'admin_Resources_Articles_List'),
    path('AdminMaster/resources-articles-list/add', views.ResourceCreate.as_view(), name= '/add-resource'),

    path('AdminMaster/evaluation-articles-list', views.AdminEvaluationList.as_view(), name= 'admin_Evaluation_Articles_List'),
    path('AdminMaster/evaluation-articles-list/add', views.EvaluationCreate.as_view(), name= '/add-evaluation'),

    path('AdminMaster/user-list', views.AdminUserList.as_view(), name= 'admin_User_List'),
    path('AdminMaster/user/add', views.create_user, name= 'add-user'),
    path('AdminMaster/user/edit', views.update_profile, name= 'edit-user'),
    url(r'AdminMaster/user-list/(?P<id_user>\d+)/update/$', views.update_profile_ID, name= 'edit-user-id'),
    url(r'AdminMaster/user-list/(?P<id_user>\d+)/delete/$', views.delete_profile_ID, name= 'delete-user-id'),


    url(r'^AdminMaster/resources-articles-list/(?P<pk>\d+)/update/$', views.ResourceUpdate.as_view(), name='resource-post-update'),
    url(r'^AdminMaster/resources-articles-list/(?P<pk>\d+)/delete/$', views.ResourceDelete.as_view(), name='resource-post-delete'),


    url(r'^AdminMaster/carrer-articles-list/(?P<pk>\d+)/update/$', views.CarrerUpdate.as_view(), name='carrer-post-update'),
    url(r'^AdminMaster/carrer-articles-list/(?P<pk>\d+)/delete/$', views.CarrerDelete.as_view(), name='carrer-post-delete'),


    url(r'^AdminMaster/home-articles-list/(?P<pk>\d+)/delete/$', views.HomeDelete.as_view(), name='post-delete'),
    url(r'^AdminMaster/home-articles-list/(?P<pk>\d+)/update/$', views.HomeUpdate.as_view(), name='post-update'),

    url(r'^AdminMaster/evaluation-articles-list/(?P<pk>\d+)/delete/$', views.EvaluationDelete.as_view(), name='evaluation-delete'),
    url(r'^AdminMaster/evaluation-articles-list/(?P<pk>\d+)/update/$', views.EvaluationUpdate.as_view(), name='evaluation-update'),

    url(r'^AdminMaster/accounts/', include('django.contrib.auth.urls')),
] 

## views.add_post_Home
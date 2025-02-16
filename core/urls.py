from django.contrib import admin
from django.urls import path
from core import views  # Importa todas as views corretamente

urlpatterns = [
    path('', views.index, name='index'),
    path('hire-me/', views.hire_me, name='hire_me'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('faq/', views.faq, name='faq'),
    path('privacy/', views.privacy, name='privacy'),
    path('payment/', views.payment, name='payment'),  # Página de pagamentos

    path('base/', views.base_view, name='base_view'),

]
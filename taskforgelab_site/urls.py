from django.contrib import admin
from django.urls import path, include
from core import views  # Certifique-se de que está importando as views corretamente


urlpatterns = [
    path('admin/', admin.site.urls),  # Painel de administração do Django
    path('', include('core.urls')),   # Inclui todas as URLs do app "core"
]


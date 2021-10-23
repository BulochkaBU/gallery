"""gallery_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from gallery_app.views import AutosViews, AnimalsViews, ArchitectureViews, IndexViews, AutoView, ArchitectureDetailView, \
    AnimalView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexViews.as_view(), name='index'),
    path('autos', AutosViews.as_view(), name='autos'),
    path('animals/', AnimalsViews.as_view(), name='animals'),
    path('architecture/', ArchitectureViews.as_view(), name='architecture'),

    path('autos/<int:auto_pk>', AutoView.as_view(), name='auto'),
    path('animals/<int:animal_pk>', AnimalView.as_view(), name='animal'),
    path('architecture/<int:architecture_pk>', ArchitectureDetailView.as_view(), name='architecture_detail'),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



"""dummy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import include
from dummyapp import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
app_name='dummyapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
    path('upload/',views.image,name='image'),
    path('gallery/',views.gallery,name='gallery'),
    path('',views.index,name='index'),

    ]
#additional url pattern for adding images or media

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
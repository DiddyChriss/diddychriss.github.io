"""Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from codedadies import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from home.views import home, about, projects, skils, contact, tictactoe
from codedadies.views import codedadies_home, new_search
from todoapp.views import home_view,delete_view, add_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('skils/', skils, name='skils'),
    path('contact/', contact, name='contact'),
    path('projects/codedadies/', codedadies_home, name='codedadies'),
    path('projects/new_search/', new_search, name='new_search'),
    path('projects/todoapp/', home_view, name='todoapp'),
    path('projects/todoapp/delete/<int:todo_id>/',delete_view ,name='delete'),
    path('projects/todoapp/add/',add_view,name='add'),
    path('projects/tictactoe',tictactoe,name='tictactoe')

              ]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

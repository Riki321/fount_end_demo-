"""hackthon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
urlpatterns = [
    #organization
    path('admin/', admin.site.urls),
    path('',views.HomePage,name="HomePage"),
    path('show_org',views.show_org,name="show_org"),
    path('insert_org',views.insert_org,name="insert_org"),
    path('sort_org',views.sort_org,name="sort_org"),
    path('edit_org/<str:id>',views.edit_org,name="edit_org"),
    path('update_org/<str:id>',views.update_org,name="update_org"),
    path('del_org/<str:id>',views.del_org,name="del_org"),
    path('deleted_org/<str:id>',views.deleted_org,name="deleted_org"),
    path('runQueryorg',views.runQueryorg,name="runQueryorg"),
    path('run_query',views.run_query,name="run_query"),
    path('custom_query',views.custom_query,name="custom_query"),

    #Pariticipants
    path('show_part',views.show_part,name="show_part"),
    path('insert_part',views.insert_part,name="insert_part"),
    path('sort_part',views.show_part,name="sort_part"),
    path('edit_part/<str:id>',views.edit_part,name="edit_part"),
    path('update_part/<str:id>',views.update_part,name="update_part"),
    path('del_part/<str:id>',views.del_part,name="del_part"),
    path('deleted_part/<str:id>',views.deleted_part,name="deleted_part"),
    path('runQuerypart',views.runQuerypart,name="runQuerypart"),
    path('run_query1',views.run_query1,name="run_query1"),
    path('custom_query1',views.custom_query1,name="custom_query1"),

]

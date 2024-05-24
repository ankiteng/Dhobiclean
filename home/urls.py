from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("contact",views.contact, name='contact'),
       
]
admin.site.site_header = ' DhobiClean Admin'                    # default: "Django Administration"
admin.site.index_title = 'Laundry Project'                 # default: "Site administration"
admin.site.site_title = 'Ankit'
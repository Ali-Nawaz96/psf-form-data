
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('form_submit', views.form_submit, name='form_submit'),

]

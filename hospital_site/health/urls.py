from django.urls import path

from health import views
urlpatterns = [
    path('hospital_index/', views.hospital_index, name='hospital_index'),
    path('hospital_about/', views.hospital_about, name='hospital_about'),
    path('hospital_appointment/', views.hospital_appointment, name='hospital_appointment'),
    path('form_process/', views.form_process, name='form_process'), 
    path('success/', views.success, name='success') 
]

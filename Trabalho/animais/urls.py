from django.urls import path
from . import views
urlpatterns = [
    path('',views.main,name='main'),
    path('animais/', views.animais, name='animais'),
    path('animais/detalhes/<int:id>',views.detalhes,name='detalhes'),
    path('testing/', views.testing, name='testing'),

]
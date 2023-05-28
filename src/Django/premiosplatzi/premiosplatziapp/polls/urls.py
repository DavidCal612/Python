from django.urls import path

from . import views

# CREACION DE VISTAS EN PYTHON 

urlpatterns = [
    path("", views.index, name="index"),
    #ex: /polls/5/
    path("<int:question_id>/", views.detail, name="index"),
    #ex: /polls/5/
    path("<int:question_id>/results/", views.results, name="index"),
    #ex: /polls/5/
    path("<int:question_id>/vote/", views.vote, name="index"),
]

# int:question_id>/ para poder pasar parametros mediante la URL que estamps utilizando para una pagina web 


from django.urls import path

from . import views

# CREACION DE VISTAS EN PYTHON  # /polls/{{question.id}} 
app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    #ex: /polls/5/
    path("<int:question_id>/detail/paginadetails", views.detail, name="detail"),
    #ex: /polls/5/
    path("<int:question_id>/results/", views.results, name="results"),
    #ex: /polls/5/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

# int:question_id>/ para poder pasar parametros mediante la URL que estamps utilizando para una pagina web 


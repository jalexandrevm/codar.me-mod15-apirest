from django.contrib import admin
from django.urls import path, re_path

from agenda.views import agendamento_detail_delete_alter, agendamento_list_create, horarios_list

urlpatterns = [
    # path('agendamentos/', agendamento_list),
    path('agendamentos/', agendamento_list_create),
    path('agendamentos/<int:id>/', agendamento_detail_delete_alter),
    path('horarios/', horarios_list),
]

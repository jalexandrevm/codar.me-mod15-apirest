from django.contrib import admin
from django.urls import path, re_path

from agenda.views import (
    AgendamentoDetalheAlteraCancela,
    AgendamentoListCreate,
    AgendamentoListHorario,
    PrestadorList,
)

urlpatterns = [
    # path('agendamentos/', agendamento_list),
    # path('agendamentos/', agendamento_list_create),
    # path('agendamentos/<int:id>/', agendamento_detail_delete_alter),
    # path('horarios/', horarios_list),
    path("agendamentos/", AgendamentoListCreate.as_view()),
    path("agendamentos/<int:pk>/", AgendamentoDetalheAlteraCancela.as_view()),
    path("horarios/", AgendamentoListHorario.as_view()),
    path("prestadores/", PrestadorList.as_view()),
]

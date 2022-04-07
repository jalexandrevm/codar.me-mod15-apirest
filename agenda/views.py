from datetime import datetime, timedelta
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from django.utils import timezone
import pytz
import re

from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer

# Create your views here.
# parte do exercício 4 (listar e criar)
@api_view(http_method_names=["GET", "POST"])
def agendamento_list_create(request):
    if request.method == "GET":
        # qs = Agendamento.objects.all() # mudar para apenas ativo
        qs = Agendamento.objects.filter(cancelado=False)
        serializer = AgendamentoSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
# parte do exercício 4 (detalhar)
@api_view(http_method_names=["GET", "DELETE", "PUT", "PATCH"])
def agendamento_detail_delete_alter(request, id):
    obj = get_object_or_404(Agendamento, id=id)
    if request.method == "GET":
        serializer = AgendamentoSerializer(obj)
        return JsonResponse(serializer.data)
    if request.method == "DELETE":
        # obj.delete() # alterado para apenas cancelar
        # exercício 5 pra cancelar agendamento
        obj.cancelado = True
        obj.save()
        serializer = AgendamentoSerializer(obj)
        return JsonResponse(serializer.data, status=202)
    # deprecated use POST or PATCH
    if request.method == "PUT":
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            dado_valido = serializer.validated_data
            obj.data_horario = dado_valido.get("data_horario", obj.data_horario)
            obj.nome_cliente = dado_valido.get("nome_cliente", obj.nome_cliente)
            obj.email_cliente = dado_valido.get("email_cliente", obj.email_cliente)
            obj.telefone_cliente = dado_valido.get("telefone_cliente", obj.telefone_cliente)
            obj.save()
            return JsonResponse(serializer.data, status=202)
        return JsonResponse(serializer.errors, status=400)
    if request.method == "PATCH":
        serializer = AgendamentoSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=202)
        return JsonResponse(serializer.errors, status=400)
@api_view(http_method_names=["GET"])
def horarios_list(request):
    if request.method == "GET":
        data = request.query_params.get("data")
        if data:
            try:
                data_ini = data_fim = datetime.fromisoformat(data).replace(tzinfo=pytz.UTC)
                data_fim += timedelta(hours=23, minutes=59)
                objs = Agendamento.objects.filter(data_horario__gte=data_ini).filter(data_horario__lt=data_fim).filter(cancelado=False)
                serializer = AgendamentoSerializer(objs, many=True)
                return JsonResponse(serializer.data, status=200, safe=False)
            except ValueError as v_error:
                dict_error = {"erro": str(v_error)}
                return JsonResponse(dict_error, status=400, safe=False)
        objs = Agendamento.objects.all().filter(cancelado=False)#.order_by('-data_horario')
        serializer = AgendamentoSerializer(objs, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    return JsonResponse(request.data, status=400)
    pass

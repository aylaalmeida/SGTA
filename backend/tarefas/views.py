from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from .models import Tarefa
from django.utils import timezone

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_abertas(request):  
    tarefas = Tarefa.objects.filter(status='ABERTA').values()
    return JsonResponse(list(tarefas), safe=False)

def buscar_tarefa_por_id(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    return JsonResponse(model_to_dict(tarefa))

def listar_tarefas_urgentes_abertas(request):
    tarefas = Tarefa.objects.filter(status='ABERTA', prioridade='URGENTE').values()
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_por_prioridade(request, prioridade):
    tarefas = Tarefa.objects.filter(prioridade=prioridade).values()
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_atrasadas(request):
    hoje = timezone.now().date()
    tarefas = Tarefa.objects.filter(
        data_entrega__lt=hoje
    ).exclude(status='CONCLUIDA').values()
    return JsonResponse(list(tarefas), safe=False)

def buscar_tarefas_por_titulo(request, termo):
    tarefas = Tarefa.objects.filter(titulo__icontains=termo).values()
    return JsonResponse(list(tarefas), safe=False)
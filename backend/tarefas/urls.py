from django.urls import path
from .views import buscar_tarefa_por_id, buscar_tarefas_por_titulo, listar_tarefas, listar_tarefas_abertas, listar_tarefas_atrasadas, listar_tarefas_urgentes_abertas, listar_tarefas_por_prioridade

urlpatterns = [
    path('tarefas/abertas/', listar_tarefas_abertas), 
    path('tarefas/', listar_tarefas),
    path('tarefas/<int:id>/', buscar_tarefa_por_id),
    path('tarefas/urgentes/', listar_tarefas_urgentes_abertas),
    path('tarefas/prioridade/<str:prioridade>/', listar_tarefas_por_prioridade),
    path('tarefas/atrasadas/', listar_tarefas_atrasadas),
    path('tarefas/busca/<str:termo>/', buscar_tarefas_por_titulo),
]
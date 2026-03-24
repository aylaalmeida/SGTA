from django.urls import path
from .views import listar_tarefas, listar_tarefas_abertas 

urlpatterns = [
    path('tarefas/abertas/', listar_tarefas_abertas), 
    path('tarefas/', listar_tarefas),
]
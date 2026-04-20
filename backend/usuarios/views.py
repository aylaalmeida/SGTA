from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Usuario

def listar_usuarios(request):
    usuarios = Usuario.objects.all().values('id', 'nome', 'email', 'ativo')
    return JsonResponse(list(usuarios), safe=False)

def buscar_usuario_por_id(request, id):
    try:
        usuario = Usuario.objects.get(id=id)
        dados = {
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email,
            "ativo": usuario.ativo
        }
        return JsonResponse(dados)
    except Usuario.DoesNotExist:
        return JsonResponse({"erro": "Usuário não encontrado"}, status=404)
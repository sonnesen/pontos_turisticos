from django.http.response import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao', 'endereco__linha1',)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    
    @action(methods=['posts'], detail=True)
    def associa_atracoes(self, request, id):
        atracoes = request.data['atracoes']
        ponto_turistico = PontoTuristico.objects.get(id=id)
        ponto_turistico.set(atracoes)
        ponto_turistico.save()
        
        return HttpResponse('OK', status_code=200)
    
        
#     def get_queryset(self):
#         id_ponto = self.request.query_params().get('id', None)
#         nome = self.request.query_params().get('nome', None)
#         descricao = self.request.query_params().get('descricao', None)
#         queryset = PontoTuristico.objects.all()
#         
#         if id:
#             queryset = queryset.filter(pk=id_ponto)
#         
#         if nome:
#             queryset = queryset.filter(nome__iexact=nome)
#             
#         if descricao:
#             queryset = queryset.filter(descricao__iexact=descricao)
#             
#         return queryset
    
#     def list(self, request, *args, **kwargs):
#         return ModelViewSet.list(self, request, *args, **kwargs)
# 
#     def create(self, request, *args, **kwargs):
#         return ModelViewSet.create(self, request, *args, **kwargs)
# 
#     def destroy(self, request, *args, **kwargs):
#         return ModelViewSet.destroy(self, request, *args, **kwargs)
# 
#     def update(self, request, *args, **kwargs):
#         return ModelViewSet.update(self, request, *args, **kwargs)
# 
#     def retrieve(self, request, *args, **kwargs):
#         return ModelViewSet.retrieve(self, request, *args, **kwargs)
# 
#     def partial_update(self, request, *args, **kwargs):
#         return ModelViewSet.partial_update(self, request, *args, **kwargs)
#
#     @action(methods=['get'], detail=True)
#     def denunciar(self, request, pk=None):
#         pass
#
#     @action(methods=['get'], detail=False)
#     def teste(self, request):
#         pass

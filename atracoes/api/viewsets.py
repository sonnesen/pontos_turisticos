from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from atracoes.api.serializers import AtracaoSerializer
from atracoes.models import Atracao


class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filter_fields = ('nome', 'descricao')
    search_fields = ('^nome', '^descricao')
    ordering_fields = ('nome', 'descricao')
    ordering = ('nome',)

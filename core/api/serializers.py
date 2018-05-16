from rest_framework.serializers import ModelSerializer

from atracoes.api.serializers import AtracaoSerializer
from atracoes.models import Atracao
from core.models import PontoTuristico
from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
#     comentarios = ComentarioSerializer(many=True)
#     avaliacoes = AvaliacaoSerializer(many=True)
    
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado',
                  'atracoes', 'comentarios', 'avaliacoes',
                  'endereco', 'foto')
        read_only_fields = ('comentarios', 'avaliacoes')

    def extract_atracao(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        return atracoes

    def extract_endereco(self, validated_data):
        endereco = validated_data['endereco']
        del validated_data['endereco']
        return endereco

    def create_atracoes(self, atracoes, ponto_turistico):
        for atracao in atracoes:
            nova_atracao = Atracao.objects.create(**atracao)
            ponto_turistico.atracoes.add(nova_atracao)

    def create_endereco(self, endereco, ponto_turistico):
        endereco = Endereco.objects.create(**endereco)
        ponto_turistico.endereco = endereco
        
    def create(self, validated_data):
        atracoes = self.extract_atracao(validated_data)
        endereco = self.extract_endereco(validated_data)
        ponto_turistico = PontoTuristico.objects.create(**validated_data)        
        
        self.create_atracoes(atracoes, ponto_turistico)
        self.create_endereco(endereco, ponto_turistico)
        ponto_turistico.save()
               
        return ponto_turistico

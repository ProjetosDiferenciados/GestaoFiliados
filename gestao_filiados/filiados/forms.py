from django import forms
from django.core.exceptions import ObjectDoesNotExist
from tse_importador.up.entidades.filiado_up import filiado_up
from tse_importador.up.entidades.profissao_enum import profissao_enum
from tse_importador.up.entidades.regiao_administrativa import regiao_administrativa
from tse_importador.tse.entidades.situacao_filiacao import situacao_filiacao, get_situacao_filiacao_por_nome
from .models import Filiado


class FiliadoForm(forms.Form):
    id = forms.IntegerField(required=False)
    nome_completo = forms.CharField(max_length=100)
    nome_social = forms.CharField(max_length=100, required=False)
    data_nascimento = forms.DateField()
    genero = forms.CharField(max_length=20)
    sexualidade = forms.CharField(max_length=20, required=False)
    raca = forms.CharField(max_length=20)
    pcd = forms.BooleanField(required=False)
    local_residencia = forms.CharField(max_length=100)
    local_exercicio = forms.ChoiceField(choices=[(tag.name, tag.value[0]['nome']) for tag in regiao_administrativa])
    tituloEleitor = forms.CharField(max_length=20)
    dataFiliacao = forms.DateField()
    uf = forms.CharField(max_length=2)
    zona = forms.IntegerField()
    situacao = forms.ChoiceField(choices=[(tag.name, tag.name) for tag in situacao_filiacao])
    profissao = forms.ChoiceField(choices=[(tag.name, tag.name) for tag in profissao_enum])
    etnia = forms.CharField(max_length=100)
    pendenciaComunicacao = forms.BooleanField(required=False)
    
    #usar método da entidade no tse_importador(?)
    def save(self):
        local_exercicio = regiao_administrativa[self.cleaned_data['local_exercicio']]
        situacao = get_situacao_filiacao_por_nome(self.cleaned_data['situacao'])

        filiado_novo = filiado_up(
            id=self.cleaned_data.get('id'),
            nome_completo=self.cleaned_data['nome_completo'],
            nome_social=self.cleaned_data.get('nome_social', ''),
            data_nascimento=self.cleaned_data['data_nascimento'],
            genero=self.cleaned_data['genero'],
            sexualidade=self.cleaned_data.get('sexualidade', ''),
            raca=self.cleaned_data['raca'],
            pcd=self.cleaned_data.get('pcd', False),
            local_residencia=self.cleaned_data['local_residencia'],
            local_exercicio=local_exercicio,
            tituloEleitor=self.cleaned_data['tituloEleitor'],
            dataFiliacao=self.cleaned_data['dataFiliacao'],
            uf=self.cleaned_data['uf'],
            zona=self.cleaned_data['zona'],
            situacao=situacao,
            profissao=self.cleaned_data.get('profissao_enum',profissao_enum.DESCONHECIDO),
            etnia=self.cleaned_data['etnia'],
            pendenciaComunicacao=self.cleaned_data.get('pendenciaComunicacao', False)
        )
        try :
            filiado_banco: Filiado = Filiado.objects.filter(tituloEleitor=filiado_novo.tituloEleitor).get()
            raise Exception(f'Filiado com título eleitor {filiado_novo.tituloEleitor} já existe')
        except ObjectDoesNotExist as e:
            filiado_ent = Filiado().setarCampos(filiado_novo)
            filiado_ent.save()
            return filiado_novo

class UploadFileForm(forms.Form):
    file = forms.FileField()
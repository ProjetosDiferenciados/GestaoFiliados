from django.shortcuts import render, redirect
from .forms import FiliadoForm, UploadFileForm
from .models import Filiado
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from tse_importador.tse.entidades.conversor.upload_filiado import upload_filiado
import pandas as pd

# Registro individual e visualização do BD
class FiliadoListView(ListView):
    model = Filiado
    template_name = 'filiados/list_filiado.html'

class FiliadoDetailView(DetailView):
    model = Filiado
    template_name = 'filiados/details_filiado.html'

class FiliadoCreateView(View):
    form_class = FiliadoForm
    initial = {}
    template_name = 'filiados/filiado_form.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_filiado')
        return render(request, self.template_name, {'form': form})
    
# Criar no tse_importador e fazer uma classe?
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            list_filiado: list = upload_filiado().converter_excel_to_filiado_list(file)
            for filiado_elem in list_filiado:
                ormFiliado = Filiado().instanciar(filiado_elem)
                ormFiliado.save()
            return redirect('list_filiado')
    else:
        form = UploadFileForm()
    return render(request, 'filiados/upload.html', {'form': form})

def display_file_content(request):
    data = request.session.get('data')
    if not data:
        return HttpResponse('Não há dados')
    return render(request, 'display_content.html', {'data': data})

def save_filiados(request):
    data = request.session.get('data')
    if not data:
        return HttpResponse('Não há dados')
    for item in data:
        filiado = Filiado(
            tituloEleitor=item.get('tituloEleitor'),
            nome=item.get('nome'),
            genero=item.get('genero'),
            dataFiliacao=item.get('dataFiliacao'),
            uf=item.get('uf'),
            municipio=item.get('municipio'),
            zona=item.get('zona'),
            situacao=item.get('situacao'),
            pendenciaComunicacao=item.get('pendenciaComunicacao', False),
            nome_completo=item.get('nome_completo'),
            nome_social=item.get('nome_social'),
            data_nascimento=item.get('data_nascimento'),
            sexualidade=item.get('sexualidade'),
            raca=item.get('raca'),
            pcd=item.get('pcd'),
            local_residencia=item.get('local_residencia'),
            local_exercicio=item.get('local_exercicio'),
        )
        filiado.save()
    return HttpResponse('Dados salvos!')
from django.urls import path
from . import views

urlpatterns = [
    path('', views.FiliadoListView.as_view(), name='list_filiado'),
    path('<int:pk>/', views.FiliadoDetailView.as_view(), name='details_filiado'),
    path('create/', views.FiliadoCreateView.as_view(), name='filiado-create'),
    path('upload-tse/', views.upload_file, name='upload_file'),
    path('upload-up/', views.upload_filiados_planilha_up, name='upload_file_up'),
    path('display/', views.display_file_content, name='display_file_content'),
    path('save/', views.save_filiados, name='save_filiados'),
]

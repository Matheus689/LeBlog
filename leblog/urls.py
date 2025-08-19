from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('post/<int:id>/', views.detalhe_post, name='detalhe_post'),
    path('categoria/<int:categoria_id>/', views.filtrar_por_categoria, name='filtrar_por_categoria'),
]

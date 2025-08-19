from django.shortcuts import render, get_object_or_404
from .models import Post, Categoria

def lista_posts(request):
    posts = Post.objects.order_by('-data_publicacao')
    categorias = Categoria.objects.all()
    return render(request, 'leblog/lista_posts.html', {'posts': posts, 'categorias': categorias})

def detalhe_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'leblog/detalhe_post.html', {'post': post})

def filtrar_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    posts = Post.objects.filter(categoria=categoria).order_by('-data_publicacao')
    categorias = Categoria.objects.all()
    return render(request, 'leblog/lista_posts.html', {'posts': posts, 'categorias': categorias, 'categoria_selecionada': categoria})

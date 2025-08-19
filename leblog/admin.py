from django.contrib import admin
from .models import Post, Categoria

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicacao', 'categoria')
    list_filter = ('categoria', 'data_publicacao')
    search_fields = ('titulo', 'conteudo')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

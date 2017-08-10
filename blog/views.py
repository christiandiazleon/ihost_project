from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


from blog.models import Article, Comment
from blog.forms import ArticleForm, CommentForm
from django.urls import reverse_lazy


from django.contrib.auth.mixins import LoginRequiredMixin
from ihost.mixins import UserProfileDataMixin
from django.contrib.auth.decorators import login_required


from django.views.generic import (ListView, DetailView,
                                    CreateView, UpdateView,
                                    DeleteView)

# Create your views here.


class ArticleListView(UserProfileDataMixin, ListView):
    template_name = 'ihost/home.html'
    model = Article
    paginate_by = 2

    # Permite usar el django ORM en las CBV genericas solamente
    # para personalizar el query acorde a lo que queremos es como un
    # sql query sobre mi modelo
    # Ver documentacion de field lookups
    # https://docs.djangoproject.com/en/1.11/topics/db/queries/#field-lookups
    def get_queryset(self):
        return Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class ArticleDetailView(UserProfileDataMixin, DetailView):
    model = Article

def article_detail(request, pk):
    pass




class CreateArticleView(LoginRequiredMixin, UserProfileDataMixin, CreateView):
    login_url = 'accounts/login/'
    redirect_field_name = 'blog/article_detail.html'
    form_class = ArticleForm

    model=Article


class ArticleUpdateView(LoginRequiredMixin, UserProfileDataMixin, UpdateView):
    login_url = 'accounts/login/'
    redirect_field_name = 'blog/article_detail.html'
    form_class = ArticleForm

    model=Article


class ArticleDeleteView(LoginRequiredMixin, UserProfileDataMixin, DeleteView):
    model=Article
    success_url = reverse_lazy('article_list')


class ArticleDraftListView(LoginRequiredMixin, UserProfileDataMixin, ListView):
    login_url = '/login/'
    # redirect_field_name = 'blog/article_list.html'
    template_name = 'ihost/home2.html'

    model = Article

    def get_queryset(self):
        return Article.objects.filter(published_date__isnull=True).order_by('created_date')

#######################################
## Functions that require a pk match ##
#######################################

@login_required
def article_publish(request, pk):
    article = get_object_or_404(Article,pk=pk)
    # View publish method in Article model
    article.publish()
    return redirect('article_detail', pk=pk)

@login_required
def add_comment_to_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # Queremos conectar ese comentario particular de un articulo
            # a un objeto articulo y grabarlo
            # ver en modelo Comment la F.K article
            comment.article = article
            comment.save()
            return redirect('article_detail', pk=article.pk)
    # Pero si el request method no es un POST, es decir, que alguien
    # no ha llenado el formulario de comentario, pinte el formulario
    # y pasamos en el contexto, un diccionario que contiene el form
    # a renderizar
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form':form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    # View approve method in Comment model which set one Comment object
    # to approved_comment = True
    comment.approve()
    return redirect('article_detail', pk=comment.article.pk)
    # Un comment esta conectado a un articulo particular en el modelo
    # Comment


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    article_pk = comment.article.pk
    comment.delete()
    return redirect('article_detail', pk=article_pk)
















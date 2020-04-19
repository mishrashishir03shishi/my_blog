from django.http import HttpResponseForbidden,HttpResponseRedirect,Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from .models import Article,Category,Comment
from django.db.models import Q
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import FormMixin
from .filters import ArticleFilter, CategoryArticleFilter
from django.contrib.messages.views import SuccessMessageMixin

class article_list(ListView):
    model = Article
    template_name='articles/article_list.html'

    def get_queryset(self):
        queryset = super(article_list, self).get_queryset()
        queryset = queryset.filter(approved=True)
        return queryset    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories']=Category.objects.all()
        context['filter']=ArticleFilter(self.request.GET, queryset=self.get_queryset())     
        return context
  
    

class article_detail(FormMixin,LoginRequiredMixin,DetailView):
    login_url='/accounts/login/'
    model=Article
    template_name='articles/article_detail.html'
    context_object_name = 'article'
    form_class=CommentForm


    def get_queryset(self):
        queryset = super(article_detail, self).get_queryset()
        queryset = queryset.filter(approved=True)
        return queryset


    def get_success_url(self):
        return reverse('articles:detail', kwargs={"pk": self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super(article_detail, self).get_context_data(**kwargs)
        context['categories']=Category.objects.all()
        context['comments'] = self.object.comments.filter()[:30]
        context['tags'] = self.object.tags.similar_objects()[:10]
        context['form']=self.get_form()         
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form): 
        new_comment = form.save(commit=False)
        new_comment.post = self.get_object()
        new_comment.name=self.request.user
        form.save()
        return super(article_detail,self).form_valid(form)
       
   
class article_create(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    login_url='/accounts/login/'
    model=Article
    template_name='articles/article_create.html'    
    fields=['title','body','thumb','category','tags']
    success_message='Thank You! Your Post will be published once the Admin has approved it!'



    def get_success_url(self):
        return reverse('articles:list')

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(article_create, self).get_context_data(**kwargs)
        context['categories']=Category.objects.all()
        return context


class article_edit(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    login_url='/accounts/login/'
    model=Article
    template_name='articles/article_edit.html'
    fields=['title','body','thumb']
    success_message='Your Article has been edited successfully'  

    def get_queryset(self):
        queryset = super(article_edit, self).get_queryset()
        queryset = queryset.filter(approved=True)
        return queryset 

    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(article_edit, self).get_context_data(**kwargs)
        context['categories']=Category.objects.all()
        return context


class article_delete(SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    login_url='/accounts/login/'
    model=Article
    template_name='articles/article_delete.html'
    success_url=reverse_lazy('articles:list')


    def get_queryset(self):
        queryset = super(article_delete, self).get_queryset()
        queryset = queryset.filter(approved=True)
        return queryset

    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(article_delete, self).get_context_data(**kwargs)
        context['categories']=Category.objects.all()
        return context
    


class categorywise_list(ListView):
    model = Article
    template_name='articles/article_list.html' 
    paginate_by=3   

    def get_queryset(self):
        queryset = super(categorywise_list, self).get_queryset()
        queryset = queryset.filter(approved=True,category_id=self.kwargs['item_id'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(categorywise_list, self).get_context_data(**kwargs)
        context['filter']=CategoryArticleFilter(self.request.GET, queryset=self.get_queryset()) 
        context['categories']=Category.objects.all()
        return context



def about(request):
    categories=Category.objects.all()
    return render(request, 'articles/about.html',{'categories':categories})

@login_required(login_url="/accounts/login/")
def comment_delete(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    article=comment.post    
    if comment.name==request.user:            
        comment.delete()
        return HttpResponseRedirect(reverse('articles:detail', kwargs={'pk':article.pk}))
    else:
        return HttpResponse('<h1>Invalid Request</h1>')
    
    return render(request,'articles/article_detail')
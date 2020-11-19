from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post
from .models import Campany,Division,Process,Subprocess,Failuretype,ExpenseItems,Order
from .forms import PostForm
from .forms import CampanyForm,DivisionForm,ProcessForm,SubprocessForm,OrderForm,ProcessForm2
from django.views import generic
from django.views.generic import TemplateView
from django.http import JsonResponse

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
#            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
#            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

@login_required
def post_list2(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list2.html', {'posts':posts})

class MasterSelect(TemplateView):
    template_name = 'blog/master_select.html'
master_select = MasterSelect.as_view()

#会社マスタ
@login_required
def post_campany_list(request):
    posts = Campany.objects.all()
    return render(request, 'blog/post_campany_list.html', {'posts':posts})

def post_campany_detail(request, pk):
    post = get_object_or_404(Campany, pk=pk)
    return render(request, 'blog/post_campany_detail.html', {'post': post})

@login_required
def post_campany_new(request):
    if request.method == "POST":
        form = CampanyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
#            post.author = request.user
            post.save()
            return redirect('post_campany_list',)
    else:
        form = CampanyForm()
    return render(request, 'blog/post_campany_edit.html', {'form': form})

@login_required
def post_campany_edit(request, pk):
    post = get_object_or_404(Campany, pk=pk)
    if request.method == "POST":
        form = CampanyForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_campany_detail', pk=post.pk)
    else:
        form = CampanyForm(instance=post)
    return render(request, 'blog/post_campany_edit.html', {'form': form})

#部門マスタ
@login_required
def post_division_list(request):
    posts = Division.objects.all()
    return render(request, 'blog/post_division_list.html', {'posts':posts})

@login_required
def post_division_detail(request, pk):
    post = get_object_or_404(Division, pk=pk)
    return render(request, 'blog/post_division_detail.html', {'post': post})

@login_required
def post_division_new(request):
    if request.method == "POST":
        form = DivisionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
#            post.author = request.user
            post.save()
            return redirect('post_division_list',)
    else:
        form = DivisionForm()
    return render(request, 'blog/post_division_edit.html', {'form': form})

@login_required
def post_division_edit(request, pk):
    post = get_object_or_404(Division, pk=pk)
    if request.method == "POST":
        form = DivisionForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_division_detail', pk=post.pk)
    else:
        form = DivisionForm(instance=post)
    return render(request, 'blog/post_division_edit.html', {'form': form})

#工程マスタ
@login_required
def post_process_list(request):
    posts = Process.objects.all()
    return render(request, 'blog/post_process_list.html', {'posts':posts})

@login_required
def post_process_detail(request, pk):
    post = get_object_or_404(Process, pk=pk)
    return render(request, 'blog/post_process_detail.html', {'post': post})

@login_required
def post_process_new(request):
    if request.method == "POST":
        form = ProcessForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_process_list',)
    else:
        form = ProcessForm()
    return render(request, 'blog/post_process_edit.html', {'form': form})

@login_required
def post_process_edit(request, pk):
    post = get_object_or_404(Process, pk=pk)
    if request.method == "POST":
        form = ProcessForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_process_detail', pk=post.pk)
    else:
        form = ProcessForm(instance=post)
    return render(request, 'blog/post_process_edit.html', {'form': form})
#テスト
class ProcessCreate(generic.CreateView):
    model = Process
    form_class = ProcessForm2
    template_name = 'blog/post_process_edit2.html'
    success_url = '/'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['campany_list'] = Campany.objects.all()
#        return context

def ajax_get_category(request):
         pk = request.GET.get('pk')

         if not pk:
             division_list = Division.objects.all()

         else:
            division_list = Division.objects.filter(campany_pk=pk)

         division_list =[{'pk': division.pk, 'name': division.name} for division in division_list]

         return JsonResponse({'divisionList':division_list})


#設備コードマスタ
@login_required
def post_subprocess_list(request):
    posts = Subprocess.objects.all()
    return render(request, 'blog/post_subprocess_list.html', {'posts':posts})

@login_required
def post_subprocess_detail(request, pk):
    post = get_object_or_404(Subprocess, pk=pk)
    return render(request, 'blog/post_subprocess_detail.html', {'post': post})

@login_required
def post_subprocess_new(request):
    if request.method == "POST":
        form = SubprocessForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_subprocess_list',)
    else:
        form = SubprocessForm()
    return render(request, 'blog/post_subprocess_edit.html', {'form': form})

@login_required
def post_subprocess_edit(request, pk):
    post = get_object_or_404(Subprocess, pk=pk)
    if request.method == "POST":
        form = SubprocessForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_subprocess_detail', pk=post.pk)
    else:
        form = SubprocessForm(instance=post)
    return render(request, 'blog/post_subprocess_edit.html', {'form': form})

#依頼指示書
@login_required
def post_order_list(request):
    posts = Order.objects.all()
    return render(request, 'blog/post_order_list.html', {'posts':posts})

@login_required
def post_order_detail(request, pk):
    post = get_object_or_404(Order, pk=pk)
    return render(request, 'blog/post_order_detail.html', {'post': post})

@login_required
def post_order_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_order_list',)
    else:
        form = OrderForm()
    return render(request, 'blog/post_order_edit.html', {'form': form})

@login_required
def post_order_edit(request, pk):
    post = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_order_detail', pk=post.pk)
    else:
        form = OrderForm(instance=post)
    return render(request, 'blog/post_order_edit.html', {'form': form})

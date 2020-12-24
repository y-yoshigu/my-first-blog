from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy
from .models import Post
from .models import Campany,Division,Process,Subprocess,Failuretype,ExpenseItems,Order
from .forms import PostForm
from .forms import CampanyForm,DivisionForm,ProcessForm,SubprocessForm,OrderForm,FailuretypeForm,ExpenseItemsForm
from .forms import OrderSearchFormSet
from django.views import generic
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.db.models import Q

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

#@login_required
#def post_process_new2(request):
#    if request.method == "POST":
#        form = ProcessForm(request.POST)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.save()
#            return redirect('post_process_list',)
#    else:
#        form = ProcessForm()
#    return render(request, 'blog/post_process_edit.html', {'form': form})

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

class post_process_new(generic.CreateView):
    model = Process
    form_class = ProcessForm
    template_name = 'blog/post_process_edit.html'
    success_url = reverse_lazy('post_process_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campany_list'] = Campany.objects.all()
        return context

#設備コードマスタ
@login_required
def post_subprocess_list(request):
    posts = Subprocess.objects.all()
    return render(request, 'blog/post_subprocess_list.html', {'posts':posts})

@login_required
def post_subprocess_detail(request, pk):
    post = get_object_or_404(Subprocess, pk=pk)
    return render(request, 'blog/post_subprocess_detail.html', {'post': post})

#@login_required
#def post_subprocess_new(request):
#    if request.method == "POST":
#        form = SubprocessForm(request.POST)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.save()
#            return redirect('post_subprocess_list',)
#    else:
#        form = SubprocessForm()
#    return render(request, 'blog/post_subprocess_edit.html', {'form': form})

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

class post_subprocess_new(generic.CreateView):
    model = Subprocess
    form_class = SubprocessForm
    template_name = 'blog/post_subprocess_edit.html'
    success_url = reverse_lazy('post_subprocess_list')

def ajax_get_division(request):
         pk = request.GET.get('pk')

         if not pk:
             parentCategory_list = Division.objects.all()

         else:
             parentCategory_list = Division.objects.filter(campany__pk=pk)

         parentCategory_list =[{'pk': division.pk, 'name': division.name} for division in parentCategory_list]

         return JsonResponse({'parentCategoryList':parentCategory_list})


def ajax_get_process(request):
         pk = request.GET.get('pk')

         if not pk:
#             process_list = Process.objects.all()
             process_list = null

         else:
             process_list = Process.objects.filter(division__pk=pk)

         process_list =[{'pk': process.pk, 'name': process.name} for process in process_list]

         return JsonResponse({'processList':process_list})

#工事区分マスタ
@login_required
def post_failuretype_list(request):
    posts = Failuretype.objects.all()
    return render(request, 'blog/post_failuretype_list.html', {'posts':posts})

#@login_required
#def post_subprocess_detail(request, pk):
#    post = get_object_or_404(Subprocess, pk=pk)
#    return render(request, 'blog/post_subprocess_detail.html', {'post': post})

@login_required
def post_failuretype_new(request):
    if request.method == "POST":
        form = FailuretypeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_failuretype_list',)
    else:
        form = FailuretypeForm()
    return render(request, 'blog/post_failuretype_edit.html', {'form': form})

@login_required
def post_failuretype_edit(request, pk):
    post = get_object_or_404(Failuretype, pk=pk)
    if request.method == "POST":
        form = FailuretypeForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_failuretype_list',)
    else:
        form = SubprocessForm(instance=post)
    return render(request, 'blog/post_failuretype_edit.html', {'form': form})

#費目マスタ
@login_required
def post_expenseItems_list(request):
    posts = ExpenseItems.objects.all()
    return render(request, 'blog/post_expenseItems_list.html', {'posts':posts})

#@login_required
#def post_subprocess_detail(request, pk):
#    post = get_object_or_404(Subprocess, pk=pk)
#    return render(request, 'blog/post_subprocess_detail.html', {'post': post})

@login_required
def post_expenseItems_new(request):
    if request.method == "POST":
        form = ExpenseItemsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_expenseItems_list',)
    else:
        form = ExpenseItemsForm()
    return render(request, 'blog/post_expenseItems_edit.html', {'form': form})

@login_required
def post_expenseItems_edit(request, pk):
    post = get_object_or_404(ExpenseItems, pk=pk)
    if request.method == "POST":
        form = ExpenseItemsForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_expenseItems_list',)
    else:
        form = ExpenseItemsForm(instance=post)
    return render(request, 'blog/post_expenseItems_edit.html', {'form': form})

#依頼指示書
@login_required
def post_order_list(request):
    posts = Order.objects.all()
    return render(request, 'blog/post_order_list.html', {'posts':posts})

@login_required
def post_order_detail(request, pk):
    post = get_object_or_404(Order, pk=pk)
    return render(request, 'blog/post_order_detail.html', {'post': post})

#@login_required
#def post_order_new(request):
#    if request.method == "POST":
#        form = OrderForm(request.POST)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.save()
#            return redirect('post_order_list',)
#    else:
#        form = OrderForm()
#    return render(request, 'blog/post_order_edit.html', {'form': form})

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

class post_order_new(generic.CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'blog/post_order_edit.html'
    success_url = reverse_lazy('post_order_list')

def ajax_get_divisionCategory(request):
         pk = request.GET.get('pk')

         if not pk:
             divisionCategory_list = Division.objects.all()

         else:
             divisionCategory_list = Division.objects.filter(campany__pk=pk)

         divisionCategory_list =[{'pk': division.pk, 'name': division.name} for division in divisionCategory_list]

         return JsonResponse({'divisionCategoryList':divisionCategory_list})


def ajax_get_processCategory(request):
         pk = request.GET.get('pk')

         if not pk:
#             process_list = Process.objects.all()
             processCategory_list = null

         else:
             processCategory_list = Process.objects.filter(division__pk=pk)

         processCategory_list =[{'pk': process.pk, 'name': process.name} for process in processCategory_list]

         return JsonResponse({'processCategoryList':processCategory_list})

def ajax_get_subprocessCategory(request):
         pk = request.GET.get('pk')

         if not pk:
#             process_list = Process.objects.all()
             subprocessCategory_list = null

         else:
             subprocessCategory_list = Subprocess.objects.filter(process__pk=pk)

         subprocessCategory_list =[{'pk': subprocess.pk, 'name': subprocess.name} for subprocess in subprocessCategory_list]

         return JsonResponse({'subprocessCategoryList':subprocessCategory_list})

@login_required
def post_order_remove(request, pk):
    post = Order.objects.get(pk=pk)
    post.delete()
    return redirect('post_order_list')

@login_required
def post_order_allremove(request):
    post = Order.objects.all()
    post.delete()
    return redirect('post_order_list')



#抽出
@login_required
def post_ordersearch_list(request):
    OrderSearch_list = Order.objects.all()
    formset = OrderSearchFormSet(request.POST or None)
    if request.method == 'POST':
        formset.is_valid()
        queries = []

        for form in formset:
            q_kwargs = {}
            campany_search = form.cleaned_data.get('campany_search')
            if campany_search:
                q_kwargs['campany'] = campany_search

            division_search = form.cleaned_data.get('division_search')
            if division_search:
                q_kwargs['division'] = division_search

            process_search = form.cleaned_data.get('process_search')
            if process_search:
                q_kwargs['process'] = process_search

            subjectName_search = form.cleaned_data.get('subjectName_search')
            if subjectName_search:
                q_kwargs['subjectName__contains'] = subjectName_search

            app_date_search = form.cleaned_data.get('app_date_search')
            if app_date_search:
                q_kwargs['app_date__gte'] = app_date_search

            requestSection_M_search = form.cleaned_data.get('requestSection_M_search')
            if requestSection_M_search:
                q_kwargs['requestSection_M'] = requestSection_M_search

            if q_kwargs:
                q = Q(**q_kwargs)
                queries.append(q)

        if queries:
            base_query = queries.pop()
            for query in queries:
                base_query |= query
            OrderSearch_list = OrderSearch_list.filter(base_query)

    context = {
        'OrderSearch_list':OrderSearch_list,
        'formset':formset,
    }

    return render(request, 'blog/post_ordersearch_list.html', context)

#入力確認
@login_required
def post_clientApproval(request, pk):
    post = get_object_or_404(Order, pk=pk)
    post.approval_client()
    posts = Order.objects.all()

    return render(request, 'blog/post_order_list.html',{'posts':posts})

#電力検針
#QR読込
class QRreader(TemplateView):
    template_name = 'blog/post_qrreader_test.html'
QR_reader = QRreader.as_view()

#電力入力
@login_required
def post_pMeterReading_edit(request, pk):
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

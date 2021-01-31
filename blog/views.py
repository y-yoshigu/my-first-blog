import csv
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy
from .models import Post
from .models import Campany,Division,Process,Subprocess,Failuretype,ExpenseItems,Order
from .models import Whmeter,MeterReading,Place
from .forms import PostForm
from .forms import CampanyForm,DivisionForm,ProcessForm,SubprocessForm,OrderForm,FailuretypeForm,ExpenseItemsForm
from .forms import OrderSearchFormSet
from .forms import WhmeterForm,MeterReadingForm,PlaceForm
from .forms import MeterReadingSearchFormSet,ReadingMonthlyFormSet,MeterReadingReaderSearchFormSet
from django.views import generic
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.db.models import Q
from django.http import HttpResponse

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

@login_required
def post_campany_remove(request, pk):
    post = Campany.objects.get(pk=pk)
    post.delete()
    return redirect('post_campany_list')

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

@login_required
def post_division_remove(request, pk):
    post = Division.objects.get(pk=pk)
    post.delete()
    return redirect('post_division_list')

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

@login_required
def post_process_remove(request, pk):
    post = Process.objects.get(pk=pk)
    post.delete()
    return redirect('post_process_list')

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

@login_required
def post_subprocess_remove(request, pk):
    post = Subprocess.objects.get(pk=pk)
    post.delete()
    return redirect('post_subprocess_list')

#工事区分マスタ
@login_required
def post_failuretype_list(request):
    posts = Failuretype.objects.all()
    return render(request, 'blog/post_failuretype_list.html', {'posts':posts})

@login_required
def post_failuretype_detail(request, pk):
    post = get_object_or_404(Failuretype, pk=pk)
    return render(request, 'blog/post_failuretype_detail.html', {'post': post})

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
        form = FailuretypeForm(instance=post)
    return render(request, 'blog/post_failuretype_edit.html', {'form': form})

@login_required
def post_failuretype_remove(request, pk):
    post = Failuretype.objects.get(pk=pk)
    post.delete()
    return redirect('post_failuretype_list')

#費目マスタ
@login_required
def post_expenseItems_list(request):
    posts = ExpenseItems.objects.all()
    return render(request, 'blog/post_expenseItems_list.html', {'posts':posts})

@login_required
def post_expenseItems_detail(request, pk):
    post = get_object_or_404(ExpenseItems, pk=pk)
    return render(request, 'blog/post_expenseItems_detail.html', {'post': post})

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

@login_required
def post_expenseItems_remove(request, pk):
    post = ExpenseItems.objects.get(pk=pk)
    post.delete()
    return redirect('post_expenseItems_list')

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
#電力検針メイン
class MeterReadingSelect(TemplateView):
    template_name = 'blog/MeterReading_select.html'
MeterReadingSelect = MeterReadingSelect.as_view()

#電力検針 管理者メイン
class MeterReadingManage(TemplateView):
    template_name = 'blog/MeterReading_manage.html'
MeterReadingManage = MeterReadingManage.as_view()

#電力量計場所 リスト
def post_Whmeterplace_list(request):
    posts = Place.objects.all()
    return render(request, 'blog/post_Whmeterplace_list.html', {'posts':posts})

#電力量計場所　新規
@login_required
def post_Whmeterplace_new(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_Whmeterplace_list',)
    else:
        form = PlaceForm()
    return render(request, 'blog/post_Whmeterplace_edit.html', {'form': form})

#電力量計場所　詳細
@login_required
def post_Whmeterplace_detail(request, pk):
    post = get_object_or_404(Place, pk=pk)
    return render(request, 'blog/post_Whmeterplace_detail.html', {'post': post})

#電力量計場所　詳細　
@login_required
def post_Whmeterplace_edit(request, pk):
    post = get_object_or_404(Place, pk=pk)
    if request.method == "POST":
        form = PlaceForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_Whmeterplace_detail', pk=post.pk)
    else:
        form = PlaceForm(instance=post)
    return render(request, 'blog/post_Whmeterplace_edit.html', {'form': form})

#電力量計場所　削除
@login_required
def post_Whmeterplace_remove(request, pk):
    post = Place.objects.get(pk=pk)
    post.delete()
    return redirect('post_Whmeterplace_list')

#電力量計 リスト
def post_Whmeter_list(request):
    posts = Whmeter.objects.all()
    return render(request, 'blog/post_Whmeter_list.html', {'posts':posts})

#電力量計　新規
@login_required
def post_Whmeter_new(request):
    if request.method == "POST":
        form = WhmeterForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_Whmeter_list',)
    else:
        form = WhmeterForm()
    return render(request, 'blog/post_Whmeter_edit.html', {'form': form})

#電力量計　詳細
@login_required
def post_Whmeter_detail(request, pk):
    post = get_object_or_404(Whmeter, pk=pk)
    return render(request, 'blog/post_Whmeter_detail.html', {'post': post})

#電力量計　
@login_required
def post_Whmeter_edit(request, pk):
    post = get_object_or_404(Whmeter, pk=pk)
    if request.method == "POST":
        form = WhmeterForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_Whmeter_detail', pk=post.pk)
    else:
        form = WhmeterForm(instance=post)
    return render(request, 'blog/post_Whmeter_edit.html', {'form': form})

#電力量計　削除
@login_required
def post_Whmeter_remove(request, pk):
    post = Whmeter.objects.get(pk=pk)
    post.delete()
    return redirect('post_Whmeter_list')

#
@login_required
def post_meterReading_list(request):
    posts = MeterReading.objects.all()
    return render(request, 'blog/post_meterReading_list.html', {'posts':posts})

#QR読込 テンプレート展開
class QRreader(TemplateView):
    template_name = 'blog/post_qrreader_Whmeter.html'
QR_reader = QRreader.as_view()

#QR読込 値取得
@login_required
def post_Whmeter_qr(request):
    tag = request.POST.get('Whmeter')
    if Whmeter.objects.filter(tag=tag):
        tag_Whmeter = Whmeter.objects.get(tag=tag)
        initial_dict = {
            'Whmeter':tag_Whmeter.id,
            'reader':request.user,
            'Whmeter_name':tag_Whmeter.name,
#            'Whmeter_place':tag_Whmeter.place,
            'Whmeter_unit':tag_Whmeter.unit,
        }
        form = MeterReadingForm(initial=initial_dict)
    else:
        form = MeterReadingForm()

    return render(request, 'blog/post_meterReading_edit.html', {'form': form})


#電力入力
@login_required
def post_meterReading_new(request):
    if request.method == "POST":
        form = MeterReadingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.readed_date = timezone.now()
            post.save()
            return redirect('post_meterReading_list',)
    else:
        form = MeterReadingForm()
    return render(request, 'blog/post_meterReading_edit.html', {'form': form})

#電力入力
@login_required
def post_meterReading_detail(request, pk):
    post = get_object_or_404(MeterReading, pk=pk)
    return render(request, 'blog/post_meterReading_detail.html', {'post': post})

@login_required
def post_meterReading_edit(request, pk):
    post = get_object_or_404(MeterReading, pk=pk)
    if request.method == "POST":
        form = MeterReadingForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.readed_date = timezone.now()
            post.save()
            return redirect('post_meterReading_detail', pk=post.pk)
    else:
        form = MeterReadingForm(instance=post)
    return render(request, 'blog/post_meterReading_edit.html', {'form': form})

@login_required
def post_meterReading_remove(request, pk):
    post = MeterReading.objects.get(pk=pk)
    post.delete()
    return redirect('post_meterReading_list')

@login_required
def post_meterReadingsearch_list(request):
    MeterReadingSearch_list = MeterReading.objects.all()
    formset = MeterReadingSearchFormSet(request.POST or None)
    if request.method == 'POST':
        formset.is_valid()
        queries = []

        for form in formset:
            q_kwargs = {}
            Whmeter_place_search = form.cleaned_data.get('Whmeter_place_search')
            if Whmeter_place_search:
                q_kwargs['Whmeter__place'] = Whmeter_place_search

            count_year_search = form.cleaned_data.get('count_year_search')
            if count_year_search:
                q_kwargs['count_year'] = count_year_search

            count_month_search = form.cleaned_data.get('count_month_search')
            if count_month_search:
                q_kwargs['count_month__contains'] = count_month_search

            if q_kwargs:
                q = Q(**q_kwargs)
                queries.append(q)

        if queries:
            base_query = queries.pop()
            for query in queries:
                base_query |= query
            MeterReadingSearch_list = MeterReadingSearch_list.filter(base_query)

    context = {
        'MeterReadingSearch_list':MeterReadingSearch_list,
        'formset':formset,
    }

    return render(request, 'blog/post_meterReadingsearch_list.html', context)

#一括入力 テンプレート展開
class MeterReading_monthly(TemplateView):
    template_name = 'blog/post_meterReading_monthly.html'
MeterReading_monthly = MeterReading_monthly.as_view()

#電力入力　一括
@login_required
def post_meterReading_monthly(request):
    whmeter = Whmeter.objects.all()
    count_year = request.POST.get('count_year')
    count_month = request.POST.get('count_month')

    posts = []
    for i in whmeter:
        post = MeterReading(Whmeter=i,count_year=count_year,count_month=count_month)
        posts.append(post)
    MeterReading.objects.bulk_create(posts)

    return redirect('post_meterReading_list')

#検針者 テンプレート展開
class MeterReading_Rmonthly(TemplateView):
    template_name = 'blog/post_meterReading_Rmonthly.html'
MeterReading_Rmonthly = MeterReading_Rmonthly.as_view()

#カメラ撮影
class post_meterReading_camera(TemplateView):
    template_name = 'blog/post_meterReading_camera.html'
post_meterReading_camera = post_meterReading_camera.as_view()

#カメラ撮影　tag受取
@login_required
def post_meterReading_camera2(request):
    pk = request.POST.get('wm_tag')
#    post = Whmeter.objects.get(pk=pk)
    if Whmeter.objects.filter(pk=pk):
        post = Whmeter.objects.get(pk=pk)

    else:
        post = Whmeter.objects.get(pk=1)

    return render(request, 'blog/post_meterReading_camera.html', {'post': post})

#検針者　検針年月抽出リスト
@login_required
def post_meterReading_Rlist(request):
    count_year = request.POST.get('count_year')
    count_month = request.POST.get('count_month')
    posts = MeterReading.objects.filter(count_year=count_year,count_month=count_month)

    context = {
        'posts':posts,
        'Rcount_year':count_year,
        'Rcount_month':count_month,
    }

    return render(request, 'blog/post_meterReading_Rlist.html', context)

#検針者　電力入力
@login_required
def post_meterReading_Redit(request, pk):
    post = get_object_or_404(MeterReading, pk=pk)
    initial_dict = {
        'Whmeter':post.Whmeter,
        'reader':request.user,
        'Whmeter_name':post.Whmeter.name,
        'Whmeter_unit':post.Whmeter.unit,
        'Whmeter_place':post.Whmeter.place.name,
    }
    count_year = post.count_year
    count_month = post.count_month
    wh = 0
    wh_last = 0

#20210125 使用電力項目
    if request.method == 'POST':
        form = MeterReadingForm(instance=post,initial=initial_dict)

        integrated_now = float(request.POST.get('integrated_now'))
        if post.count_month ==1:
            post_last = MeterReading.objects.get(Whmeter=post.Whmeter,count_year=post.count_year-1,count_month=12)
            integrated_last = post_last.integrated_Wh
            if integrated_last > integrated_now:
                wh = post.Whmeter.maxvalue-integrated_last + integrated_now
            else:
                wh = integrated_now - integrated_last

            post_twomonthago = MeterReading.objects.get(Whmeter=post.Whmeter,count_year=post.count_year-1,count_month=11)
            integrated_twomonthago = post_twomonthago.integrated_Wh
            if integrated_twomonthago > integrated_last:
                wh_last = post.Whmeter.maxvalue - integrated_twomonthago + integrated_last
            else:
                wh_last = integrated_last - integrated_twomonthago

        elif post.count_month ==2:
            post_last = MeterReading.objects.get(Whmeter=post.Whmeter,count_year=post.count_year,count_month=post.count_month-1)
            integrated_last = post_last.integrated_Wh
            if integrated_last > integrated_now:
                wh = post.Whmeter.maxvalue-integrated_last + integrated_now
            else:
                wh = integrated_now - integrated_last

            post_twomonthago = MeterReading.objects.get(Whmeter=post.Whmeter,count_year=post.count_year-1,count_month=12)
            integrated_twomonthago = post_twomonthago.integrated_Wh
            if integrated_twomonthago > integrated_last:
                wh_last = post.Whmeter.maxvalue - integrated_twomonthago + integrated_last
            else:
                wh_last = integrated_last - integrated_twomonthago

        else:
            post_last = MeterReading.objects.get(Whmeter=post.Whmeter,count_year=count_year,count_month=count_month-1)
            integrated_last = post_last.integrated_Wh
            if integrated_last > integrated_now:
                wh = post.Whmeter.maxvalue - integrated_last + integrated_now
            else:
                wh = integrated_now - integrated_last

            post_twomonthago = MeterReading.objects.get(Whmeter=post.Whmeter,count_year=post.count_year,count_month=post.count_month-2)
            integrated_twomonthago = post_twomonthago.integrated_Wh
            if integrated_twomonthago > integrated_last:
                wh_last = post.Whmeter.maxvalue - integrated_twomonthago + integrated_last
            else:
                wh_last = integrated_last - integrated_twomonthago

#        return render(request,)

    else:
        form = MeterReadingForm(instance=post,initial=initial_dict)

    if wh == 0 or wh_last == 0:
        judgment = 0
    elif wh/wh_last < 0.5 and wh/wh_last > 1.5:
        judgment = 2
    else:
        judgment = 1

    context = {
        'form':form,
        'Rcount_year':count_year,
        'Rcount_month':count_month,
        'pk':pk,
        'wh':wh,
        'wh_last':wh_last,
        'judgment':judgment,
    }

    return render(request, 'blog/post_meterReading_Redit.html', context)

#検針者　QR読込 テンプレート展開
@login_required
def post_qrreader_R(request):
    count_year = request.POST.get('Rcount_year')
    count_month = request.POST.get('Rcount_month')

    context = {
        'Rcount_year':count_year,
        'Rcount_month':count_month,
    }

    return render(request, 'blog/post_qrreader_R.html', context)

#検針者　QR読込 値取得 edit展開
@login_required
def post_Whmeter_qrR(request):
    tag = request.POST.get('Whmeter')
    count_year = request.POST.get('Rcount_year')
    count_month = request.POST.get('Rcount_month')
    whmeter = Whmeter.objects.get(tag=tag)

    if MeterReading.objects.get(Whmeter=whmeter.id,count_year=count_year,count_month=count_month):

        post = MeterReading.objects.get(Whmeter=whmeter.id,count_year=count_year,count_month=count_month)
        pk = post.pk

        initial_dict = {
            'reader':request.user,
            'Whmeter_name':post.Whmeter.name,
            'Whmeter_place':post.Whmeter.place.name,
            'Whmeter_unit':post.Whmeter.unit,
        }

        form = MeterReadingForm(initial=initial_dict,instance=post)

        context = {
            'form':form,
            'Rcount_year':count_year,
            'Rcount_month':count_month,
            'pk':pk
        }

        return render(request, 'blog/post_meterReading_Redit.html', context)


#検針者　QR時　edit保存
@login_required
def post_meterReading_ReditR(request):
    MeterReading_id = request.POST.get('MeterReading_id')
    id = MeterReading_id
    count_year = request.POST.get('count_year')
    count_month = request.POST.get('count_month')

    post = get_object_or_404(MeterReading,pk=id)   #pk=16 ok
#    post = MeterReading.objects.filter(pk=15)     #pk=15 NG

    if request.method == "POST":
        form = MeterReadingForm(request.POST,instance=post)    #instanse=post
        if form.is_valid():
            post = form.save(commit=False)
            post.readed_date = timezone.now()
            post.save()

#            return redirect('post_meterReading_detail',pk=post.pk)
            posts = MeterReading.objects.filter(count_year=count_year,count_month=count_month)

            context = {
                'posts':posts,
                'Rcount_year':count_year,
                'Rcount_month':count_month,
            }

            return render(request, 'blog/post_meterReading_Rlist.html', context)

    else:
        posts = MeterReading.objects.filter(count_year=count_year,count_month=count_month)

        context = {
            'posts':posts,
            'Rcount_year':count_year,
            'Rcount_month':count_month,
            'pk':pk,
        }

        return render(request, 'blog/post_meterReading_Redit.html', context)

#検針者用　抽出リスト
@login_required
def post_meterReadingReadersearch_list(request):
    Scount_year = request.GET.get('Scount_year')
    Scount_month = request.GET.get('Scount_month')
    MeterReadingSearch_Rlist = MeterReading.objects.filter(count_year=Scount_year,count_month=Scount_month)
    formset = MeterReadingReaderSearchFormSet(request.POST or None)
    if request.method == 'POST':
        formset.is_valid()
        queries = []

        for form in formset:
            q_kwargs = {}
            Whmeter_place_search = form.cleaned_data.get('Whmeter_place_search')
            if Whmeter_place_search:
                q_kwargs['Whmeter__place'] = Whmeter_place_search

            if q_kwargs:
                q = Q(**q_kwargs)
                queries.append(q)

        if queries:
            base_query = queries.pop()
            for query in queries:
                base_query |= query
            MeterReadingSearch_Rlist = MeterReadingSearch_Rlist.filter(base_query)

    context = {
        'MeterReadingSearch_Rlist':MeterReadingSearch_Rlist,
        'formset':formset,
        'Scount_year':Scount_year,
        'Scount_month':Scount_month,
    }

    return render(request, 'blog/post_meterReadingsearch_Rlist.html', context)

#検針者 カメラ撮影
@login_required
def post_meterReading_Rcamera2(request):
    pk = request.POST.get('wm_tag')
    Rcount_year = request.POST.get('Rcount_year')
    Rcount_month = request.POST.get('Rcount_month')
    meterReading = MeterReading.objects.get(Whmeter=pk,count_year=Rcount_year,count_month=Rcount_month)
    meterReading_id = meterReading.pk
#    post = Whmeter.objects.get(pk=pk)
    if Whmeter.objects.filter(pk=pk):
        post = Whmeter.objects.get(pk=pk)

    else:
        post = Whmeter.objects.get(pk=1)

    context = {
        'post':post,
        'Rcount_year':Rcount_year,
        'Rcount_month':Rcount_month,
        'pk':meterReading_id,
    }
    return render(request, 'blog/post_meterReading_camera.html', context)

#CSV年月選択テンプレート展開
class meterReading_export(TemplateView):
    template_name = 'blog/post_meterReading_export.html'
meterReading_export = meterReading_export.as_view()

#CSVエクスポート
@login_required
def post_meterReading_export(request):
    count_year = request.POST.get('count_year')
    count_month = request.POST.get('count_month')
    posts = MeterReading.objects.filter(count_year=count_year,count_month=count_month)

    response = HttpResponse(content_type='text/csv; charset=Shift-JIS')
    csvname = str(count_year) + "-" + str(count_month) + ".csv"
    response['Content-Disposition'] = 'attachment; filename={}'.format(csvname)
    writer = csv.writer(response)

    header = [
        '物件コード',  #1
        '物件名称',    #2
        '物件略称',    #3
        '物件かな',    #4
        'グループ',    #5
        'メーターコード',  #6
        'メーター名称',   #7
        'メーター略称',   #8
        'タイプコード',   #9
        'タイプ名称',   #10
        '単位',         #11
        '倍率',         #12
        '全桁数',         #13
        '小数表示桁数',         #14
        '検定期限',         #15
        '判定許容値',         #16
        '比較対象ID',         #17
        '比較対象',         #18
        '警報レベルID',         #19
        '警報レベル',         #20
        '指図メモ',         #21
        '状態ID',         #22
        '状態',         #23
        '検針日',         #24
        '検針日時',      #25
        '積算値',        #26
        '使用量',        #27
        '判定結果ID',        #28
        '判定結果',        #29
        '検針者コード',        #30
        '検針者名',        #31

        ]
    writer.writerow(header)

    for post in posts:
        writer.writerow([
            post.Whmeter.place.code,   #1
            post.Whmeter.place.name,   #2
            post.Whmeter.place.name,   #3
            '',                        #4
            post.Whmeter.place.name,   #5
            post.Whmeter.tag,          #6
            post.Whmeter.name,          #7
            post.Whmeter.name,          #8
            post.type,                  #9
            '電気',                     #10
            post.Whmeter.unit,          #11
            post.Whmeter.magnification,          #12
            post.Whmeter.digits,          #13
            post.Whmeter.decimalPoint,          #14
            '',                          #15
            '',                          #16
            '',                          #17
            '',                          #18
            '',                          #19
            '',                          #20
            '',                          #21
            '',                          #22
            '',                          #23
            '',                          #24
            post.readed_date,             #25
            post.integrated_Wh,           #26
            '',                          #27
            '',                          #28
            '',                          #29
            '',                          #30
            post.reader,                 #31
        ])
    return response







#テスト
#class post_camera_test(TemplateView):
#    template_name = 'blog/post_camera_test2.html'
#camera_test = post_camera_test.as_view()

class post_cameraOCR_test3(TemplateView):
    template_name = 'blog/post_cameraOCR_test3.html'
post_cameraOCR_test3 = post_cameraOCR_test3.as_view()

#@login_required
#def post_camera_test2(request):
#    pk = request.POST.get('wm_tag')
##    post = Whmeter.objects.get(pk=pk)
#    if Whmeter.objects.filter(pk=pk):
#        post = Whmeter.objects.get(pk=pk)

#    else:
#        post = Whmeter.objects.get(pk=1)

#    return render(request, 'blog/post_camera_test2.html', {'post': post})

@login_required
def post_qr_test3(request):
    tag = request.POST.get('Whmeter')
    if Whmeter.objects.filter(tag=tag):
        tag_Whmeter = Whmeter.objects.get(tag=tag)
#        tag_Whmeter_id = tag_Whmeter.id
        initial_dict = {
            'Whmeter':tag_Whmeter.id,
            'reader':request.user,
            'Whmeter_name':tag_Whmeter.name,
            'Whmeter_place':tag_Whmeter.place,
            'Whmeter_unit':tag_Whmeter.unit,
        }
        form = MeterReadingForm(initial=initial_dict)
    else:
        form = MeterReadingForm()

    return render(request, 'blog/post_meterReading_edit.html', {'form': form})

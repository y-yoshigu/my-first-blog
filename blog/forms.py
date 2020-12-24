from django import forms

from .models import Post
from .models import Campany,Division,Process,Subprocess,Order,Failuretype,ExpenseItems

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CampanyForm(forms.ModelForm):

    class Meta:
        model = Campany
        fields = ('name', 'address', 'telephon',)
        labels = {'name':'会社名', 'address':'住　所', 'telephon':'電話番号',}

class DivisionForm(forms.ModelForm):

    class Meta:
        model = Division
        fields = ('name', 'campany',)
        labels = {'name':'部門名', 'campany':'会社名',}

class ProcessForm(forms.ModelForm):

    parent_category2 = forms.ModelChoiceField(
        label = '会　社',
        queryset = Campany.objects,
        required = False
    )

    class Meta:
        model = Process
        fields = ('name', 'tag', 'campany', 'division',)
        labels = {'name':'工程名', 'tag':'Tag', 'division':'部門名',}
        widgets = {'campany':forms.HiddenInput()}

    field_order = ('name', 'tag', 'parent_category2', 'division', )


class SubprocessForm(forms.ModelForm):

    grandparent_category = forms.ModelChoiceField(
        label = '会　社',
        queryset = Campany.objects,
        required = False
    )

    parent_category = forms.ModelChoiceField(
        label = '部　門',
        queryset = Division.objects,
        required = False
    )

    class Meta:
        model = Subprocess
        fields = ('name', 'code', 'codeM', 'campany', 'division', 'process')
        labels = {'name':'設備名', 'code':'コード', 'codeM':'MESCO番号','process':'工程名',}
        widgets = {'campany':forms.HiddenInput(),'division':forms.HiddenInput()}

    field_order = ('name', 'code', 'codeM', 'grandparent_category', 'parent_category','process', )


class FailuretypeForm(forms.ModelForm):

    class Meta:
        model = Failuretype
        fields = ('name',)
        labels = {'name':'工事区分',}

class ExpenseItemsForm(forms.ModelForm):

    class Meta:
        model = ExpenseItems
        fields = ('name',)
        labels = {'name':'費　目',}

class OrderForm(forms.ModelForm):

    campany_category = forms.ModelChoiceField(
        label = '会　社',
        queryset = Campany.objects,
        required = False
    )

    division_category = forms.ModelChoiceField(
        label = '部　門',
        queryset = Division.objects,
        required = False
    )

    process_category = forms.ModelChoiceField(
        label = '工　程',
        queryset = Process.objects,
        required = False
    )

    class Meta:
        model = Order
        fields = (
        'type', 'campany_category', 'division_category', 'process_category', 'subProcess', 'subjectName',
        'chargeName','orderNo','subjectDetail',
        'app_date','requestSection_M','requestSection_E','requestSection_C',
        'wishStart_date','wishEnd_date','failuretype','expenseItems','budget',
        'safePremeasure_removal','safePremeasure_valve','safePremeasure_switsh','safePremeasure_gas',
        'safeContact_start','safeContact_intermediate','safeContact_complete',
        'safeWitness_always','safeWitness_start','leagalConfimation','safeApproval',
        'campany','division','process',
        )
        labels = {
#            'campany':'会　社',
#            'division':'課',
#            'process':'工　程',
            'subjectName':'工事件名',
            'chargeName':'担当者',
            'subProcess':'設備コード',
            'orderNo':'工事受付番号',
            'subjectDetail':'工事内容',
            'app_date':'申し込み',
            'requestSection_M':'機械',
            'requestSection_E':'電計',
            'requestSection_C':'土建',
            'wishStart_date':'希望開始日',
            'wishEnd_date':'希望完了日',
            'failuretype':'工事区分',
            'expenseItems':'費目',
            'budget':'予算金額',
            'safePremeasure_removal':'有害物除去',
            'safePremeasure_valve':'バルブ操作',
            'safePremeasure_switsh':'スイッチ操作',
            'safePremeasure_gas':'ガス濃度',
            'safeContact_start':'着工時',
            'safeContact_intermediate':'中間',
            'safeContact_complete':'完成',
            'safeWitness_always':'常時',
            'safeWitness_start':'着工前',
            'leagalConfimation':'法的確認',
            'safeApproval':'安全環境確認',


        }
        widgets = {'campany':forms.HiddenInput(),'division':forms.HiddenInput(),'process':forms.HiddenInput()}


class OrderSearchForm(forms.Form):

    campany_search = forms.ModelChoiceField(
        label = '会　社',
        queryset = Campany.objects,
        required = False,
    )

    division_search = forms.ModelChoiceField(
        label = '課',
        queryset = Division.objects,
        required = False,
    )

    process_search = forms.ModelChoiceField(
        label = '工程',
        queryset = Process.objects,
        required = False,
    )

    subjectName_search = forms.CharField(
        label = '工事件名',
        max_length = 50,
        required = False,
    )

    app_date_search = forms.DateField(
        label = '申込日(以降)',
        required = False,
    )

    requestSection_M_search = forms.BooleanField(
        label = '依頼先　機械',
        required = False
    )

OrderSearchFormSet = forms.formset_factory(OrderSearchForm,extra=1)

#

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

    class Meta:
        model = Process
        fields = ('name', 'tag', 'campany', 'division',)
        labels = {'name':'工程名', 'tag':'Tag', 'campany':'会社名', 'division':'部門名',}
#テスト
class ProcessForm2(forms.ModelForm):

    parent_category =forms.ModelChoiceField(
        label = '会　社',
        queryset = Campany.objects,
        required = False
    )

    class Meta:
        model = Process
        fields = ('name', 'tag', 'parent_category', 'division',)

#
class SubprocessForm(forms.ModelForm):

    class Meta:
        model = Subprocess
        fields = ('name', 'code', 'codeM', 'campany', 'division', 'process',)
        labels = {'name':'設備コード名', 'code':'コード', 'codeM':'MESCOコード', 'campany':'会社名', 'division':'部門名', 'process':'工程名',}

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

    class Meta:
        model = Order
        fields = (
        'type', 'campany','division','process','subjectName',
        'chargeName','subProcess','orderNo','subjectDetail',
        'app_date','requestSection_M','requestSection_E','requestSection_C',
        'wishStart_date','wishEnd_date','failuretype','expenseItems','budget',
        'safeContact_start','safeContact_intermediate','safeContact_complete',
        'safeWitness_always','safeWitness_start',
        )
        labels = {
            'campany':'会　社',
            'division':'課',
            'process':'工　程',
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
            'safeContact_start':'着工時',

        }

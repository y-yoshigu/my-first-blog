from django import forms

from .models import Post
from .models import Campany,Division,Process,Subprocess,Order,Failuretype,ExpenseItems
from .models import Whmeter,MeterReading,Place

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



#電力量計入力
class WhmeterForm(forms.ModelForm):

    class Meta:
        model = Whmeter
        fields = ('name', 'tag','place','magnification','unit','maxvalue','digits','decimalPoint')
        labels = {'name':'機器', 'tag':'電力量計コード','place':'取付場所','magnification':'倍率','unit':'単位','maxvalue':'最大値','digits':'桁数','decimalPoint':'小数点位置'}

#電力量計場所
class PlaceForm(forms.ModelForm):

    class Meta:
        model = Place
        fields = ('name','code')
        labels = {'name':'取付場所','code':'コード'}


#電力検針
class MeterReadingForm(forms.ModelForm):

    MeterReading_id = forms.IntegerField(
        label = 'ID',
#        max_length = 10,
        required = False,
    )

    Whmeter_name = forms.CharField(
        label = '機器',
        max_length = 30,
        required = False,
    )

    Whmeter_place = forms.CharField(
        label = '取付場所',
        max_length = 50,
        required = False,
    )

    Whmeter_unit = forms.CharField(
        label = '単位',
        max_length = 15,
        required = False,
    )

    Wh_now = forms.FloatField(
        label = '使用電力量（今月）',
        required = False,
    )

    Wh_last = forms.FloatField(
        label = '使用電力量（前月）',
        required = False,
    )

    class Meta:
        model = MeterReading
        fields = ( 'MeterReading_id','Whmeter', 'Whmeter_name','Whmeter_place','Whmeter_unit','integrated_Wh','reader','count_year','count_month','number','Wh_now','Wh_last')
        labels = { 'Whmeter':'電力量計', 'integrated_Wh':'積算値','reader':'検針者','count_year':'積算年','count_month':'積算月'}

#
class MeterReadingSearchForm(forms.Form):

    Whmeter_place_search = forms.ModelChoiceField(
        label = '取付場所 ',
        queryset = Place.objects,
        required = False,
    )

    count_year_search = forms.IntegerField(
        label = '積算年 ',
        required = False,
    )

    count_month_search = forms.IntegerField(
        label = '積算月 ',
        required = False,
    )

MeterReadingSearchFormSet = forms.formset_factory(MeterReadingSearchForm,extra=1)

#検針年月入力
class ReadingMonthlyForm(forms.Form):

    count_year_Rsearch = forms.IntegerField(
        label = '積算年 ',
        required = False,
    )

    count_month_Rsearch = forms.IntegerField(
        label = '積算月 ',
        required = False,
    )

ReadingMonthlyFormSet = forms.formset_factory(ReadingMonthlyForm,extra=1)

#
class MeterReadingReaderSearchForm(forms.Form):

    Whmeter_place_search = forms.ModelChoiceField(
        label = '取付場所 ',
        queryset = Place.objects,
        required = False,
    )

MeterReadingReaderSearchFormSet = forms.formset_factory(MeterReadingReaderSearchForm,extra=1)

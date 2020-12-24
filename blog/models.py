from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Campany(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    telephon = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Division(models.Model):
    name = models.CharField(max_length=200)
    campany = models.ForeignKey(Campany,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Process(models.Model):
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=50)
    division = models.ForeignKey(Division,on_delete=models.CASCADE)
    campany = models.ForeignKey(Campany,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Subprocess(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    codeM = models.CharField(max_length=20)
    campany = models.ForeignKey(Campany,on_delete=models.CASCADE)
    division = models.ForeignKey(Division,on_delete=models.CASCADE)
    process = models.ForeignKey(Process,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Failuretype(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ExpenseItems(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Order(models.Model):
    subjectName = models.CharField(max_length=200,blank=True,null=True)
    type = models.CharField(max_length=100,blank=True,null=True)
    campany = models.ForeignKey(Campany,on_delete=models.CASCADE,default=1,)
    division = models.ForeignKey(Division,on_delete=models.CASCADE,default=1)
    process = models.ForeignKey(Process,on_delete=models.CASCADE,default=1)
    chargeName = models.CharField(max_length=100,blank=True,null=True)
    subProcess = models.ForeignKey(Subprocess,on_delete=models.CASCADE,default=1)
    orderNo = models.CharField(max_length=50,blank=True,null=True)
    subjectDetail = models.TextField(max_length=1000,blank=True,null=True)
    app_date = models.DateField(blank=True,null=True)
    requestSection_M = models.BooleanField(default=False)
    requestSection_E = models.BooleanField(default=False)
    requestSection_C = models.BooleanField(default=False)
    wishStart_date = models.DateField(blank=True, null=True)
    wishEnd_date = models.DateField(blank=True, null=True)
    failuretype = models.ForeignKey(Failuretype,on_delete=models.CASCADE,default=2,)
    expenseItems = models.ForeignKey(ExpenseItems,on_delete=models.CASCADE,default=1,)
    budget = models.IntegerField(blank=True,null=True)
#客先事前措置
    safePremeasure_removal = models.BooleanField(default=False)
    safePremeasure_valve = models.BooleanField(default=False)
    safePremeasure_switsh = models.BooleanField(default=False)
    safePremeasure_gas = models.BooleanField(default=False)
#連絡
    safeContact_start = models.BooleanField(default=False)
    safeContact_intermediate = models.BooleanField(default=False)
    safeContact_complete = models.BooleanField(default=False)
#立会
    safeWitness_always = models.BooleanField(default=False)
    safeWitness_start = models.BooleanField(default=False)
    safeWitness_disassembly = models.BooleanField(default=False)
    safeWitness_intermediate = models.BooleanField(default=False)
    safeWitness_receipt = models.BooleanField(default=False)
    safeWitness_complete = models.BooleanField(default=False)
    safeWitness_test = models.BooleanField(default=False)
#作業環境
    safeEnvironment_hazardous = models.BooleanField(default=False)
    safeEnvironment_heavy = models.BooleanField(default=False)
    safeEnvironment_pit = models.BooleanField(default=False)
    safeEnvironment_dust = models.BooleanField(default=False)
    safeEnvironment_height = models.BooleanField(default=False)
    safeEnvironment_updown = models.BooleanField(default=False)
#
    safeEnvironment_other = models.CharField(max_length=100,blank=True,null=True)
#危険物質
    safeHazardous_ASH3 = models.BooleanField(default=False)
    safeHazardous_SO2 = models.BooleanField(default=False)
    safeHazardous_SO3 = models.BooleanField(default=False)
    safeHazardous_CO2 = models.BooleanField(default=False)
    safeHazardous_CO = models.BooleanField(default=False)
    safeHazardous_H2S = models.BooleanField(default=False)
#
    safeHazardous_other = models.CharField(max_length=100,blank=True,null=True)
#保護具
    safeProtecter_helmet = models.BooleanField(default=False)
    safeProtecter_shoes = models.BooleanField(default=False)
    safeProtecter_fallPrevention = models.BooleanField(default=False)
    safeProtecter_acid = models.BooleanField(default=False)
    safeProtecter_earplug = models.BooleanField(default=False)
    safeProtecter_gloves = models.BooleanField(default=False)
#
    safeProtecter_other = models.CharField(max_length=100,blank=True,null=True)
#着工前措置
    safePretreatment_rope = models.BooleanField(default=False)
    safePretreatment_barricade = models.BooleanField(default=False)
    safePretreatment_light = models.BooleanField(default=False)
    safePretreatment_guard = models.BooleanField(default=False)
#
    safePretreatment_other = models.CharField(max_length=100,blank=True,null=True)
#環境側面
    safeAspect_waste = models.BooleanField(default=False)
    safeAspect_liquid = models.BooleanField(default=False)
    safeAspect_oil = models.BooleanField(default=False)
    safeAspect_remaining = models.BooleanField(default=False)
#
    safeNotices = models.CharField(max_length=200,blank=True,null=True)
    leagalConfimation = models.BooleanField(default=False)
    clientApproval = models.BooleanField(default=False)
    safeApproval = models.BooleanField(default=False)
    mescoReception = models.BooleanField(default=False)
#
    comfirmed = models.BooleanField(default=False)
    comfirmed_M = models.BooleanField(default=False)
    comfirmed_E = models.BooleanField(default=False)
    comfirmed_C = models.BooleanField(default=False)
#
    acceptance = models.BooleanField(default=False)

    def approval_client(self):
        self.clientApproval = True
        self.save()

#    def __str__(self):
#        return self.id


#電力入力
#

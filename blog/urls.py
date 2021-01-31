from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail,name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/list/', views.post_list2, name='post_list2'),
    path('post/Campany/', views.post_campany_list, name='post_campany_list'),
    path('post/Campany/<int:pk>/', views.post_campany_detail,name='post_campany_detail'),
    path('post/Campany/new/', views.post_campany_new, name='post_campany_new'),
    path('post/Campany/<int:pk>/edit', views.post_campany_edit, name='post_campany_edit'),
    path('post/Campany/<pk>/remove/', views.post_campany_remove, name='post_campany_remove'),
    path('post/master/', views.master_select, name='master_select'),
    path('post/Division/', views.post_division_list, name='post_division_list'),
    path('post/Division/<int:pk>/', views.post_division_detail,name='post_division_detail'),
    path('post/Division/new/', views.post_division_new, name='post_division_new'),
    path('post/Division/<int:pk>/edit', views.post_division_edit, name='post_division_edit'),
    path('post/Division/<pk>/remove/', views.post_division_remove, name='post_division_remove'),
    path('post/Process/', views.post_process_list, name='post_process_list'),
    path('post/Process/<int:pk>/', views.post_process_detail,name='post_process_detail'),
    path('post/Process/new/', views.post_process_new.as_view(), name='post_process_new'),
    path('post/Process/<int:pk>/edit', views.post_process_edit, name='post_process_edit'),
    path('post/Process/<pk>/remove/', views.post_process_remove, name='post_process_remove'),
    path('post/Subprocess/', views.post_subprocess_list, name='post_subprocess_list'),
    path('post/Subprocess/<int:pk>/', views.post_subprocess_detail,name='post_subprocess_detail'),
    path('post/Subprocess/new/', views.post_subprocess_new.as_view(), name='post_subprocess_new'),
    path('post/Subprocess/<int:pk>/edit', views.post_subprocess_edit, name='post_subprocess_edit'),
    path('post/Subprocess/<pk>/remove/', views.post_subprocess_remove, name='post_subprocess_remove'),
    path('post/Failuretype/', views.post_failuretype_list, name='post_failuretype_list'),
    path('post/Failuretype/<int:pk>/', views.post_failuretype_detail,name='post_failuretype_detail'),
    path('post/Failuretype/new/', views.post_failuretype_new, name='post_failuretype_new'),
    path('post/Failuretype/<int:pk>/edit', views.post_failuretype_edit, name='post_failuretype_edit'),
    path('post/Failuretype/<pk>/remove/', views.post_failuretype_remove, name='post_failuretype_remove'),
    path('post/ExpenseItems/', views.post_expenseItems_list, name='post_expenseItems_list'),
    path('post/ExpenseItems/<int:pk>/', views.post_expenseItems_detail,name='post_expenseItems_detail'),
    path('post/ExpenseItems/new/', views.post_expenseItems_new, name='post_expenseItems_new'),
    path('post/ExpenseItems/<int:pk>/edit', views.post_expenseItems_edit, name='post_expenseItems_edit'),
    path('post/ExpenseItems/<pk>/remove/', views.post_expenseItems_remove, name='post_expenseItems_remove'),
    path('post/Order/', views.post_order_list, name='post_order_list'),
    path('post/Order/<int:pk>/', views.post_order_detail,name='post_order_detail'),
    path('post/Order/new/', views.post_order_new.as_view(), name='post_order_new'),
    path('post/Order/<int:pk>/edit', views.post_order_edit, name='post_order_edit'),
    path('post/Order/<pk>/remove/', views.post_order_remove, name='post_order_remove'),
    path('post/Order/allremove/', views.post_order_allremove, name='post_order_allremove'),
#
    path('api/division/get/', views.ajax_get_division, name='ajax_get_division'),
    path('api/process/get/', views.ajax_get_process, name='ajax_get_process'),

    path('api/divisionCategory/get/', views.ajax_get_divisionCategory, name='ajax_get_divisionCategory'),
    path('api/processCategory/get/', views.ajax_get_processCategory, name='ajax_get_processCategory'),
    path('api/subprocessCategory/get/', views.ajax_get_subprocessCategory, name='ajax_get_subprocessCategory'),

    path('post/Ordersearch/', views.post_ordersearch_list, name='post_ordersearch_list'),
    path('post/Order/<int:pk>/clientapproval', views.post_clientApproval, name='post_clientApproval'),

#電力
    path('post/MeterReading/', views.MeterReadingSelect, name='MeterReadingSelect'),
    path('post/MeterReading/Manage/', views.MeterReadingManage, name='MeterReadingManage'),
    path('post/Whmeter/list/', views.post_Whmeter_list, name='post_Whmeter_list'),
    path('post/Whmeter/new/', views.post_Whmeter_new, name='post_Whmeter_new'),
    path('post/Whmeter/<int:pk>/', views.post_Whmeter_detail,name='post_Whmeter_detail'),
    path('post/Whmeter/<int:pk>/edit', views.post_Whmeter_edit, name='post_Whmeter_edit'),
    path('post/Whmeter/<pk>/remove/', views.post_Whmeter_remove, name='post_Whmeter_remove'),
    path('post/Whmeterplace/list/', views.post_Whmeterplace_list, name='post_Whmeterplace_list'),
    path('post/Whmeterplace/new/', views.post_Whmeterplace_new, name='post_Whmeterplace_new'),
    path('post/Whmeterplace/<int:pk>/', views.post_Whmeterplace_detail,name='post_Whmeterplace_detail'),
    path('post/Whmeterplace/<int:pk>/edit', views.post_Whmeterplace_edit, name='post_Whmeterplace_edit'),
    path('post/Whmeterplace/<pk>/remove/', views.post_Whmeterplace_remove, name='post_Whmeterplace_remove'),
    path('post/MeterReading/list/', views.post_meterReading_list, name='post_meterReading_list'),
    path('post/MeterReading/new/', views.post_meterReading_new, name='post_meterReading_new'),
    path('post/MeterReading/<int:pk>/', views.post_meterReading_detail,name='post_meterReading_detail'),
    path('post/MeterReading/<int:pk>/edit', views.post_meterReading_edit, name='post_meterReading_edit'),
    path('post/MeterReading/<pk>/remove/', views.post_meterReading_remove, name='post_meterReading_remove'),
    path('post/MeterReadingsearch/', views.post_meterReadingsearch_list, name='post_meterReadingsearch_list'),
    path('post/MeterReading/monthly/add/', views.post_meterReading_monthly, name='post_meterReading_monthly'),
    path('post/MeterReading/monthly/', views.MeterReading_monthly, name='MeterReading_monthly'),
    path('post/MeterReading/camera/', views.post_meterReading_camera, name='post_meterReading_camera'),
    path('post/MeterReading/export/', views.meterReading_export, name='meterReading_export'),
    path('post/MeterReading/csv/', views.post_meterReading_export, name='post_meterReading_export'),

#検針者用
    path('post/MeterReading/Rmonthly/', views.MeterReading_Rmonthly, name='MeterReading_Rmonthly'),
    path('post/MeterReading/Rlist/', views.post_meterReading_Rlist, name='post_meterReading_Rlist'),
    path('post/MeterReading/<int:pk>/Redit/', views.post_meterReading_Redit, name='post_meterReading_Redit'),
    path('post/QRreader/R/', views.post_qrreader_R, name='post_qrreader_R'),
    path('post/Whmeter/QRR/', views.post_Whmeter_qrR, name='post_Whmeter_qrR'),
    path('post/MeterReading/ReditR/', views.post_meterReading_ReditR, name='post_meterReading_ReditR'),
    path('post/MeterReadingReadersearch/', views.post_meterReadingReadersearch_list, name='post_meterReadingReadersearch_list'),
    path('post/MeterReading/camera2/', views.post_meterReading_camera2, name='post_meterReading_camera2'),
    path('post/MeterReading/Rcamera2/', views.post_meterReading_Rcamera2, name='post_meterReading_Rcamera2'),

    path('post/QRreader/', views.QR_reader, name='QR_reader'),
    path('post/Whmeter/QR', views.post_Whmeter_qr, name='post_Whmeter_qr'),
#    path('post/camera/test', views.camera_test, name='camera_test'),
#    path('post/camera/test2', views.post_camera_test2, name='post_camera_test2'),
    path('post/cameraOCR/test3', views.post_cameraOCR_test3, name='post_cameraOCR_test3'),

#    path('post/QRtest2/', views.post_qr_test2, name='post_qr_test2'),


]

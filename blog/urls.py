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
    path('post/master/', views.master_select, name='master_select'),
    path('post/Division/', views.post_division_list, name='post_division_list'),
    path('post/Division/<int:pk>/', views.post_division_detail,name='post_division_detail'),
    path('post/Division/new/', views.post_division_new, name='post_division_new'),
    path('post/Division/<int:pk>/edit', views.post_division_edit, name='post_division_edit'),
    path('post/Process/', views.post_process_list, name='post_process_list'),
    path('post/Process/<int:pk>/', views.post_process_detail,name='post_process_detail'),
    path('post/Process/new/', views.post_process_new.as_view(), name='post_process_new'),
    path('post/Process/<int:pk>/edit', views.post_process_edit, name='post_process_edit'),
    path('post/Subprocess/', views.post_subprocess_list, name='post_subprocess_list'),
    path('post/Subprocess/<int:pk>/', views.post_subprocess_detail,name='post_subprocess_detail'),
    path('post/Subprocess/new/', views.post_subprocess_new.as_view(), name='post_subprocess_new'),
    path('post/Subprocess/<int:pk>/edit', views.post_subprocess_edit, name='post_subprocess_edit'),
    path('post/Failuretype/', views.post_failuretype_list, name='post_failuretype_list'),
    path('post/Failuretype/new/', views.post_failuretype_new, name='post_failuretype_new'),
    path('post/Failuretype/<int:pk>/edit', views.post_failuretype_edit, name='post_failuretype_edit'),
    path('post/ExpenseItems/', views.post_expenseItems_list, name='post_expenseItems_list'),
    path('post/ExpenseItems/new/', views.post_expenseItems_new, name='post_expenseItems_new'),
    path('post/ExpenseItems/<int:pk>/edit', views.post_expenseItems_edit, name='post_expenseItems_edit'),
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

    path('post/QRreader/', views.QR_reader, name='QR_reader'),


]

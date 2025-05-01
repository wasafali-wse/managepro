from django.urls import path

from . import views 


urlpatterns = [
    path('dashboard/', views.dashboard,name='dashboard'),
    path('pos/invoice/', views.pos_invoice,name='pos_invoice'),
    # path('pos/invoice/<int:id>',views.pos_invoice,name='pos_invoice'),
    path('pos/extra-income/', views.extra_income,name='extra_income'),
    path('pos/quotation/', views.quotation,name='quotation'),
    # path('pos/quotation/<int:id>',views.quotation,name=''),
    path('pos/customer/', views.customer,name='customer'),
    path('pos/customer/<int:id>',views.customer_detail,name='customer-detail'),
    path('pos/suppliers/', views.supplier,name='supplier'),
    path('pos/receipt/', views.reciept,name='reciept'),
    path('pos/inventory/', views.inventory,name='inventory'),
    path('pos/expenses/', views.expense,name='expense'),
    path('chat/inbox/', views.inbox,name='inbox'),
    path('chat/sent/', views.sent,name='sent'),
    path('todo/', views.todo,name='todo'),
    path('file-manager/', views.file_manager,name='file_manager'),
]
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'erp/dashboard.html')


@login_required
def pos_invoice(request):
    return render(request, 'erp/pos_invoice.html')
    
@login_required
def extra_income(request):
    return render(request, 'erp/extra_income.html')

@login_required
def quotation(request):
    return render(request, 'erp/quotation.html')

@login_required
def customer(request):
    return render(request, 'erp/customer.html')
@login_required
def customer_detail(request, id):
    data = {
        'id': id,
        'name': 'John Doe',
        'phone':'03332278859',
        'phone2':'03138163302',
        'address':'123 Main St, City, Country',
    }
    return render(request, 'erp/customer_detail.html' , data)


@login_required
def supplier(request):
    return render(request, 'erp/supplier.html')

@login_required
def reciept(request):
    return render(request, 'erp/reciept.html')

@login_required
def inventory(request):
    return render(request, 'erp/inventory.html')

@login_required
def expense(request):
    return render(request, 'erp/expense.html')

@login_required
def inbox(request):
    return render(request, 'erp/inbox.html')

@login_required
def sent(request):
    return render(request, 'erp/sent.html')

@login_required
def todo(request):
    return render(request, 'erp/todo.html')

@login_required
def file_manager(request):
    return render(request, 'erp/file-manager.html')

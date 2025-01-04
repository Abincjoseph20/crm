from django.shortcuts import render, redirect,get_object_or_404
from .models import Customer, BANK_CHOICE, PRODUCT_CHOICE, STATUS_CHOICES, TYPE_CHOICES
from django.views import View

def create_customer(request):
    if request.method == 'POST':
        # Get form data
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        phone_num = request.POST.get('phone_num')
        product = request.POST.get('product')
        bank = request.POST.get('bank')
        status = request.POST.get('status')
        type = request.POST.get('type')
        dsa_name = request.POST.get('dsa_name')
        dsa_number = request.POST.get('dsa_number')
        dsa_connector_code = request.POST.get('dsa_connector_code')

        # Create and save a new Customer instance
        customer = Customer(
            f_name=f_name,
            l_name=l_name,
            phone_num=phone_num,
            product=product,
            bank=bank,
            status=status,
            type=type,
            dsa_name=dsa_name if type == 'DSA' else '',
            dsa_number=dsa_number if type == 'DSA' else '',
            dsa_connector_code=dsa_connector_code if type == 'DSA' else ''
        )
        customer.save()

        return redirect('list')

    context = {
        'bank_choices': BANK_CHOICE,
        'product_choices': PRODUCT_CHOICE,
        'status_choices': STATUS_CHOICES
    }
    return render(request, 'create.html', context)



def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'list.html', {'customers': customers})



def details(request,pk):
    fom = get_object_or_404(Customer,pk=pk)
    return render(request,'details.html',{'fom':fom})

def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.f_name = request.POST.get('f_name')
        customer.l_name = request.POST.get('l_name')
        customer.phone_num = request.POST.get('phone_num')
        customer.product = request.POST.get('product')
        customer.bank = request.POST.get('bank')
        customer.status = request.POST.get('status')
        customer.type = request.POST.get('type')
        customer.dsa_name = request.POST.get('dsa_name')
        customer.dsa_number = request.POST.get('dsa_number')
        customer.dsa_connector_code = request.POST.get('dsa_connector_code')
        customer.save()
        return redirect('list')

    context = {
        'customer': customer,
        'bank_choices': BANK_CHOICE,
        'product_choices': PRODUCT_CHOICE,
        'status_choices': STATUS_CHOICES,
        'type_choices': TYPE_CHOICES,
    }
    return render(request, 'edit.html', context)


def delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('list')
    return render(request, 'delete.html', {'customer': customer})


class Category(View):
    def get(self, request, val):
        customers = Customer.objects.filter(product=val)  
        titles = customers.values('f_name', 'l_name')  
        return render(request, 'category.html', {'customers': customers, 'titles': titles})


class CategoryTitle(View):
    def get(self, request, val):
        customers = Customer.objects.filter(f_name=val)
        if customers:
            titles = Customer.objects.filter(product=customers[0].product).values('f_name', 'l_name')
        else:
            titles = None
        return render(request, 'category.html', {'customers': customers, 'titles': titles})
    

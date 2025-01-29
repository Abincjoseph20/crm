from django.shortcuts import render, redirect,get_object_or_404,HttpResponse
from .models import Customer,DSA, BANK_CHOICE, PRODUCT_CHOICE, STATUS_CHOICES, TYPE_CHOICES
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
        dsa_id = request.POST.get('dsa')  # Get selected DSA ID
        
        if type == 'DSA' and dsa_id:
            dsa = DSA.objects.get(id=dsa_id)  # Get the DSA if it exists
        else:
            dsa = None 

        # Create and save a new Customer instance
        customer = Customer.objects.create(
            f_name=f_name,
            l_name=l_name,
            phone_num=phone_num,
            product=product,
            bank=bank,
            status=status,
            type=type,
            dsa=dsa
        )
        customer.save()

        return redirect('list')
    
    dsa_list = DSA.objects.all()
    context = {
        'bank_choices': BANK_CHOICE,
        'product_choices': PRODUCT_CHOICE,
        'status_choices': STATUS_CHOICES,
        'dsa_list': dsa_list
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


class Bank_Category(View):
    def get(self, request, val):
        customers = Customer.objects.filter(bank=val)  
        titles = customers.values('f_name', 'l_name')  
        return render(request, 'Bank_category.html', {'customers': customers, 'titles': titles})
    
    
class Pdoduct_Catogory(View):
    def get(self,request,val):
        product = Customer.objects.filter(product=val)
        titles = product.values('f_name','l_name')
        return render(request,'Product_catogory.html',{'product': product, 'titles': titles})

    
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            customers = Customer.objects.order_by('-created_date').filter(f_name__icontains=keyword)
        else:
            return redirect('list')
    context = {
        'customers': customers,
    }
    return render(request,'list.html',context)



def dsa(request):
    context = {}
    if request.method == 'POST':
        dsa_name = request.POST.get('dsa_name')
        dsa_code = request.POST.get('dsa_code')
        dsa_phone_number = request.POST.get('dsa_phone_number')
        
        DSA.objects.create(
            dsa_name=dsa_name,
            dsa_code=dsa_code,
            dsa_phone_number=dsa_phone_number,
        )
        return redirect('dsa_list')
    
    return render(request,'dsa_create.html',context)


def dsa_lis(request):
    dsa = DSA.objects.all()
    return render(request,'dsa_list.html',{'dsa':dsa})
        
from django.shortcuts import render, redirect,get_object_or_404,HttpResponse
from .models import Customer,DSA,Task, BANK_CHOICE, PRODUCT_CHOICE, STATUS_CHOICES, TYPE_CHOICES
from django.views import View
from django.utils import timezone
from django.http import Http404
from datetime import datetime,timedelta
from datetime import timedelta



from django.utils import timezone
from datetime import datetime, timedelta
from django.http import Http404
from .models import Task

def Home(request):
    return render(request,'home1.html')

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
    
    
class status_filter(View):
    def get(self,request,status):
        customers =Customer.objects.filter(status=status)
        return render(request,'status_filter.html',{'customers':customers,'status':status})

    
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


# Direct Selling Agent(DSA)
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




def Create_Task(request):
    if request.method == 'POST':
        try:
            # Get raw input
            title = request.POST.get('title')
            task_date_str = request.POST.get('task_date')
            task_time_str = request.POST.get('task_time')
            
            # Parse and localize
            naive_datetime = datetime.strptime(
                f"{task_date_str} {task_time_str}", 
                '%Y-%m-%d %H:%M'
            )
            localized_datetime = timezone.make_aware(
                naive_datetime,
                timezone.get_current_timezone()
            )
            
            Task.objects.create(
                title=title,
                descriptions=request.POST.get('descriptions'),
                task_date=localized_datetime.date(),
                task_time=localized_datetime.time(),
            )
            return redirect('task_list')
        except Exception as e:
            return render(request, 'error_page.html', {'error': str(e)})
    return render(request, 'task_create.html')
        

def task_list(request):
    tasks = Task.objects.all().order_by('task_date', 'task_time')
    
    task_dict = {}
    
    for task in tasks:    
        if task.task_date not in task_dict:
            task_dict[task.task_date] = []
        task_dict[task.task_date].append(task)
        
    context = {
        'task_dict': task_dict,
    }

    return render(request, 'task_list.html', context)


def edit_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        if request.method == 'POST':
            task.title = request.POST.get('title')
            task.descriptions = request.POST.get('descriptions')
            task.task_date = request.POST.get('task_date')
            task.task_time = request.POST.get('task_time')
            task.save()
            return redirect('task_list')
        return render(request, 'task_edit.html', {'task': task})
    except Task.DoesNotExist:
        raise Http404("Task not found")
    except Exception as e:
        return render(request, 'error_page.html', {'error': str(e)})


def delete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
    except Task.DoesNotExist:
        raise Http404("Task not found")
    return redirect('task_list')


def upcoming_notifications(request):
    now = timezone.localtime(timezone.now())
    window_end = now + timedelta(minutes=5)
    
    # Debug prints
    print(f"\nCurrent local time: {now}")
    print(f"Notification window: {now.time()} to {window_end.time()}")
    
    upcoming_tasks = Task.objects.filter(
        task_date=now.date(),
        task_time__range=(now.time(), window_end.time())
    ).order_by('task_time')
    
    print(f"Found tasks: {list(upcoming_tasks)}")
    
    return render(request, 'upcoming_notifications.html', {
        'upcoming_notifications': upcoming_tasks,
        'current_time': now,
    })
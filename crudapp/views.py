from django.shortcuts import render, redirect
from django.urls import reverse
from crudapp.forms import EmployeeForm
from crudapp.models import Employee
from django.contrib import messages
from django.core.paginator import Paginator


def show(request):
    edata = Employee.objects.all().order_by('eid')
    if edata.exists():
        paginator = Paginator(object_list=edata, per_page= 3,orphans=1)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request,'index.html',{"page_obj": page_obj})
    page_obj = None
    return render(request,'index.html',{'page_obj': page_obj})

def emp(request):
    if request.method == "POST":
        fm = EmployeeForm(request.POST,request.FILES)
        print(fm)
        if fm.is_valid():
            fm.save()
            messages.success(request=request,message="Data Added Successfully")
            return redirect(reverse("show"))
    else:
        fm = EmployeeForm()
    if request.POST:
        fm = EmployeeForm(request.POST,request.FILES)
    return render(request,'emp.html',{'fm': fm})

def edit(request,eid):
    einstance = Employee.objects.get(pk=eid)
    if request.method == "POST":
        fm = EmployeeForm(request.POST,request.FILES, instance=einstance)
        if fm.is_valid():
            fm.save()
            messages.success(request=request,message="Data has been successfully updated")
            return redirect(reverse('show'))
    else:
        fm = EmployeeForm(instance=einstance)
    return render(request,'edit.html',{'fm': fm})

def destroy(request, eid):
    if request.method == "GET":
        try:
            obj = Employee.objects.get(eid=eid)
            obj.delete()
            messages.success(request, 'Data has been successfully deleted.')
        except Employee.DoesNotExist:
            messages.error(request, 'The specified data does not exist.')
        except Exception as e:
            messages.error(request, f'Something went wrong. Please try again. Error: {e}')

    return redirect(reverse('show'))




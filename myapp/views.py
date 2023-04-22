from django.shortcuts import render,redirect
from .models import Student
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def index(request):
    if request.method=='GET':
        return render(request,'index.html')
    else:
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password'],
            mobile=request.POST['mobile'],
        )
        return redirect('show')
    

def show(request):
    sss=Student.objects.all()
    free={
        'sss':sss
    }
    return render(request,'in.html',free)


def page(request):
    object_list = Student.objects.all()
    page_num = request.GET.get('page', 1)

    paginator = Paginator(object_list, 2) # 6 employees per page


    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'page.html', {'page_obj': page_obj})


def delete(request,pk):
    # Student.objects.filter(id=pk).delete()
    Student.objects.get(id=pk).delete()
    return redirect('show')


def edit(request,pk):
    ss=Student.objects.get(id=pk)
    if request.method=='POST':
        ss.name=request.POST['name']
        ss.email=request.POST['email']
        ss.password=request.POST['password']
        ss.mobile=request.POST['mobile']

        ss.save()
        return redirect('show')
    
    return render(request,'edit.html',{'pob':ss})


def log_page(request):
    if request.method=='POST':
        user=request.POST.get('username')
        upass=request.POST.get('password')
        print(user,upass)
        
        return render(request,'edit.html')
from django.shortcuts import render
from django.http import HttpResponse
from .forms import WriterForm,ViewLogForm,ViewRegForm
from .models import WriterData,ViewerReg,ViewerLog

def view(request):
    if request.method=="POST":
        wform=WriterForm(request.POST)
        if wform.is_valid():
            title=request.POST.get('Title')
            content=request.POST.get('Content')
            image= request.POST.get('Image')
            data= WriterData(
                Title=title,
                Content=content,
                Image=image
            )
            data.save()
            wform=WriterForm()
            return render (request,'projectapp/w.html',{'wform':wform})

        return HttpResponse ("please provide valid data")
    wform=WriterForm()
    return render (request,'projectapp/w.html',{'wform':wform})
def user_reg_view(request):
    if request.method=="POST":
       vrform=ViewRegForm(request.POST)
       if vrform.is_valid():
           f_name=request.POST.get('f_name')
           l_name=request.POST.get('l_name')
           username=request.POST.get('username')
           password=request.POST.get('password')
           data=ViewerReg(
               f_name==f_name,
               l_name=l_name,
               username=username,
               password=password
           )
           data.save()
           vlform=ViewLogForm()
           context={'vlform':vlform}
           return render (request,'projectapp/log.html',context)
       return HttpResponse("please enter valid details")
    vrform=ViewRegForm
    context={'vrform':vrform}
    return render (request,'projectapp/reg.html',context)
def user_log_view(request):
    if request.method=="POST":
        vlform=ViewLogForm(request.POST)
        if vlform.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=ViewerReg.objects.filter(username=username)
            pwd=ViewerReg.objects.filter(password=password)

            if user and pwd:
                data=WriterData.objects.all()
                context={'data':data}
                return render(request,'projectapp/list_data.html',context)
            return  HttpResponse("Invalid Ctredentials")
        vlform=ViewLogForm()
        context={'vlform':vlform}
        return render (request,'projectapp/log.html',context)
    vlform=ViewLogForm()
    context={'vlform':vlform}
    return render (request,'projectapp/log.html',context)














from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .forms import RegisterForm
from robonish.models import Register,Robot

def index_view(request):
    form = RegisterForm()
    return render(request,'index.html', dict(form=form))

def register_view(request): #veritabanına girilen verileri kaydetme
    form = RegisterForm()
    if request.POST:
        form = RegisterForm(request.POST or None,request.FILES or None)

        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())

    context ={
        "form": form,
        #"robots":robots,
    }
    return render(request,'index.html',context)

def register_view_id(request,id): #veritabanına girilen verileri kaydetme
    context ={
    }
    return render(request,'index.html',context)
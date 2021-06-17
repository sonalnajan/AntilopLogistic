from django.shortcuts import render
from antilopapp.forms import PickupForm,QueryForm
from antilopapp.models import pickup,Query

# Create your views here.
def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")  

def service(request):
    return render(request,"service.html")  



def queryform(request):
    query=Query.objects.all()
    if request.method == "POST":
        form = QueryForm(request.POST,instance=query)
        if form.is_valid():
            form.save()
               
    return render(request,"queryform.html")  

def query(request):
    query=Query.objects.all()

    context={
        'query':query
    }

    return render(request,"query.html",context)

def pickupview(request):
    form=PickupForm()
    if request.method == "POST":
        form = PickupForm(request.POST)
        if form.is_valid():

            form.save()
    context= {


    }     
    return render(request,"pickup.html",context)

def pickupform(request):
    form=pickup.objects.all()
    
    context={
        'form':form
    }
    
    return render(request,"pickupform.html",context)    
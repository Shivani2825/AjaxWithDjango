from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Person

def getdata(request):
    data = list(Person.objects.values('fname', 'lname','id'))
    return JsonResponse(data, safe=False)

def home(request):
    data=Person.objects.all()
    return render(request, 'index.html')

def deletedata(request):
    id=request.GET.get('id')
    person=Person.objects.get(id=id)
    person.delete()
    return redirect('home')

def savedata(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        data = Person(fname=fname,lname=lname)
        data.save()
        return HttpResponse(f"User {fname} is successfully created")

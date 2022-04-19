from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import entry

def home(request):
    return render(request, 'home.html')

def show(request):
    data = entry.objects.all()
    return render(request, 'show.html',{'data':data})

def edit(request):
    ID = request.GET['id']
    for data in entry.objects.filter(ID=ID):
        data1 = data.data1
        data2 = data.data2
    return render(request, 'edit.html',{'ID':ID,'data1':data1,'data2':data2})

def RecordEdited(request):
    if request.method == 'POST':
        ID = request.POST['id']
        data1 = request.POST['data1']
        data2 = request.POST['data2']

        entry(ID = ID, data1 = data1, data2 = data2).save()
        msg = "Data update succesfully"
        return render(request, 'show.html',{'msg':msg})

    else:
        return HttpResponse(" <h1>404 Error </h1>")
    return render(request, 'edit.html',{'ID':ID,'data1':data1,'data2':data2})

def delete(request):
    ID = request.GET['id']
    entry.objects.filter(ID=ID).delete()

    return HttpResponseRedirect('show')

def send(request):
    if request.method == 'POST':
        ID = request.POST['id']
        data1 = request.POST['data1']
        data2 = request.POST['data2']

        entry(ID = ID, data1 = data1, data2 = data2).save()
        msg = "Data save succesfully"
        return render(request, 'home.html',{'msg':msg})

    else:
        return HttpResponse(" <h1>404 Error </h1>")


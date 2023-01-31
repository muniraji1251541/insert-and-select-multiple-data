from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST.get('topic')
        t=Topic.objects.get_or_create(topic_name=tn)[0]
        t.save()
        return HttpResponse('Data inserted successfully')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    qst=Topic.objects.all()
    d={'topics':qst}
    if request.method=='POST':
        tn=request.POST.get('topic')
        name=request.POST.get('na')
        url=request.POST.get('ur')
        t=Topic.objects.get_or_create(topic_name=tn)[0]
        t.save()
        w=Webpage.objects.get_or_create(topic_name=t,name=name,url=url)[0]
        w.save()
        return HttpResponse('Data inserted successfully')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    qsw=Webpage.objects.all()
    d1={'names':qsw}
    if request.method=='POST':
        name=request.POST.get('na')
        date=request.POST.get('da')
        w=Webpage.objects.get_or_create(name=name)[0]
        w.save()
        a=Accessrecord.objects.get_or_create(name=w,date=date)[0]
        a.save()
        return HttpResponse('Data inserted successfully')
    return render(request,'insert_access.html',d1)

def select_multiple(request):
    qst=Topic.objects.all()
    d={'topics':qst}
    if request.method=='POST':
        tn=request.POST.getlist('topic')
        qsw=Webpage.objects.none()
        for i in tn:
            qsw=qsw|Webpage.objects.filter(topic_name=i)
        d1={'names':qsw}
        return render(request,'display_webpage.html',d1)
    return render(request,'select_multiple.html',d)

def checkbox(request):
    qst=Topic.objects.all()
    d={'topics':qst}
    if request.method=='POST':
        tn=request.POST.getlist('topic')
        qsw=Webpage.objects.none()
        for i in tn:
            qsw=qsw|Webpage.objects.filter(topic_name=i)
        d1={'names':qsw}
        return render(request,'display_webpage.html',d1)
    return render(request,'checkbox.html',d)

def radio(request):
    qst=Topic.objects.all()
    d={'topics':qst}
    return render(request,'radio.html',d)
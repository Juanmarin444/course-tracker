from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import pytz
from django.utils import timezone
import tzlocal

def index(request):
    courses = Course.objects.all()
    newTimes = []
    for i in courses:
        newTime = convert_to_localtime(i.created_at);
        newTimes.append(newTime)

    myLists = zip(courses, newTimes)
    context = {'courses': courses, 'newTimes': newTimes}
    context2 = {"myLists": myLists}
    return render(request, 'add_courses/index.html', context2)

def convert_to_localtime(utctime):
    fmt = '%h %d, %Y @ %I:%M %p'
    ltz = tzlocal.get_localzone()
    localtz = utctime.replace(tzinfo=pytz.utc).astimezone(ltz)
    return localtz.strftime(fmt)

def add_course(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        Course.objects.create(name = request.POST['c_name'], desc = request.POST['desc'])
    return redirect('/')

def remove(request, id):
    course = Course.objects.get(id=id)
    context = {"course": course}
    return render(request, 'add_courses/delete.html', context)

def destroy(request, id):
    course = Course.objects.get(id=id)
    course.delete()

    return redirect('/')

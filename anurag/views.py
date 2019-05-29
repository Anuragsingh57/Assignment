from django.shortcuts import render
import requests
# Create your views here.
from anurag.models import Assignment
import json

def index(request):
    return render(request, 'index.html')


def task1(request, id=1):
    url = 'https://jsonplaceholder.typicode.com/posts/'
    url_request = requests.get(url)
    file = url_request.json()

    return render(request, 'page1.html', {'file':file}, {'id':id})


def task1_1(request, id=2):
    url = 'https://jsonplaceholder.typicode.com/posts/'
    url_request = requests.get(url)
    file = url_request.json()

    return render(request, 'page2.html', {'file':file})



def task2(request):
    url = 'https://jsonplaceholder.typicode.com/users'
    url_request = requests.get(url)
    file = url_request.json()


    return  render(request, 'task2.html', {'file': file})


def task3(request):
    url = 'https://jsonplaceholder.typicode.com/users'
    url_request = requests.get(url)
    file = url_request.json()

    if request.method == 'POST':
        email = request.POST.get('select')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        value = Assignment(select=email, subject=subject, message=message)
        value.save()

        return render(request, 'task3.html', {'file': file})
    else:
        return render(request, 'task3.html', {'file': file})






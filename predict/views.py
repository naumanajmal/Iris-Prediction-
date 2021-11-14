from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import urls
from .models import *
from .forms import *
def predict(request):
    data = Post.objects.all()
    form  = PostForm()
    context = { 'data': data, 'form':form}
    return render(request, 'predict.html', context)
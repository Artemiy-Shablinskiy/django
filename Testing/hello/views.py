from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Cont_form
from .models import Contestant
def welcome(request):
    return render(request, r'hello/welcome.html')
def input_data(request):
    if request.method == "POST":
        form = Cont_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("graphs")
    else:
        form = Cont_form()
    return render(request, r'hello/input_data.html',{"form":form})
def graphs(request):
    return HttpResponse("Graphs")
# Create your views here.

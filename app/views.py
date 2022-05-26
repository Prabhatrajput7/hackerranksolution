from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from .forms import Todoapp
from .models import Todo
# Create your views here.

class Pageone(FormView):
    form_class = Todoapp
    template_name = "app/main.html"
    success_url ="/"

    def form_valid(self, form):
        form.save()
        return super(Pageone,self).form_valid(form)

class Pagetwo(ListView):
    template_name = 'app/all.html'
    model = Todo
    context_object_name = 'todo'  

def complete(request,id):
    t = Todo.objects.get(pk=id)
    t.completed = True
    t.save()
    return redirect('tv')

def uncomplete(request,id):
    t = Todo.objects.get(pk=id)
    t.completed = False
    t.save()
    return redirect('tv')
from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from . models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class Testlistview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'task'
class Testdetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task2'
class Testupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('dvhome',kwargs={'pk':self.object.id})
class Testdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('lvhome')

def add(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date = request.POST.get('date', '')
        task=Task(name=name,priority=priority,date=date)
        task.save()

    return render(request,"home.html",{'task':task1})
# def details(request):
#
#     return render(request,"details.html")
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,"delete.html")

def update(request,id):
    task = Task.objects.get(id=id)
    form1=TodoForm(request.POST or None,instance=task)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,'edit.html',{'f':form1,'task':task})

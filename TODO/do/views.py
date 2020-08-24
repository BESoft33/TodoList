from django.shortcuts import render, redirect
from .models import Assignment
from .forms import AssignmentForm

#Function based views

def homepage(request):
    tasks = Assignment.objects.all()
    form = AssignmentForm()

    if request.method == 'POST':
        form = AssignmentForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('/')

    context = {'tasks': tasks,
               'form': form,
               }

    return render(request, 'index.html', context)


def update(request, pk):
    item = Assignment.objects.get(id=pk)
    form = AssignmentForm(instance=item)

    context = {
        'form': form,
    }
    item.delete()

    return render(request, 'update.html', context)


def delete(request, pk):
    item = Assignment.objects.get(id=pk)
    item.delete()

    return redirect('/')

def check(request, pk):
    item = Assignment.objects.get(id=pk)

    if item.completed == True:
        item.completed = False
        item.save()
    else:
        item.completed = True
        item.save()
        
    return redirect('/')
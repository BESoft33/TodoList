from django.shortcuts import render, redirect
from .models import Assignment
from .forms import AssignmentForm


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
    return render(request, 'update.html', context)

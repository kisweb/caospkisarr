from django.shortcuts import render, redirect

from .models import Ief
from account.models import User



def iefs(request):
    iefs = Ief.objects.order_by('name').all()
        # user = User.objects.filter(pk=iefs[0].created_by)
    return render(request, 'ief/iefs.html', {
        'iefs': iefs,
        'segment': 'ief-list'

    })


def ief(request, pk):
    ief = Ief.objects.filter(pk=pk)
        # user = User.objects.filter(pk=iefs[0].created_by)

    return render(request, 'ief/ief.html', {
        'ief': ief
    })

def add(request):

    if request.method == 'POST':
        name = request.POST.get('name', '')
        academie = request.POST.get('academie', '')
        print(request.POST)
        if name:
            Ief.objects.create(name=name, academie=academie)
    context = {'segment': 'ief-add'}

    return render(request, 'ief/add.html', context=context)


def edit(request, pk):
    
    ief = Ief.objects.get(pk=pk)

    if request.method == 'POST':        
        name = request.POST.get('name')
        academie = request.POST.get('academie')
        if name:
            ief.name = name
            ief.academie = academie
            ief.save()
            return redirect('/iefs/')

    return render(request, 'ief/edit.html', {
        'ief': ief
    })


def delete(request, pk):
    ief = Ief.objects.get(pk=pk)
    ief.delete()

    return redirect(f'/iefs/')
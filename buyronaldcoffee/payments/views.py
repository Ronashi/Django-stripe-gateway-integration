from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse


def index(request):
    return render(request, 'payments/index.html')

def charge(request):
    amount = 10
    if request.method == 'POST':
        print('Data:', request.POST['amount'])
    
    return redirect(reverse('success', args=[amount]))

def success_msg(request,args):
    amount = args
    return render(request, 'payments/sucess.html', {'amounts':amounts})    
                  


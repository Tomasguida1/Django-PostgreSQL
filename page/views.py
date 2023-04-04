from django.shortcuts import render, redirect

def lists_vg(request):
    return render(request, 'list_vg.html')

def create_vg(request):
    print (request.POST)
    return redirect('/vg/')
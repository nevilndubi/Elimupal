from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'admindash.html')

def dashboard2(request):
    return render(request, 'index2.html')

def dashboard3(request):
    return render(request, 'index3.html')
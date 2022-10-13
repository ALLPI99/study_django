from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def intnum(request, intnum):
    return render(request, 'intnum.html', {'intnum':intnum})

def string(request, string):
    return render(request, 'string.html', {'string':string})
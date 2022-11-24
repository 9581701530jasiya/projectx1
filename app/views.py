from django.shortcuts import render

# Create your views here.
def elsecondition(request):
    d={'a':100,'b':200}
    return render (request,'elsecondition.html',d)
def ifelif(request):
    s={'a':100,'b':200,'c':300}
    return render(request,'elsecondition.html',s)
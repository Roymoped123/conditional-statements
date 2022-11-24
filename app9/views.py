from django.shortcuts import render

# Create your views here.
def condition1(request):
    d=context={'a':500,'b':400,'c':300}
    return render(request,'condition1.html',d)

from django.shortcuts import render,HttpResponse


def manager(request):
    return render(request, template_name='main.html')
# Create your views here.

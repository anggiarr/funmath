from django.shortcuts import render

# Create your views here.
def indexwelcome(request): 

 return render(request, 'bukawelcome.html')
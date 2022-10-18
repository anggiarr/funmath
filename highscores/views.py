from django.shortcuts import render

# Create your views here.
def indexhighscores(request): 

 return render(request, 'bukahighscores.html')
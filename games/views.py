from django.shortcuts import render

# Create your views here.
def indexgames(request): 

 return render(request, 'bukagames.html')
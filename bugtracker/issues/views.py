from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'index/index.html')
    
def tracker(request):
    if request.user.is_authenticated:
        return render(request, 'tracker/index.html')
    else:
        # return render(request, 'registration/need_login.html')
        return render(request, 'tracker/index.html')

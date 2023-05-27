from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from email_site.models import User

def check_username(request):
    username = request.POST.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)
def index(request):
    return render(request,'login_page.html')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', 'default')
        pass_word = request.POST.get('password', 'default')
        print(user_name)
        print(pass_word)
        return render(request, 'home_screen.html')
    

@csrf_exempt
def sign_up(request):
    if request.method =='POST':
        first_name = request.POST.get('first_name','default')
        middle_name = request.POST.get('middle_name','default')
        last_name = request.POST.get('last_name','default')
        user_name = request.POST.get('username','default')
        pass_word = request.POST.get('password', 'default')
        con_password = request.POST.get('con_password','default')
        return render(request, 'home_screen.html')
    else:
        return render(request,"sign_up.html")


        
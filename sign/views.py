from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return  render(request,"index.html")
# 登陆方法
def  login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123':
            return HttpResponse('login success!!!')
            pass
        else:
            return render(request, 'index.html', {'error':'username or password error!!!'})
        pass
    pass
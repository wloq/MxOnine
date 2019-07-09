from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login#django自带登陆验证函数库
from django.contrib.auth import logout
from users . models import UserProfile
from django.urls import reverse#反向解析网址
from django.contrib.auth.hashers import make_password#加密密码库

# Create your views here.

def index(request):
    return render(request,'index.html')

def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get("username","")
        pass_word = request.POST.get("password","")
        user = authenticate(username=user_name,password=pass_word)#django自带登陆验证函数
        if user is not None:
            login(request,user)#登陆成功，把user通过request传入index.html中
            return render(request,"index.html")
        else:
            return render(request,'login.html',{"msg":"用户名或者密码错误"})#可以传字符串或者变量到指定页面
    else:
        return render(request,'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        email = request.POST.get('email')
        address = request.POST.get('address')
        if username and password and password1 and email and address:
            if password == password1:
                uc = UserProfile.objects.filter(username=username).all().count()  # 验证用户名是否被注册
                if uc == 0:#用户名不存在
                    user_info = {
                        'username': username,
                        'password': make_password(password),
                        'email' :email,
                        'address' : address,
                    }
                    try:
                        UserProfile.objects.create(**user_info)
                        to_url = reverse('user_login')
                        return HttpResponseRedirect(to_url)  # 注册成功跳转到首页
                    except Exception as e:
                        msg = '系统繁忙,注册失败 '
                        return render(request, 'register.html', {"msg": msg})
                else:
                    msg = "用户名已存在，请重新注册"
                    return render(request,"register.html",{"msg":msg})
            else:
                msg = "两次输入密码不一样，请重新输入"
                return render(request, "register.html", {"msg": msg})
        else:
            msg = "用户名，密码，邮件，地址不能为空"
            return render(request,"register.html",{"msg":msg})
    else:
        return render(request,"register.html")


def forgetpwd(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if username:
            uc = UserProfile.objects.filter(username=username).all().count()  # 验证用户名是否被注册
            if uc !=0:#如果用户名存在
                user = UserProfile.objects.get(username=username)
                return render(request,"xiugaipwd.html",{"user":user})
            else:
                msg = "用户名不存在"
                return render(request,"forgetpwd.html",{"msg":msg})
        else:
            msg = "请输入用户名"
            return render(request,"forgetpwd.html",{"msg":msg})
    else:
        return render(request,"forgetpwd.html")

def xiugaipwd(request):
    user_name = request.GET.get('user_name', None)  # get方式从超连接传递过来的参数
    if request.method == 'POST':
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if password and password1:
            if password ==password1:
                user_info = {
                    'password': make_password(password),
                }
                UserProfile.objects.filter(username=user_name).update(**user_info)  # 根据超链接传过来的值更新修改字段里的内容
                return redirect('/user_login/')
            else:
                msg = "两次密码输入不同"
                return render(request, "xiugaipwd.html", {"msg": msg})
        else:
            msg = "密码不能为空"
            return render(request, "xiugaipwd.html", {"msg": msg})
    else:
        return render(request,"xiugaipwd.html",{"msg":user_name})




def tuichu(request):
    logout(request)
    return redirect('/user_login/')
from django.shortcuts import render
from Star.models import *
from django.http import JsonResponse


def index(request):
    star = Star.objects.filter(hot="true")
    articles = Article.objects.all()[:4]
    return render(request, "index.html", locals())


def star_list(request):
    if request.method == "GET":
        page = request.GET.get("page")
        page_size = request.GET.get("page_size")
        onece_page = 5
        if not page:
            page = 1
        if not page_size:
            page_size = 3
        page = int(page)
        page_size = int(page_size)
        if page % onece_page == 0:
            s_n = int(page / onece_page)
            r_n = onece_page
        else:
            s_n = int(page / onece_page) + 1
            r_n = page % onece_page
        total = Star.objects.all()
        select_star = (s_n - 1) * onece_page * page_size
        select_end = s_n * onece_page * page_size
        select_range = total[select_star:select_end]
        return_start = (r_n - 1) * page_size
        return_end = r_n * page_size
        return_range = select_range[return_start:return_end]
        if page <= 3:
            page_range = range(1, 6)
        else:
            page_range = range(page - 2, page + 3)
        return_list = []
        for data in return_range:
            if data.id:
                pic = Picture.objects.filter(star_id=data.id).first().picture.url
            else:
                pic = "None"
            pic = pic.replace("media/","")
            return_list.append({
                "id": data.id,
                "name":data.name,
                "picture": pic
            })
        result = {"data": return_list, "page_range": ",".join([str(i) for i in page_range])}
        return JsonResponse(result)

def list(request):
    return render(request,"list.html")


def view(request, id):
    star = Star.objects.filter(id=id).first()
    n_star = Star.objects.filter(id=str(int(id) + 1)).first()
    l_star = Star.objects.filter(id=str(int(id) - 1)).first()
    pics = Picture.objects.filter(star_id=id)
    return render(request, "view.html", locals())


def register(request):
    return render(request, "register.html", locals())


def register_data(request):
    result = {"state": "error", "data": ""}
    if request.method == "POST" and request.POST:
        data = request.POST
        file = request.FILES
        name = data.get("name")
        age = data.get("age")
        birthday = data.get("birthday")
        description = data.get("description")
        picture = file.get("picture")

        s = Tstar()
        s.name = name
        s.age = age
        s.birthday = birthday
        s.detail = description
        s.picture = picture
        s.save()
        result["state"] = "success"
        result["data"] = "添加成功"

    return JsonResponse(result)

def base(request):
    return render(request,"base.html")

def start(request):
    return render(request,"start.html")


def picwall(request):
    pics = KidPic.objects.all()
    return render(request,"picwall.html",locals())

def search(request):
    if request.method=="POST" and request.POST:
        keyword = request.POST.get("search")
        stars = Star.objects.filter(name__icontains=keyword)
        if not stars:
            stars = ["没有您查询的相关明星",]
    return render(request,"search.html",locals())


def article_detail(request,id):
    id = int(id)
    article = Article.objects.filter(id =id).first()
    return render(request,"article.html",locals())

import random
from django.core.mail import EmailMultiAlternatives

def sendCode(email,code):
    result = {"state": "error", "data": ""}
    try:
        subject = '明星之家欢迎您投稿'  # 标题
        content = "您的验证码是:"+str(code)  # 内容
        sender = '505555162@qq.com'  # 发送的邮箱
        receivers = [email]  # 接收邮件
        massage = EmailMultiAlternatives(subject, content, sender, receivers)
        massage.send()
        result["state"] = "success"
        result["data"] = "发送成功"
    except Exception as e:
        result["data"] = str(e)
    return result

import time

def valid_code(request):
    result = {"state": "error", "data": ""}
    code = ""
    if request.method == "POST":
        email = request.POST.get("email")
        valid_code = ValidCode.objects.filter(email=email)
        code = random.randint(1000, 9999)
        result["code"] = code
        if valid_code:
            valid_code = valid_code.first()
            now = time.time()
            db_time = valid_code.yield_time
            if now - db_time > 60:
                valid_code.yield_time = now
                valid_code.code = code
                valid_code.save()
                result = sendCode(email,code)
            else:
                result["state"] = "success"
                result["data"] = "验证码已经发送,请注意查收"
        else:
            ValidCode.objects.create(code=code,yield_time=time.time(),email=email)
            result = sendCode(email,code)
    else:
        result["data"] = "request method must be post"
    return JsonResponse({"result":result,"code":str(code)})

def show(request):
    id = request.GET.get("id")
    pic = KidPic.objects.filter(id = id).first()
    name = pic.star_name
    return JsonResponse(name,safe=False)
# Create your views here.

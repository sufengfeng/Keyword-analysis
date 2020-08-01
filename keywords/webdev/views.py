import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.from webdev.models import BlogPostz


from webdev import models
from webdev.get_nearby import GetKeyWordList

from webdev.models import User, Article


def josn_ret(request):
    return HttpResponse("Hello world2!")


g_article = None


@csrf_exempt
def index(request):
    global g_article
    email = request.session.get("email", None)  # 如果再次点击登录，则为退出当前用户
    context = {}
    if email:
        context['Log_In'] = "Log Out"
        context['email'] = email
    else:
        context['Log_In'] = "Log In"
        context['email'] = ""
    if g_article != None:
        context['article'] = g_article
        g_article = None
    return render(request, 'index.html', context)


@csrf_exempt
def signup(request):
    if request.session.get("email", None):  # 如果再次点击登录，则为退出当前用户
        # 清除Cookie和Session数据
        request.session.flush()
    if request.method == "POST" and request.POST:

        email = request.POST["email"]
        password = request.POST.get("password")
        password_repeat = request.POST.get("password-repeat")
        role = "None"

        school = request.POST.get("school")
        major = request.POST.get("major")

        if password == password_repeat:
            try:
                counte = 0
                type = "basic"
                # 若创建成功，则自动登录
                ret = models.User.objects.create(email=email, password=password, role=role, school=school, major=major,
                                                 counte=counte, type=type)
                if ret:
                    request.session["email"] = email
                    # 设置超时时间 (Cookie和Session数据的)
                    request.session.set_expiry(60)
                    return HttpResponseRedirect('/')
                else:
                    return render(request, 'signup.html')
            except Exception as e:
                print(e)
    return render(request, 'signup.html')


@csrf_exempt
def login(request):
    if request.session.get("email", None):  # 如果再次点击登录，则为退出当前用户
        # 清除Cookie和Session数据
        request.session.flush()

    if request.method == "POST" and request.POST:
        email = request.POST["email"]
        password = request.POST.get("password")
        users = User.objects.filter(email=email, password=password)
        # print(users.count())
        if users.count() > 0:
            request.session["email"] = email
            # 设置超时时间 (Cookie和Session数据的)
            request.session.set_expiry(0)
            return HttpResponseRedirect('/')
            # /?message=error
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


@csrf_exempt
def userOptions(request):
    email = request.session.get("email", None)  # 如果再次点击登录，则为退出当前用户
    context = {}
    if email:
        if request.method == "POST" and request.POST:  # 登录状态下才允许修改
            password = request.POST.get("password")
            password_repeat = request.POST.get("password-repeat")
            school = request.POST.get("school")
            major = request.POST.get("major")
            if password == password_repeat:
                models.User.objects.filter(email=email).update(password=password, school=school, major=major)
        context['Log_In'] = "Log Out"
        context['email'] = email
        user = User.objects.filter(email=email).all()
        user_list = list(user)
        context['user'] = user_list[0]
        return render(request, 'userOptions.html', context)
    return HttpResponse("用户未登录")


# 根据当前用户渲染页面，如果未登录，则直接报错
def userPanel(request):
    email = request.session.get("email", None)  # 如果再次点击登录，则为退出当前用户
    context = {}
    if email:
        context['Log_In'] = "Log Out"
        context['email'] = email
        context['index'] = 0

        articles = Article.objects.filter(email=email).all()
        article_list = list(articles)
        context['article_list'] = article_list
        return render(request, 'userPanel.html', context)
    return HttpResponse("用户未登录")


# 保存信息，并返回保存状态，若保存成功，则跳转
@csrf_exempt
def save_context(request):
    email = request.session.get("email", None)  # 如果再次点击登录，则为退出当前用户
    retContext = "用户未登录"
    if email == None:  # 如果没有登录
        return HttpResponse(retContext)
    try:
        title = request.GET.get("title", None)  # 如果再次点击登录，则为退出当前用户
        context = request.GET.get("context", None)  # 如果再次点击登录，则为退出当前用户
        if title == "" or context == "":
            retContext = "请补全信息"
            return HttpResponse(retContext)

        ret = models.Article.objects.create(email=email, title=title, context=context)  # 若创建成功，则自动登录
        retContext = "保存成功，即将跳转..."
        return HttpResponse(retContext)
    except Exception as e:
        print(e)
        models.Article.objects.filter(email=email, title=title).update(context=context)
        retContext = "已存在当前title，更新数据..."
        return HttpResponse(retContext)
    return HttpResponse(retContext)


def open_title(request):
    global g_article
    index = request.GET.get("index")
    article = Article.objects.filter(id=index).all()
    g_article = list(article)[0]
    return HttpResponse("Done")


def delete_title(request):
    index = request.GET.get("index")
    models.Article.objects.filter(id=index).delete()
    return HttpResponse("Done")


def get_nearby(request):
    email = request.session.get("email", None)  # 如果再次点击登录，则为退出当前用户
    retContext = "用户未登录"
    if email == None:  # 如果没有登录
        return HttpResponse(retContext)

    keyword01 = request.GET.get("keyword01")
    keyword02 = request.GET.get("keyword02")
    if keyword01 == "" or keyword02 == "":
        retContext = "请输入关键字"
        return HttpResponse(retContext)
    setKeyword01 = GetKeyWordList(keyword01)
    # setKeyword01 = {'失败', '急于', '获得成功', '取得成功', '最终', '胜利', '顺利', '事与愿违', '成功'}
    setKeyword02 = GetKeyWordList(keyword02)
    # setKeyword02 = {'cheque', '达到', '行为', 'bank_check', 'stop', '一定', 'check', '合法', 'tab', 'arrest','stoppage', 'chit', 'assay', 'stay'}
    print(setKeyword01)
    print(setKeyword02)
    jsonRet = {}
    jsonRet["Keyword01"] = list(setKeyword01)
    jsonRet["Keyword02"] = list(setKeyword02)
    counter = models.User.objects.filter(email=email).all()[0].counter
    counter = counter + 1
    models.User.objects.filter(email=email).update(counter=counter)
    return HttpResponse(json.dumps(jsonRet))


def test(request):
    return render(request, 'test.html')


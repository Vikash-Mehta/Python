from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
#def hello(request):
#    text = """<h1>welcome to my app !</h1>"""
#    return HttpResponse(text)

def hello(request):
    print 'ssss'
    today = datetime.datetime.now().date()
    return render(request, "hello.html", {"today" : today})

    #print render(request, "hello.html", {})
    #return render(request, "hello.html", {})
    #text = """<h1>welcome to my app !</h1>"""
    #return HttpResponse(text)

def viewArticle(request, articleId):
    text = "Displaying article Number : %s"%articleId
    return HttpResponse(text)

def viewArticle(request, month, year):
    text = "Displaying articles of : %s/%s"%(year, month)
    return HttpResponse(text)
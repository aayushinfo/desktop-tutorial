#me create
import imp
from django.http import HttpResponse
from  django.shortcuts import render


# def index(request):
#     return HttpResponse('''<a href="https://www.amazon.in">Amzone</a>''')

# def about(request):
#     return HttpResponse('hahah')


def index(request):
    return render(request,'index.html')

# def removepunc(request):
#     dj = request.GET.get('text','default')
#     print(dj)
#     return HttpResponse('''removepunc '''  '''<a href="/">Back</a>''' )

# def charcount(request):
#     return HttpResponse('charcount')

# def spaceremove(request):
#     return HttpResponse('spaceremove')

def analyze(request):
    djj = request.GET.get('text','default')
    # jno = request.GEt.get('removepunc','default') aa line ma error aavr che
    # print(jno)
    print(djj)
    # analyzed = djj    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_'''
    analyzed = ""
    for char in djj:
        if char not in punctuations:
            analyzed=analyzed+char

    params = {'purpose':'Removed Punctuations','analyzed_text': analyzed}
    
    return render(request,'analyze.html',params)
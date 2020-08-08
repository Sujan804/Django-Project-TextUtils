# I created this folder
from django.http import HttpResponse
from django.shortcuts import render
import string
from collections import Counter
import re


def index(request):
    return render(request, 'index.html')


def removepunc(request):
    djtext = request.GET.get('text', 'default')
    checkPunc = request.GET.get('removepunc', 'off')
    checkCap = request.GET.get('capitalize', 'off')
    checkNewLine = request.GET.get('newLineRemove', 'off')
    checkSpace = request.GET.get('spaceRemove', 'off')
    checkCounter = request.GET.get('charCounter', 'off')

    punc = string.punctuation

    Count = 0
    if checkPunc == 'on':
        Analyze = ""
        for char in djtext:
            if char not in punc:
                Analyze += char
        dick = {'name': 'Remove Punctuations', 'Analyze_text': Analyze}
        djtext = Analyze
    if checkCap == 'on':
        Analyze = ""
        for char in djtext:
            Analyze = Analyze + char.upper()
        dick = {'name': 'Uppercase', 'Analyze_text': Analyze}
        djtext = Analyze

    if checkNewLine == 'on':
        Analyze = ""
        for char in djtext:
            if char != '\n' and char != "\r":
                Analyze += char
        dick = {'name': 'Remove New Line', 'Analyze_text': Analyze}
        djtext = Analyze

    if checkSpace == 'on':
        Analyze = ""
        for index, char in enumerate(djtext):
            if djtext[index] == ' ' and djtext[index+1] == ' ':
                pass
            else:
                Analyze += char
        dick = {'name': 'Extra Space Remove', 'Analyze_text': Analyze}
        djtext = Analyze

    if checkCounter == 'on':
        Analyze = ""
        Count = len(djtext)
        dick = {'name': 'Character Counter', 'Analyze_text': Count}
        djtext = Analyze

    if checkCap != 'on' and checkCounter != 'on' and checkNewLine != 'on' and checkPunc != 'on' and checkSpace != 'on':
        return HttpResponse("<h1>Please check your requisites !</h1>")

    return render(request, 'removepunc.html', dick)

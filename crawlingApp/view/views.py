from django.http import HttpResponse
from django.shortcuts import render

import crawlingProject


def index(request):
    return render(request, "index.html")
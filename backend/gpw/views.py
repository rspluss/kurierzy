from django.shortcuts import render, redirect
from .models import Index

from bs4 import BeautifulSoup
from requests import get
from .tasks import download


def home(request):
    indexes = Index.objects.all()

    download.delay()

    context = {'indexes': indexes}
    return render(request, "gpw/index.html", context)


def download_index(request):

    download.delay()

    return redirect('gpw:home')

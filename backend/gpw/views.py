from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from .models import Index
from .tasks import download
from .serializers import IndexSerializer

from rest_framework.response import Response
from rest_framework import generics


class IndexView(generics.RetrieveAPIView):
    queryset = Index.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = IndexSerializer(queryset, many=True)
        return Response(serializer.data)


def home(request):
    indexes = Index.objects.all()

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")

    context = {'indexes': indexes}
    return render(request, "gpw/index.html", context)


def download_index(request):

    download.delay()

    return redirect('gpw:home')


def table(request):
    indexes = Index.objects.all()
    download.delay()

    return render(request, 'gpw/table.html', {'indexes': indexes})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")

    context = {}
    return render(request, "authenticate/login.html", context)


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, "authenticate/register_user.html", context)


def logout_view(request):
    logout(request)

    return redirect('home')

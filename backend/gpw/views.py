from django.shortcuts import render, redirect
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

    context = {'indexes': indexes}
    return render(request, "gpw/index.html", context)


def download_index(request):

    download.delay()

    return redirect('gpw:home')


def table(request):
    download.delay()

    indexes = Index.objects.all()
    return render(request, 'gpw/table.html', {'indexes': indexes})

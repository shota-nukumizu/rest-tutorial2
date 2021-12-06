from rest_framework import generics
from .models import PersonModel
from .serializers import PersonModelSerializer

class ListView(generics.ListCreateAPIView):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonModelSerializer

class DetailView(generics.RetrieveDestroyAPIView):
    queryset = PersonModel.objects.all()
    serializer_class = PersonModelSerializer
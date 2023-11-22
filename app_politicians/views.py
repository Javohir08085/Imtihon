from rest_framework.generics import (
    ListAPIView,RetrieveAPIView,
    CreateAPIView,UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.views import APIView

from django.db.models import Max

from .models import PoliticiansModel
from .serializers import PoliticiansSerializer,PoliticianDetailsSerializer

class PoliticiansListAPIView(ListAPIView):
    queryset = PoliticiansModel.objects.all()
    serializer_class = PoliticiansSerializer

    # def get_queryset(self):
    #     if 'name' in self.request.GET and 'value' in self.request.GET:
    #         match self.request.GET['name']:
    #             case 'name':
    #                 key_word = self.request.GET['value']
    #                 queryset = PoliticiansModel.objects.filter(politician_name__icontains=key_word)
    #             case 'country':
    #                 key_word = self.request.GET['value']
    #                 queryset = PoliticiansModel.objects.filter(politician_country__icontains=key_word)
    #             case 'party':
    #                 key_word = self.request.GET['value']
    #                 queryset = PoliticiansModel.objects.filter(politician_party__icontains=key_word)
    #             case 'position':
    #                 key_word = self.request.GET['value']
    #                 queryset = PoliticiansModel.objects.filter(politician_position__icontains=key_word)
    #             case _:
    #                 key_word = self.request.GET['value']
    #                 queryset = PoliticiansModel.objects.filter(politician_name__icontains=key_word) | PoliticiansModel.objects.filter(book_country__icontains=key_word) | PoliticiansModel.objects.filter(book_party__icontains=key_word) | PoliticiansModel.objects.filter(book_position__icontains=key_word)
    #     else:
    #         queryset = PoliticiansModel.objects.all()
    #
    #     return queryset


class PoliticianDetailAPIView(RetrieveAPIView):
    serializer_class = PoliticiansSerializer
    queryset = PoliticiansModel.objects.all()


class PoliticianCreateAPIView(CreateAPIView):
    queryset = PoliticiansModel.objects.all()
    serializer_class = PoliticiansSerializer


class PoliticianUpdateAPIView(UpdateAPIView):
    queryset = PoliticiansModel.objects.all()
    serializer_class = PoliticiansSerializer


class PoliticianDeleteAPIView(DestroyAPIView):
    queryset = PoliticiansModel.objects.all()
    serializer_class = PoliticiansSerializer


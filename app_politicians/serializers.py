from rest_framework.serializers import ModelSerializer

from .models import PoliticiansModel


class PoliticiansSerializer(ModelSerializer):
    class Meta:
        model = PoliticiansModel
        # fields = ['id', 'politician_name','politician_country','politician_party','politician_position','politician_image']
        fields = '__all__'


class PoliticianDetailsSerializer(ModelSerializer):
    class Meta:
        model = PoliticiansModel
        # fields = ['id', 'politician_name','politician_country','politician_party','politician_position','politician_image']
        fields = '__all__'
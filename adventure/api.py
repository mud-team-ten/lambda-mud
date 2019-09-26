from rest_framework import serializers, viewsets
from .models import Room


class AllRoomsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'title', 'description', 'n_to', 's_to', 'e_to', 'w_to')


class AllRoomsViewSet(viewsets.ModelViewSet):
    serializer_class = AllRoomsSerializer
    queryset = Room.objects.all()

from rest_framework import serializers, viewsets
# from .models import Player

# class PlayerSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta: 
#         model = Player
#         fields = ('currentRoom', 'uuid')

# class PlayerViewset(viewsets.ModelViewSet):
#     serializer_class = PlayerSerializer
#     queryset = Player.objects.all()
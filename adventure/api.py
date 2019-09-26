from rest_framework import serializers, viewsets
from .models import Room, Player


class AllRoomsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'title', 'description', 'n_to', 's_to', 'e_to', 'w_to')


class AllRoomsViewSet(viewsets.ModelViewSet):
    serializer_class = AllRoomsSerializer
    queryset = Room.objects.all()


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('uuid', 'currentRoom')


class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.none()

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Player.objects.filter()
        else:
            return Player.objects.filter(user=user)

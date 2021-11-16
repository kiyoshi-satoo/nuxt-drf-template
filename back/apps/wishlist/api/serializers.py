from rest_framework import serializers

from apps.wishlist.models import WishList


class WishListSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def __str__(self):
        return f'{self.id}'

    def create(self, validated_data):
        wishlist = WishList(self.context['request'])
        wishlist.add(id=validated_data.get('id'))
        return wishlist

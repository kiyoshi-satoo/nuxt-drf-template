from django.urls import path

from apps.wishlist.api.views import WishListView

urlpatterns = [
    #
    path('', WishListView.as_view(), name='wishlist'),
]

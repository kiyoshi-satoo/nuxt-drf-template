from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.wishlist.api.serializers import WishListSerializer
from apps.wishlist.models import WishList
from is_coded.mixins import CustomPaginationMixin


class WishListView(APIView, CustomPaginationMixin):
    pass
#     parser_classes = [FormParser, MultiPartParser, JSONParser]
#     permission_classes = [AllowAny]
#
#     def post(self, request):
#         data = request.data
#         print(request.data)
#         serializer = WishListSerializer(data=data, context={'request': request})
#         if serializer.is_valid(raise_exception=True):
#             wishlist = serializer.save()
#             return Response({"success": f"Successfuly added {wishlist}"})
#         else:
#             return Response({"failed": "Pleaase recheck"}, status=403)
#
#     def delete(self, request):
#         wishlist = WishList(request)
#         data = request.data
#         wishlist.remove(1)
#
#         return Response({"success": f"Successfuly removed"})
#
#     # def get(self, request):
#     #     wishlist = WishList(request)
#     #     # queryset = Announcement.objects.filter(pk__in=[item['id'] for item in wishlist])
#     #     page = self.paginate_queryset(queryset)
#     #     serializer = AnnouncementListSerializer(page, many=True, context={'request': self.request})
#     #
#     #     return self.get_paginated_response(serializer.data)

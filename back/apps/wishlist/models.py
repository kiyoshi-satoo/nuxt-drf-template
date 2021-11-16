from django.conf import settings
from rest_framework.generics import get_object_or_404



class WishList(object):
    def __init__(self, request):
        self.request = request
        self.session = request.session
        wishlist = self.session.get(settings.WISHLIST_SESSION_ID)

        if not wishlist:
            wishlist = self.session[settings.WISHLIST_SESSION_ID] = {}

        self.wishlist = wishlist

    def __iter__(self):
        for item in self.wishlist.values():
            yield item

    def __len__(self):
        return 10

    def add(self, id):
        if str(id) not in list(self.wishlist.keys()):
            self.wishlist[str(id)] = {'id': str(id)}
            self.save()
        for i in self.wishlist:
            print(i,"++")

    def exist(self, id):
        if str(id) in list(self.wishlist.keys()):
            return True
        else:
            return False

    def remove(self, id):
        if self.exist(str(id)):
            del self.wishlist[str(id)]
            self.save()

    def save(self):
        self.session[settings.WISHLIST_SESSION_ID] = self.wishlist
        self.session.modified = True

    def clear(self):
        del self.session[settings.WISHLIST_SESSION_ID]
        self.session.modified = True

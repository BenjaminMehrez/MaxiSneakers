from .favorite import Favorite


def cart(request):
    return {'favorite': Favorite(request)}
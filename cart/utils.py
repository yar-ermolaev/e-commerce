from .models import Cart


def get_or_create_cart(request):
    if not request.user.is_authenticated:
        if not request.session.session_key:
            request.session.create()
        cart, _ = Cart.objects.get_or_create(session_key=request.session.session_key)
    else:
        cart, _ = Cart.objects.get_or_create(user=request.user)
    return cart

from .models import UserProfile, UserWishList


def get_wish_list(request):
    """ Function used site wide to collate and list products """
    if request.user.is_authenticated:
        # get users profile
        user = UserProfile.objects.get(user=request.user)
        list_to_display = []
        # check to see if there are any products in the list
        for item in UserWishList.objects.filter(user=user):
            # add product to list
            list_to_display.append(item.product)
    else:
        # render empty list
        list_to_display = []
    return {
            'wishlist_items': list_to_display,
        }
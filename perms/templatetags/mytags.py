from django import template
from users.models import User


register = template.Library()


@register.filter(name='get_user_perm_asset_list')
def get_user_perm_asset_list(user_id):
    asset_list = []

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return asset_list

    perm_iter = user.perm_set.iterator()
    for perm in perm_iter:
        asset_list.extend(perm.asset.all())

    return list(set(asset_list))


@register.filter
def get_user_perm_asset_count(user_id):
    asset_list = get_user_perm_asset_list(user_id)
    return len(asset_list)

# coding: utf-8

from .models import Perm


def get_user_asset(user):
    assets = set()
    perms = Perm.objects.filter(user=user)
    for perm in perms:
        for asset in perm.asset.iterator():
            assets.add(asset)
    return assets

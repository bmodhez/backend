from django.shortcuts import render
from assets.models.asset import Asset
from assets.models.license import License
from assets.models.accessories import Accessory
from assets.models.consumables import Consumable
from assets.models.components import Component


def dashboard(request):
    assets_count = Asset.objects.count()
    licenses_count = License.objects.count()
    accessories_count = Accessory.objects.count()
    consumables_count = Consumable.objects.count()
    components_count = Component.objects.count()

    context = {
        "assets_count": assets_count,
        "licenses_count": licenses_count,
        "accessories_count": accessories_count,
        "consumables_count": consumables_count,
        "components_count": components_count,
    }

    return render(request, "dashboard/dashboard.html", context)

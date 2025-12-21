from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from assets.models import Asset, License, Accessory, Consumable, Component

@login_required
def dashboard(request):
    return render(request, "dashboard/dashboard.html", {
    "assets": Asset.objects.all(),
    "licenses": License.objects.all(),
    "accessories": Accessory.objects.all(),
    "consumables": Consumable.objects.all(),
    "components": Component.objects.all(),
})

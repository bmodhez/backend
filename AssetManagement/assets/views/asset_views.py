from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from assets.models import Asset

User = get_user_model()


@login_required
def asset_list(request):
    assets = Asset.objects.filter(is_deleted=False)
    return render(request, "asset_list.html", {
        "assets": assets
    })


@login_required
def asset_create(request):
    users = User.objects.all()

    if request.method == "POST":
        Asset.objects.create(
            name=request.POST.get("name"),
            asset_tag=request.POST.get("asset_tag"),
            category=request.POST.get("category"),
            status=request.POST.get("status"),
            location=request.POST.get("location"),
            purchase_cost=request.POST.get("purchase_cost") or None,
            assigned_to_id=request.POST.get("assigned_to") or None,
            image=request.FILES.get("image"),
        )
        return redirect("asset_list")

    return render(request, "asset_form.html", {
        "users": users,
        "status_choices": Asset.STATUS_CHOICES,   
    })


@login_required
def asset_edit(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id, is_deleted=False)
    users = User.objects.all()

    if request.method == "POST":
        asset.name = request.POST.get("name")
        asset.asset_tag = request.POST.get("asset_tag")
        asset.category = request.POST.get("category")
        asset.status = request.POST.get("status")
        asset.location = request.POST.get("location")
        asset.purchase_cost = request.POST.get("purchase_cost") or None
        asset.assigned_to_id = request.POST.get("assigned_to") or None

        if request.FILES.get("image"):
            asset.image = request.FILES["image"]

        asset.save()
        return redirect("asset_list")

    return render(request, "asset_form.html", {
        "asset": asset,
        "users": users,
        "status_choices": Asset.STATUS_CHOICES,   
    })


@login_required
def asset_delete(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id, is_deleted=False)

    if request.method == "POST":
        asset.is_deleted = True
        asset.save()

    return redirect("asset_list")

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from assets.models import Consumable


@login_required
def consumable_list(request):
    consumables = Consumable.objects.filter(is_deleted=False)
    return render(request, "consumable_list.html", {
        "consumables": consumables
    })


@login_required
def consumable_create(request):
    if request.method == "POST":
        Consumable.objects.create(
            name=request.POST.get("name"),
            category=request.POST.get("category"),
            model_no=request.POST.get("model_no"),
            item_no=request.POST.get("item_no"),
            order_number=request.POST.get("order_number"),
            purchase_date=request.POST.get("purchase_date") or None,
            min_quantity=request.POST.get("min_quantity") or 0,
            quantity=request.POST.get("quantity"),
            unit_cost=request.POST.get("unit_cost") or None,
            location=request.POST.get("location"),
        )
        return redirect("consumable_list")

    return render(request, "consumable_form.html")


@login_required
def consumable_edit(request, consumable_id):
    consumable = get_object_or_404(
        Consumable, id=consumable_id, is_deleted=False
    )

    if request.method == "POST":
        consumable.name = request.POST.get("name")
        consumable.category = request.POST.get("category")
        consumable.quantity = request.POST.get("quantity")
        consumable.location = request.POST.get("location")
        consumable.save()
        return redirect("consumable_list")

    return render(request, "consumable_form.html", {
        "consumable": consumable
    })


@login_required
def consumable_delete(request, consumable_id):
    consumable = get_object_or_404(
        Consumable, id=consumable_id, is_deleted=False
    )

    if request.method == "POST":
        consumable.is_deleted = True
        consumable.save()

    return redirect("consumable_list")

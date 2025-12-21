from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from assets.models import Accessory


@login_required
def accessory_list(request):
    accessories = Accessory.objects.filter(is_deleted=False)
    return render(request, "accessory_list.html", {
        "accessories": accessories
    })


@login_required
def accessory_create(request):
    if request.method == "POST":
        Accessory.objects.create(
            name=request.POST.get("name"),
            category=request.POST.get("category"),
            model_no=request.POST.get("model_no"),
            location=request.POST.get("location"),
            min_quantity=request.POST.get("min_quantity") or 0,
            quantity=request.POST.get("quantity"),
            device_image=request.FILES.get("device_image"),
        )
        return redirect("accessory_list")

    return render(request, "accessory_form.html")


@login_required
def accessory_edit(request, accessory_id):
    accessory = get_object_or_404(
        Accessory, id=accessory_id, is_deleted=False
    )

    if request.method == "POST":
        accessory.name = request.POST.get("name")
        accessory.category = request.POST.get("category")
        accessory.model_no = request.POST.get("model_no")
        accessory.location = request.POST.get("location")
        accessory.min_quantity = request.POST.get("min_quantity") or 0
        accessory.quantity = request.POST.get("quantity")

        if request.FILES.get("device_image"):
            accessory.device_image = request.FILES["device_image"]

        accessory.save()
        return redirect("accessory_list")

    return render(request, "accessory_form.html", {
        "accessory": accessory
    })


@login_required
def accessory_delete(request, accessory_id):
    accessory = get_object_or_404(
        Accessory, id=accessory_id, is_deleted=False
    )

    if request.method == "POST":
        accessory.is_deleted = True
        accessory.save()

    return redirect("accessory_list")

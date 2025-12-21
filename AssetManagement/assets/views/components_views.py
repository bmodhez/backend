
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from assets.models import Component


@login_required
def component_list(request):
    components = Component.objects.filter(is_deleted=False)
    return render(request, "component_list.html", {
        "components": components
    })


@login_required
def component_create(request):
    if request.method == "POST":
        Component.objects.create(
            name=request.POST.get("name"),
            serial=request.POST.get("serial"),
            category=request.POST.get("category"),
            model_no=request.POST.get("model_no"),
            order_number=request.POST.get("order_number"),
            purchase_date=request.POST.get("purchase_date") or None,
            min_quantity=request.POST.get("min_quantity") or 0,
            quantity=request.POST.get("quantity"),
            unit_cost=request.POST.get("unit_cost") or None,
            location=request.POST.get("location"),
        )
        return redirect("component_list")

    return render(request, "component_form.html")


@login_required
def component_edit(request, component_id):
    component = get_object_or_404(
        Component, id=component_id, is_deleted=False
    )

    if request.method == "POST":
        component.name = request.POST.get("name")
        component.serial = request.POST.get("serial")
        component.category = request.POST.get("category")
        component.model_no = request.POST.get("model_no")
        component.order_number = request.POST.get("order_number")
        component.purchase_date = request.POST.get("purchase_date") or None
        component.min_quantity = request.POST.get("min_quantity") or 0
        component.quantity = request.POST.get("quantity")
        component.unit_cost = request.POST.get("unit_cost") or None
        component.location = request.POST.get("location")
        component.save()

        return redirect("component_list")

    return render(request, "component_form.html", {
        "component": component
    })


@login_required
def component_delete(request, component_id):
    component = get_object_or_404(
        Component, id=component_id, is_deleted=False
    )

    if request.method == "POST":
        component.is_deleted = True
        component.save()

    return redirect("component_list")

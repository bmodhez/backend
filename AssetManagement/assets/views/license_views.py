
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from assets.models import License


@login_required
def license_list(request):
    licenses = License.objects.filter(is_deleted=False)
    return render(request, "license_list.html", {
        "licenses": licenses
    })


@login_required
def license_detail(request, license_id):
    license = get_object_or_404(License, id=license_id, is_deleted=False)
    return render(request, "assets/licenses/detail.html", {
        "license": license
    })


@login_required
def license_create(request):
    if request.method == "POST":
        License.objects.create(
            name=request.POST.get("name"),
            product_key=request.POST.get("product_key"),
            manufacturer=request.POST.get("manufacturer"),
            total_seats=request.POST.get("total_seats"),
            available_seats=request.POST.get("available_seats"),
            expiration_date=request.POST.get("expiration_date"),

            licensed_to_name=request.POST.get("licensed_to_name"),
            licensed_to_email=request.POST.get("licensed_to_email"),
        )
        return redirect("license_list")

    return render(request, "license_form.html")


@login_required
def license_edit(request, license_id):
    license = get_object_or_404(License, id=license_id, is_deleted=False)

    if request.method == "POST":
        license.name = request.POST.get("name")
        license.product_key = request.POST.get("product_key")
        license.manufacturer = request.POST.get("manufacturer")
        license.total_seats = request.POST.get("total_seats")
        license.available_seats = request.POST.get("available_seats")
        license.expiration_date = request.POST.get("expiration_date")

        license.licensed_to_name = request.POST.get("licensed_to_name")
        license.licensed_to_email = request.POST.get("licensed_to_email")

        license.save()
        return redirect("license_list")

    return render(request, "license_form.html", {
        "license": license
    })



@login_required
def license_delete(request, license_id):
    license = get_object_or_404(License, id=license_id, is_deleted=False)

    if request.method == "POST":
        license.is_deleted = True
        license.save()

    return redirect("license_list")

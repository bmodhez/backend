from django.urls import path

from assets.views.dash_views import dashboard
from assets.views.asset_views import (
    asset_list,
    asset_create,
    asset_edit,
    asset_delete,
)

from assets.views.license_views import (
    license_list,
    license_create,
    license_edit,
    license_delete,
)
from assets.views.accessories_views import (
    accessory_list,
    accessory_create,
    accessory_edit,
    accessory_delete,
)

from assets.views.consumables_views import (
    consumable_list,
    consumable_create,
    consumable_edit,
    consumable_delete,
)

from assets.views.components_views import (
    component_list,
    component_create,
    component_edit,
    component_delete,
)

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("assets/", asset_list, name="asset_list"),
    path("assets/create/", asset_create, name="asset_create"),
    path("assets/<int:asset_id>/edit/", asset_edit, name="asset_edit"),
    path("assets/<int:asset_id>/delete/", asset_delete, name="asset_delete"),
    path("licenses/", license_list, name="license_list"),
    path("licenses/create/", license_create, name="license_create"),
    path("licenses/<int:license_id>/edit/", license_edit, name="license_edit"),
    path("licenses/<int:license_id>/delete/", license_delete, name="license_delete"),
    path("accessories/", accessory_list, name="accessory_list"),
    path("accessories/create/", accessory_create, name="accessory_create"),
    path("accessories/<int:accessory_id>/edit/", accessory_edit, name="accessory_edit"),
    path("accessories/<int:accessory_id>/delete/", accessory_delete, name="accessory_delete"),
    path("consumables/", consumable_list, name="consumable_list"),
    path("consumables/create/", consumable_create, name="consumable_create"),
    path("consumables/<int:consumable_id>/edit/", consumable_edit, name="consumable_edit"),
    path("consumables/<int:consumable_id>/delete/", consumable_delete, name="consumable_delete"),
    path("components/", component_list, name="component_list"),
    path("components/create/", component_create, name="component_create"),
    path("components/<int:component_id>/edit/", component_edit, name="component_edit"),
    path("components/<int:component_id>/delete/", component_delete, name="component_delete"),
]

from django.contrib import admin
from django.urls import path, include
from formapp.views import index, show_applications, delete_application

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("applications/", show_applications, name="applications"),
    path("applications/<int:id>/delete/", delete_application, name="delete_application"),
]

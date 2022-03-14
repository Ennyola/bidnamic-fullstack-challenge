from django.contrib import admin
from django.urls import path,include
from formapp.views import index,show_applications,delete_application
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('applications/',show_applications,name="applications" ),
    path('', index, name="index"),
    path('<int:id>/delete/',delete_application,name="delete-application")
]

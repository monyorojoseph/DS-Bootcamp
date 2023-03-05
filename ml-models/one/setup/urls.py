from django.contrib import admin
from django.urls import path
from endpoints.urls import urlpatterns as endpoint_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
]
urlpatterns += endpoint_urlpatterns

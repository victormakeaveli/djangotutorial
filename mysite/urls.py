from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('polls.urls', namespace="polls")),
    path('admin/', admin.site.urls),
]

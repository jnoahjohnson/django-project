from operator import index
from django.urls import path
from .views import indexPageView, darthPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("darth/<darth_name>", darthPageView, name="anything")
]

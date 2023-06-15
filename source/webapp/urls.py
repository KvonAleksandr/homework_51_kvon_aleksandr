from django.urls import path
from webapp.views import home, cat_stats

urlpatterns = [
    path("", home),
    path("cat_stats/", cat_stats),
]
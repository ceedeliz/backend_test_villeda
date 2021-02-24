from django.urls import path, re_path
from . import views
app_name = "meal"

urlpatterns = [
    path(
        'meal/list',
        views.MealListApiView.as_view()
    ),
    path(
        'meal/create',
        views.MealCreateApiView.as_view()
    ),
    path(
        'meal/list/<fk>',
        views.MealActiveView.as_view()
    ),
    path(
        'meal/<pk>',
        views.MealDetailView.as_view()
    ),
    path(
        'meal/delete/<pk>',
        views.MealDeleteView.as_view()
    ),
    path(
        'meal/update/<pk>',
        views.MealUpdateView.as_view()
    ),
]

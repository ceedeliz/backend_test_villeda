from django.urls import path, re_path
from . import views
app_name = "menu"

urlpatterns = [
    path(
        'menu/active',
        views.MenuActiveView.as_view()
    ),
    path(
        'menu/list',
        views.MenuListApiView.as_view()
    ),
    path(
        'menu/create',
        views.MenuCreateApiView.as_view(),
    ),
    path(
        'menu/<pk>',
        views.MenuDetailView.as_view()
    ),
    path(
        'menu/delete/<pk>',
        views.MenuDeleteView.as_view()
    ),
    path(
        'menu/update/<pk>',
        views.MenuUpdateView.as_view()
    ),
]

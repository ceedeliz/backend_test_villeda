from django.urls import path, re_path
from . import views
app_name = "order"

urlpatterns = [
    path(
        'order/list',
        views.OrderListApiView.as_view()
    ),
    path(
        'order/create',
        views.OrderCreateApiView.as_view()
    ),
    path(
        'order/<pk>',
        views.OrderDetailView.as_view()
    ),
    path(
        'order/delete/<pk>',
        views.OrderDeleteView.as_view()
    ),
    path(
        'order/update/<pk>',
        views.OrderUpdateView.as_view()
    ),
]

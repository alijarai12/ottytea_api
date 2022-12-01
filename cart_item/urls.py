from django.urls import path
from .import views

urlpatterns = [


#
    path('', views.CartitemCreateListView.as_view(), name='cart'),

    #path('update-status/<int:order_id>/', views.UpdateOrderStatus.as_view(), name='update_orders_status'),


]

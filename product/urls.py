from django.urls import path
from .import views

urlpatterns = [


#
    path('teacaty/', views.CategoryCreateListView.as_view(), name='category'),
    path('teacaty/<int:cat_id>/', views.CategoryDetailView.as_view(), name='caty'),

    path('teaproduct/', views.TeaCreateListView.as_view(), name='teaproduct'),
    path('teaproduct/<int:tea_id>/', views.TeaDetailView.as_view(), name='tea'),


    #path('update-status/<int:order_id>/', views.UpdateOrderStatus.as_view(), name='update_orders_status'),


]

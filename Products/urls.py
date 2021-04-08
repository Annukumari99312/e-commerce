from django.urls import path
from .views import ProductListView, ProductDetailView

app_name = "products"

urlpatterns = [
    path('products', ProductListView.as_view(), name="product"),
    path('detail/<slug:slug>/', ProductDetailView.as_view(), name="detail")
]
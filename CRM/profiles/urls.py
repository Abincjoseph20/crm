from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_customer, name='create_customer'),
    path('customers/', views.customer_list, name='list'),
    path('customers/details/<int:pk>',views.details,name='details'),
    path('customers/edit/<int:pk>', views.edit_customer, name='edit'),
    path('customers/delete/<int:pk>', views.delete, name='delete'),
    path('categories/<slug:val>/', views.Category.as_view(), name="category"),
    
    path('categories-title/<slug:val>/', views.CategoryTitle.as_view(), name="category-title"),
    # path('product/<int:pk>/', views.ProductDetails.as_view(), name="product-details"),
    # path('search/', views.SearchResults.as_view(), name='search_results'),
]

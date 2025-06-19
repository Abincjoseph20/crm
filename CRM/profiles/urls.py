from django.urls import path
from . import views

urlpatterns = [
    path('Home',views.Home,name='home'),
    path('create_customer/', views.create_customer, name='create_customer'),
    path('customers/', views.customer_list, name='list'),
    path('customers/details/<int:pk>',views.details,name='details'),

    path('customers/edit/<int:pk>', views.edit_customer, name='edit'),
    path('customers/delete/<int:pk>', views.delete, name='delete'),
    
    path('categories/<slug:val>/', views.Bank_Category.as_view(), name="category"),
    path('product_catogory/<slug:val>/', views.Pdoduct_Catogory.as_view(),name="product_catogory"),
    
    path('search/', views.search, name='search'),
    
    path('dsa_create',views.dsa,name='dsa_create'),
    path('dsa_list',views.dsa_lis,name='dsa_list'),
    
    path('status_filter/<slug:status>',views.status_filter.as_view(),name='status_filter'),
    
    path('create_task/',views.Create_Task,name='create_task'),
    path('task_list',views.task_list,name='task_list'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('upcoming-notifications/', views.upcoming_notifications, name='upcoming_notifications'),  # New notifications view
    # path('api/loan-status-distribution/', views.loan_status_distribution, name='loan-status-distribution'),
    path('', views.get_count.as_view(), name='get_counts'),

    
]

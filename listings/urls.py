from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='listings'),
    path("<int:listing_id>", views.listing, name='listing'),
    # path("<int:pk>", views.SingleListingView.as_view(), name='listing'),
    path("search", views.search, name='search'),
    path('insert', views.insert, name='insert'),
    path('edit/<int:listing_id>', views.edit, name='edit'),
    path('remove/<int:listing_id>', views.remove, name='remove'),
    path('create-report/<int:listing_id>', views.create_report, name='create-report'),
]


from django.urls import path
from . import views
# from .views import ListingDeleteView
# from .views import ListingListView

urlpatterns = [
    # path('', views.ListingView.as_view(), name='listings'),
    path("", views.index, name='listings'),
    path("<int:listing_id>", views.listing, name='listing'),
    # path("<int:pk>", views.SingleListingView.as_view(), name='listing'),
    # path("table-test", views.table_test, name='table-test'),
    # path('table-test', ListingListView.as_view(), name='table-test'),
    path("search", views.search, name='search'),
    path('insert', views.insert, name='insert'),
    path('<int:listing_id>/edit', views.edit, name='edit'),
    path('<int:listing_id>/remove', views.remove, name='remove'),
    # path('remove/<int:pk>', ListingDeleteView.as_view(), name='remove'),
    path('<int:listing_id>/create-report', views.create_report, name='create-report'),
    path('<int:listing_id>/upload-report', views.upload_report, name='upload-report'),

]


from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.allShows),
    path('shows/new',views.new),
    path('create', views.create),
    path('shows/<int:show_id>', views.show),
    path('delete/<int:show_id>', views.delete)
]
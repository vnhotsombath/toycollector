from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('toys/',views.toys_index, name='index'),
    path('toys/<int:toy_id>/', views.toys_detail, name='detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('toys/<int:toy_id>/add_piece/', views.add_piece, name='add_piece'),
    path('abilities/', views.AbilityList.as_view(), name='abilities_index'),
    path('abilities/<int:pk>/', views.AbilityDetail.as_view(), name='abilities_detail'),
    path('abilities/create/', views.AbilityCreate.as_view(), name='abilities_create'),
    path('abilities/<int:pk>/upate/', views.AbilityUpdate.as_view(), name='abilities_update'),
    path('abilities/<int:pk>/delete/', views.AbilityDelete.as_view(), name='abilities_delete'),
]
# routes will live in here
from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('finches/', views.finch_index, name='finch-index'),
  path('finches/<int:finch_id>/', views.finch_detail, name='finch-detail'),  
  path('finches/create/', views.FinchCreate.as_view(), name='finch-create'),  
  path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finch-update'),
  path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finch-delete'),
  path('finches/<int:finch_id>/add-feeding/', views.add_feeding, name='add-feeding'),
  path('weapons/create/', views.WeaponCreate.as_view(), name='weapon-create'),
  path('weapons/<int:pk>/', views.WeaponDetail.as_view(), name='weapon-detail'),
  path('weapons/', views.WeaponList.as_view(), name='weapon-index'),
  path('weapons/<int:pk>/update/', views.WeaponUpdate.as_view(), name='weapon-update'),
  path('weapons/<int:pk>/delete/', views.WeaponDelete.as_view(), name='weapon-delete'),
  path('finches/<int:finch_id>/assoc-weapon/<int:weapon_id>/', views.assoc_weapon, name='assoc-weapon'),
  path('accounts/signup/', views.signup, name='signup'),
]
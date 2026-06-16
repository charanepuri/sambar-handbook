from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('varieties/', views.varieties, name='varieties'),
    
    path('variety/<int:id>/', views.variety_detail, name='variety_detail'),

    path('ingredients/', views.ingredients, name='ingredients'),

    path('ingredient/<int:id>/', views.ingredient_detail, name='ingredient_detail'),

    path('recipes/', views.recipes, name='recipes'),

    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),

    path('nutrition/', views.nutrition, name='nutrition'),

    path('facts/', views.facts, name='facts'),

    path('about/', views.about, name='about'),
    
    path('shopping-list/', views.shopping_list, name='shopping_list'),
    
    path('contact/', views.contact, name='contact'),
    
    path('history/', views.history, name='history'),
    
    path('tips/', views.tips, name='tips'),
    
    path('gallery/', views.gallery, name='gallery'),
    
    path('search/', views.search, name='search'),

]
from django.urls import path

from recipes_app import views

urlpatterns = [
    path('recipe/add_recipe', views.add_recipe),
    path('recipe/get_all_recipes', views.get_all_recipes),
    path('recipe/get_recipe_by_id/<int:recipe_id>', views.get_recipe_by_id),
    path('recipe/delete_recipe/<int:recipe_id>/', views.delete_recipe),
    path('recipe/edit_recipe/<int:recipe_id>/', views.edit_recipe)
]
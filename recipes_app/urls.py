from django.urls import path
from rest_framework.routers import DefaultRouter

from recipes_app import views
from recipes_app.view_sets import RecipesViewSet

router = DefaultRouter()
router.register('recipe_view_set', RecipesViewSet)

urlpatterns = [
    # path('recipe/add_recipe', views.add_recipe),
    # path('recipe/get_all_recipes', views.get_all_recipes),
    path('recipe', views.recipe),
    # path('recipe/get_recipe_by_id/<int:recipe_id>', views.get_recipe_by_id),
    # path('recipe/delete_recipe/<int:recipe_id>/', views.delete_recipe),
    # path('recipe/edit_recipe/<int:recipe_id>/', views.edit_recipe)
    path('recipe_by_id/<int:recipe_id>', views.recipe_by_id)
]

# extend!!
urlpatterns.extend(router.urls)
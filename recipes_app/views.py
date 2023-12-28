from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from recipes_app.models import Recipe
from recipes_app.serializers import RecipeSerializer

#  if request.method == 'GET':

@api_view(['POST', 'GET'])
def recipe(request):
    if request.method == 'POST':
        data = request.data
        serializer = RecipeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'GET':
        queryset = Recipe.objects.filter(delete=False)
        serializer = RecipeSerializer(instance=queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE', 'PUT', 'PATCH', 'GET'])
def recipe_by_id(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'GET':
        serializer = RecipeSerializer(instance=recipe)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data = {
            'delete': True
        }
        # recipe.delete()
        serializer = RecipeSerializer(instance=recipe, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = RecipeSerializer(
            instance=recipe,
            data=request.data,
            partial=request.method == 'PATCH'
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)



# @api_view(['POST'])
# def add_recipe(request):
#     data = request.data
#     serializer = RecipeSerializer(data=data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['GET'])
# def get_all_recipes(request):
#     queryset = Recipe.objects.filter(delete=False)
#     serializer = RecipeSerializer(instance=queryset, many=True)
#     return Response(data=serializer.data, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def get_recipe_by_id(request, recipe_id):
#     # recipe = Recipe.objects(id=recipe_id)
#     recipe = get_object_or_404(Recipe, id=recipe_id)
#     serializer = RecipeSerializer(instance=recipe)
#     return Response(data=serializer.data, status=status.HTTP_200_OK)
#
# @api_view(['DELETE'])
# def delete_recipe(request, recipe_id):
#     recipe = get_object_or_404(Recipe, id=recipe_id)
#     data = {
#         'delete': True
#     }
#     # recipe.delete()
#     serializer = RecipeSerializer(instance=recipe, data=data, partial=True)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
# #     return Response(status=status.HTTP_204_NO_CONTENT)
#
# @api_view(['PUT', 'PATCH'])
# def edit_recipe(request, recipe_id):
#     recipe = get_object_or_404(Recipe, id=recipe_id)
#     serializer = RecipeSerializer(
#             instance=recipe,
#             data=request.data,
#             partial=request.method == 'PATCH'
#         )
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(data=serializer.data, status=status.HTTP_200_OK)


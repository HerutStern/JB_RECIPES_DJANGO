from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from recipes_app.models import Recipe
from recipes_app.serializers import RecipeSerializer


# class RecipesViewSet(viewsets.ModelViewSet):
#     serializer_class = RecipeSerializer
#     queryset = Recipe.objects.all()


class RecipesViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    # queryset = Recipe.objects.filter(delete=False)

    def get_queryset(self):
        queryset = Recipe.objects.filter(delete=False)
        return queryset

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     queryset = queryset.filter(delete=False)
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

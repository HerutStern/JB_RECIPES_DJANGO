from rest_framework.serializers import ModelSerializer
from recipes_app.models import Recipe


class RecipeSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
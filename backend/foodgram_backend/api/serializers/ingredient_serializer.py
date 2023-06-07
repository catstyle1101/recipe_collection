from rest_framework import serializers

from foodgram.models import IngredientRecipe, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class IngredientRecipeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source="ingredient_id.id")
    name = serializers.ReadOnlyField(source="ingredient_id.name")
    measurement_unit = serializers.ReadOnlyField(
        source="ingredient_id.measurement_unit"
    )

    class Meta:
        model = IngredientRecipe
        fields = (
            "id",
            "name",
            "measurement_unit",
            "amount",
        )

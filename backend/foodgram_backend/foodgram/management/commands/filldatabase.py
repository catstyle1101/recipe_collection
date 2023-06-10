import json
from argparse import RawTextHelpFormatter

from django.core.management.base import BaseCommand
from foodgram.models import Ingredient, Tag


class Command(BaseCommand):
    """
    Fills database with ingredients and tags.
    """
    help = """Заполняет базу данных из json файлов в папке data
        """

    def create_parser(self, *args, **kwargs):
        parser = super(Command, self).create_parser(*args, **kwargs)
        parser.formatter_class = RawTextHelpFormatter
        return parser

    def handle(self, *args, **kwargs) -> None:
        ingredients = Ingredient.objects.all()
        if len(ingredients) == 0:
            ingredients.delete()
            with open("./data/ingredients.json", "r", encoding="utf8") as file:
                ingredients_list = json.load(file)
            for ingredient in ingredients_list:
                ingredient_instance = Ingredient(**ingredient)
                ingredient_instance.save(force_insert=True)
            self.stdout.write("Ингредиенты загружены в БД")
        tags = Tag.objects.all()
        if len(tags) == 0:
            tags.delete()
            with open("./data/tags.json", "r", encoding="utf8") as file:
                tags_list = json.load(file)
            for tag in tags_list:
                tag_instance = Tag(**tag)
                tag_instance.save(force_insert=True)
            self.stdout.write("Теги загружены в БД")


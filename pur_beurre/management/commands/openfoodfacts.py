import requests
from django.core.management.base import BaseCommand, CommandError
from pur_beurre.models import Product, Categories

NB_PROD_PAGE = 20
NB_PROD_REQUEST = 60
NB_CAT_REQUEST = 20

class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        read the categories from open food facts api and select some categorie
        """

        url = requests.get("https://fr.openfoodfacts.org/langue/francais/categories.json")
        data_raw = url.json()
        data_categories = data_raw["tags"]
        for categories in data_categories[0:NB_CAT_REQUEST]:
            cat_prod = Categories.objects.create(name=categories["name"])
            print(cat_prod)

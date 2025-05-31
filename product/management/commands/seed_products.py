import random
from django.core.management.base import BaseCommand
from product.models import Category, SubCategory, Product

class Command(BaseCommand):
    help = "Seed the database with Categories, SubCategories, and 100 Products"

    def handle(self, *args, **options):
        # Sample categories and their subcategories
        categories_data = {
            "Electronics": ["Mobile Phones", "Laptops", "Cameras", "Accessories"],
            "Clothing": ["Men", "Women", "Kids"],
            "Home & Kitchen": ["Furniture", "Appliances", "Decor"],
            "Books": ["Fiction", "Non-fiction", "Comics"],
            "Sports": ["Outdoor", "Gym", "Accessories"],
        }

        # Create categories and subcategories
        categories = []
        for cat_name, subcat_names in categories_data.items():
            cat, created = Category.objects.get_or_create(name=cat_name)
            categories.append(cat)
            for subcat_name in subcat_names:
                SubCategory.objects.get_or_create(category=cat, name=subcat_name)

        subcategories = list(SubCategory.objects.all())

        # Clear existing products (optional, remove if you want to keep old data)
        Product.objects.all().delete()

        # Generate 100 products
        for i in range(1, 501):
            # Pick a random subcategory
            subcat = random.choice(subcategories)
            cat = subcat.category

            product_name = f"{cat.name} {subcat.name} Product {i}"
            description = f"This is the description for {product_name}."
            price = round(random.uniform(10.0, 1000.0), 2)
            quantity = random.randint(1, 100)

            Product.objects.create(
                category=cat,
                sub_category=subcat,
                name=product_name,
                description=description,
                price=price,
                quantity=quantity,
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded 100 products.'))

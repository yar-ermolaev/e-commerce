import json
import os
import random
from pathlib import Path
import django
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
django.setup()
from products.models import Category, Product


def get_media_paths(from_path: str, base_path=settings.MEDIA_ROOT):
    full_path = Path(base_path, from_path)
    relative_paths = []
    for file_path in full_path.glob('*'):
        relative_paths.append(str(file_path.relative_to(settings.MEDIA_ROOT)))
    return relative_paths


def load_db():
    with open(r'E:\Dev\collect_data\data\dishwashers\db_0-71.json', encoding='utf-8') as file:
        db = json.load(file)

    cat = Category.objects.get(pk=1)

    for id_, data in db.items():
        amount = random.randint(1, 100) if not data.get('sold_out') else 0
        Product.objects.create(name=data.get('name'),
                               slug=data.get('slug'),
                               manufacturer=data.get('brand'),
                               in_stock=amount,
                               price=data.get('price'),
                               properties=data.get('properties'),
                               description=data.get('description'),
                               image_paths=get_media_paths(f'dishwashers/{id_}'),
                               category=cat)


# def convert_paths(image_paths: list, base_path=settings.MEDIA_ROOT):
#     return [str(Path(base_path, path) for path in image_paths)]


if __name__ == '__main__':
    load_db()
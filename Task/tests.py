
from models import Category
for c in Category.objects.all():
    print(c.id, c.name, c.get_name_display())
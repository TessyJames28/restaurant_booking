from booking.models import Menu

# Seed data
menu_items = [
    {"name": "Bruschetta", "price": 6.50, "menu_item_description": "Grilled bread rubbed with garlic and topped with olive oil, salt, and fresh tomatoes."},
    {"name": "Greek Salad", "price": 8.00, "menu_item_description": "A refreshing salad with cucumbers, tomatoes, olives, feta cheese, and olive oil."},
    {"name": "Grilled Fish", "price": 15.00, "menu_item_description": "Fresh fish seasoned and grilled to perfection, served with lemon and herbs."},
    {"name": "Lemon Dessert", "price": 5.50, "menu_item_description": "A light and tangy lemon-flavored dessert to finish your meal."},
]

for item in menu_items:
    obj, created = Menu.objects.get_or_create(
        name=item["name"],
        defaults={
            "price": item["price"],
            "menu_item_description": item["menu_item_description"],
        }
    )
    if created:
        print(f"Created: {obj.name}")
    else:
        print(f"Skipped (already exists): {obj.name}")

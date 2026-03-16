from django.core.management.base import BaseCommand
from django.db import transaction
from users.models import UserProfile
from restaurants.models import Restaurant, MenuItem
from orders.models import Order
import random
from decimal import Decimal

class Command(BaseCommand):
    help = 'Seed the database with sample data for BiteRight application'

    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write('Clearing existing data...')
            Order.objects.all().delete()
            MenuItem.objects.all().delete()
            Restaurant.objects.all().delete()
            UserProfile.objects.all().delete()

            self.stdout.write('Creating sample users...')
            self.create_users()
            
            self.stdout.write('Creating restaurants...')
            self.create_restaurants()
            
            self.stdout.write('Creating menu items...')
            self.create_menu_items()
            
            self.stdout.write('Creating sample orders...')
            self.create_orders()

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))

    def create_users(self):
        users_data = [
            {
                'name': 'John Doe',
                'email': 'john.doe@email.com',
                'allergies': 'peanuts, shellfish',
                'diet_preferences': 'vegetarian, gluten-free'
            },
            {
                'name': 'Jane Smith',
                'email': 'jane.smith@email.com',
                'allergies': 'dairy, nuts',
                'diet_preferences': 'vegan'
            },
            {
                'name': 'Mike Johnson',
                'email': 'mike.johnson@email.com',
                'allergies': '',
                'diet_preferences': 'keto, high-protein'
            },
            {
                'name': 'Sarah Williams',
                'email': 'sarah.williams@email.com',
                'allergies': 'soy, wheat',
                'diet_preferences': 'paleo'
            },
            {
                'name': 'David Brown',
                'email': 'david.brown@email.com',
                'allergies': 'eggs',
                'diet_preferences': 'low-carb'
            }
        ]

        for user_data in users_data:
            UserProfile.objects.create(**user_data)

    def create_restaurants(self):
        restaurants_data = [
            {
                'name': 'Spice Garden',
                'image_url': 'https://images.unsplash.com/photo-1589302168068-964664d93dc0?w=400&h=300&fit=crop&crop=center',
                'supports_customization': True
            },
            {
                'name': 'Green Bowl Cafe',
                'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop&crop=center',
                'supports_customization': True
            },
            {
                'name': 'Pizza Paradise',
                'image_url': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400&h=300&fit=crop&crop=center',
                'supports_customization': True
            },
            {
                'name': 'Sushi Master',
                'image_url': 'https://images.unsplash.com/photo-1579584425555-c3ce17fd4351?w=400&h=300&fit=crop&crop=center',
                'supports_customization': False
            },
            {
                'name': 'Burger Joint',
                'image_url': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400&h=300&fit=crop&crop=center',
                'supports_customization': True
            }
        ]

        for restaurant_data in restaurants_data:
            Restaurant.objects.create(**restaurant_data)

    def create_menu_items(self):
        restaurants = Restaurant.objects.all()
        
        menu_items_data = [
            # Spice Garden items
            {
                'restaurant': restaurants[0],  # Spice Garden
                'items': [
                    {'name': 'Spicy Biryani', 'price': 12.99, 'diet_tags': 'gluten-free, dairy-free', 'mood_tags': 'spicy', 'ingredients': 'basmati rice, chicken, spices, onions, tomatoes, yogurt'},
                    {'name': 'Paneer Butter Masala', 'price': 10.99, 'diet_tags': 'vegetarian, gluten-free', 'mood_tags': 'comfort', 'ingredients': 'paneer, butter, cream, tomatoes, spices'},
                    {'name': 'Chicken Tikka', 'price': 11.99, 'diet_tags': 'high-protein, gluten-free', 'mood_tags': 'spicy', 'ingredients': 'chicken, yogurt, spices, lemon juice'},
                    {'name': 'Vegetable Curry', 'price': 9.99, 'diet_tags': 'vegan, gluten-free', 'mood_tags': 'healthy', 'ingredients': 'mixed vegetables, coconut milk, spices, herbs'},
                ]
            },
            # Green Bowl Cafe items
            {
                'restaurant': restaurants[1],  # Green Bowl Cafe
                'items': [
                    {'name': 'Quinoa Buddha Bowl', 'price': 11.99, 'diet_tags': 'vegan, gluten-free, high-protein', 'mood_tags': 'healthy', 'ingredients': 'quinoa, chickpeas, avocado, kale, tahini, vegetables'},
                    {'name': 'Mediterranean Bowl', 'price': 10.99, 'diet_tags': 'vegetarian, gluten-free', 'mood_tags': 'healthy', 'ingredients': 'hummus, falafel, cucumber, tomatoes, olives, feta'},
                    {'name': 'Chicken Salad', 'price': 9.99, 'diet_tags': 'high-protein, low-carb', 'mood_tags': 'healthy', 'ingredients': 'grilled chicken, mixed greens, olive oil, lemon, vegetables'},
                    {'name': 'Veggie Wrap', 'price': 8.99, 'diet_tags': 'vegetarian', 'mood_tags': 'healthy', 'ingredients': 'whole wheat wrap, hummus, vegetables, sprouts'},
                ]
            },
            # Pizza Paradise items
            {
                'restaurant': restaurants[2],  # Pizza Paradise
                'items': [
                    {'name': 'Cheese Pizza', 'price': 12.99, 'diet_tags': 'vegetarian', 'mood_tags': 'comfort, cheat', 'ingredients': 'dough, mozzarella, tomato sauce, basil'},
                    {'name': 'Loaded Nachos', 'price': 10.99, 'diet_tags': 'vegetarian', 'mood_tags': 'cheat, late-night', 'ingredients': 'tortilla chips, cheese, jalapenos, sour cream, guacamole'},
                    {'name': 'Pepperoni Pizza', 'price': 14.99, 'diet_tags': 'high-protein', 'mood_tags': 'cheat, comfort', 'ingredients': 'dough, mozzarella, pepperoni, tomato sauce'},
                    {'name': 'Veggie Pizza', 'price': 13.99, 'diet_tags': 'vegetarian', 'mood_tags': 'healthy', 'ingredients': 'dough, mozzarella, bell peppers, mushrooms, onions, olives'},
                ]
            },
            # Sushi Master items
            {
                'restaurant': restaurants[3],  # Sushi Master
                'items': [
                    {'name': 'Salmon Roll', 'price': 15.99, 'diet_tags': 'high-protein, gluten-free', 'mood_tags': 'healthy', 'ingredients': 'salmon, rice, nori, cucumber, wasabi'},
                    {'name': 'California Roll', 'price': 12.99, 'diet_tags': 'gluten-free', 'mood_tags': 'healthy', 'ingredients': 'crab, avocado, cucumber, rice, nori'},
                    {'name': 'Tuna Nigiri', 'price': 18.99, 'diet_tags': 'high-protein, gluten-free', 'mood_tags': 'healthy', 'ingredients': 'tuna, rice, nori, soy sauce, wasabi'},
                    {'name': 'Vegetable Roll', 'price': 10.99, 'diet_tags': 'vegan, gluten-free', 'mood_tags': 'healthy', 'ingredients': 'avocado, cucumber, carrot, rice, nori'},
                ]
            },
            # Burger Joint items
            {
                'restaurant': restaurants[4],  # Burger Joint
                'items': [
                    {'name': 'Classic Burger', 'price': 11.99, 'diet_tags': 'high-protein', 'mood_tags': 'comfort, cheat', 'ingredients': 'beef patty, bun, lettuce, tomato, onion, cheese'},
                    {'name': 'Chicken Burger', 'price': 10.99, 'diet_tags': 'high-protein', 'mood_tags': 'comfort', 'ingredients': 'chicken patty, bun, lettuce, tomato, mayo'},
                    {'name': 'Veggie Burger', 'price': 9.99, 'diet_tags': 'vegetarian', 'mood_tags': 'healthy', 'ingredients': 'veggie patty, bun, lettuce, tomato, onion'},
                    {'name': 'Fish Burger', 'price': 12.99, 'diet_tags': 'high-protein', 'mood_tags': 'healthy', 'ingredients': 'fish fillet, bun, lettuce, tartar sauce, lemon'},
                ]
            }
        ]

        for restaurant_data in menu_items_data:
            restaurant = restaurant_data['restaurant']
            for item_data in restaurant_data['items']:
                MenuItem.objects.create(
                    restaurant=restaurant,
                    **item_data
                )

    def create_orders(self):
        users = list(UserProfile.objects.all())
        menu_items = list(MenuItem.objects.all())

        # Make sure we have enough menu items before creating orders
        if len(menu_items) < 23:
            self.stdout.write(self.style.WARNING(f'Only {len(menu_items)} menu items available, skipping order creation'))
            return

        orders_data = [
            {
                'user': users[0],  # John Doe
                'items': [
                    {'menu_item': menu_items[0], 'quantity': 2},  # Spicy Biryani
                    {'menu_item': menu_items[1], 'quantity': 1},  # Paneer Butter Masala
                ],
                'split_details': 'No split'
            },
            {
                'user': users[1],  # Jane Smith
                'items': [
                    {'menu_item': menu_items[4], 'quantity': 1},  # Quinoa Buddha Bowl
                    {'menu_item': menu_items[5], 'quantity': 1},  # Mediterranean Bowl
                ],
                'split_details': 'Split with Sarah Williams'
            },
            {
                'user': users[2],  # Mike Johnson
                'items': [
                    {'menu_item': menu_items[8], 'quantity': 1},  # Cheese Pizza
                    {'menu_item': menu_items[9], 'quantity': 1},  # Loaded Nachos
                ],
                'split_details': 'No split'
            },
            {
                'user': users[3],  # Sarah Williams
                'items': [
                    {'menu_item': menu_items[12], 'quantity': 2},  # Salmon Roll
                    {'menu_item': menu_items[13], 'quantity': 1},  # California Roll
                ],
                'split_details': 'Split with Jane Smith'
            },
            {
                'user': users[4],  # David Brown
                'items': [
                    {'menu_item': menu_items[16], 'quantity': 1},  # Classic Burger
                    {'menu_item': menu_items[18], 'quantity': 1},  # Veggie Burger
                ],
                'split_details': 'No split'
            }
        ]

        for order_data in orders_data:
            total_amount = sum(item['menu_item'].price * item['quantity'] for item in order_data['items'])
            
            Order.objects.create(
                user=order_data['user'],
                total_amount=float(total_amount),
                split_details=order_data['split_details']
            )

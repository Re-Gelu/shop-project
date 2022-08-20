from Shop.models import *
from django.db import models
from art import tprint
import random


def DB_AUTO_FILL(amount, model):
    match model:
        case "Categories":
            print("[+] Model exists...")

            for i in range(amount):
                Categories.objects.update_or_create(name=f"Категория №{i}")

        case "Subcategories":
            print("[+] Model exists...")
            
            for i in range(amount):
                Subcategories.objects.update_or_create(name=f"Подкатегория №{i}")
                
        case "Products":
            print("[+] Model exists...")

            for i in range(amount):
                Products.objects.create(
                    name=f"Товар №{i}",
                    price=69,
                    image= "product_images/WIP.png",
                    information = "Товар заглушка",
                    subcategory=random.randint(1, Subcategories.objects.creation_counter)
                )

if __name__ == '__main__':
    tprint("DB auto fill", font="Slant")
    amount = int(input("Кол-во записей: "))
    model = input("Таблица: ")
    DB_AUTO_FILL(amount, model)

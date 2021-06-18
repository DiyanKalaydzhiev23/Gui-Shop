from canvas import *
from helpers import clean_screen
from PIL import Image, ImageTk
from json import load, dump
from collections import deque


def display_products():
    clean_screen()

    frame.create_text(150, 50, text="Blue Shirt", font=("Comic Sans MS", 15))
    frame.create_text(350, 50, text="Black Jeans", font=("Comic Sans MS", 15))
    frame.create_text(550, 50, text="Shoes", font=("Comic Sans MS", 15))

    frame.create_image(150, 150, image=blue_t_shirt_img)
    frame.create_image(350, 150, image=black_jeans_img)
    frame.create_image(550, 150, image=shoes_img)

    display_in_stock()


def display_in_stock():
    global info

    with open("db/product_in_stock.json", "r") as stock:
        info = load(stock)

    x = 150
    for el in info:
        count = info[el]
        button = buttons.popleft()

        if count > 0:
            color = "green"
            text = f"In stock: {count}"
            frame.create_window(x, 260, window=button)
        else:
            color = "red"
            text = "Out of Stock"

        buttons.append(button)
        frame.create_text(x, 220, text=text, font=("Comic Sans MS", 12), fill=color)
        x += 200


def buy_products(product):
    global info

    for el in info:
        if product == el:
            info[el] -= 1

    with open("db/product_in_stock.json", "w") as stock:
        dump(info, stock)

    clean_screen()
    display_products()


blue_t_shirt_img = ImageTk.PhotoImage(Image.open("images/blue_t_shirt.png"))
black_jeans_img = ImageTk.PhotoImage(Image.open("images/black_jeans.png"))
shoes_img = ImageTk.PhotoImage(Image.open("images/shoes.png"))

buy_t_shirt_btn = Button(root, text="Buy", command=lambda: buy_products("blue t-shirt"),
                         font=("Comic Sans MS", 12), width=5, bg="green", fg="white")
buy_jeans_btn = Button(root, text="Buy", command=lambda: buy_products("black jeans"),
                       font=("Comic Sans MS", 12), width=5, bg="green", fg="white")
buy_shoes_btn = Button(root, text="Buy", command=lambda: buy_products("shoes"),
                       font=("Comic Sans MS", 12), width=5, bg="green", fg="white")

buttons = deque([buy_t_shirt_btn, buy_jeans_btn, buy_shoes_btn])
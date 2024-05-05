import colorgram
import random
import tkinter as tk
from tkinter import filedialog
import turtle as t

number_of_dots = 100

# turtle settings
t.speed("fastest")
t.penup()
t.hideturtle()


def select_file():
    """
    Select the image file from system
    :return: The image path if selected, None otherwise
    """
    file_path = filedialog.askopenfilename(filetypes=[("Image files", ["*.jpg", "*.jpeg", "*.png"])])
    if file_path:
        print("Selected file:", file_path)
        return file_path
    else:
        print("No file selected.")
        return None


def get_colors_from_image(image_path):
    """
    Get the colors from the image
    :param image_path: the path of image if selected
    :return: the list of colors in form of tuples of rgb
    """
    rgb_colors = []
    if image_path is None:
        print("Selecting the default image")
    path = image_path if image_path is not None else "default.jpg"
    colors = colorgram.extract(path, 30)
    for color in colors:
        rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
    return rgb_colors


def draw_hirst_painting(colors):
    """
    Draw the hirst painting using turtle
    :param colors: the list of colors used for drawing painting
    """
    t.setheading(225)
    t.forward(300)
    t.setheading(0)
    for dot_count in range(1, number_of_dots + 1):
        t.dot(20, random.choice(colors))
        t.forward(50)
        if dot_count % 10 == 0:
            t.setheading(90)
            t.forward(50)
            t.setheading(180)
            t.forward(500)
            t.setheading(0)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file = select_file()
    all_colors = get_colors_from_image(file)
    t.colormode(255)
    screen = t.Screen()
    draw_hirst_painting(all_colors)
    screen.exitonclick()
    exit(0)

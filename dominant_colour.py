import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def dominant_colour():
    img = Image.open("sunset2.jpg").convert("RGB")
    img_array = np.array(img)
    colours = img_array.reshape(-1, 3)
    return colours

colours = dominant_colour()


def count_occurences(colours):
    value, counts = np.unique(colours, return_counts=True, axis=0)
    return value, counts

values, counts = count_occurences(colours)


def top5(values, counts):
    sorted_indices = np.argsort(counts)
    top_5_indices = sorted_indices[-5:][::-1]
    top_5_colors = values[top_5_indices]
    top_5_counts = counts[top_5_indices]
    return top_5_colors, top_5_counts

top_colors, top_counts = top5(values, counts)

print("Top 5 Colors (RGB): \n", top_colors)
print("Their pixel counts: \n", top_counts)


def plot_top_colors(top_colors, top_counts):
    plt.figure(figsize=(8, 8))
    labels = []
    for color in top_colors:
        text = f"RGB: ({color[0]}, {color[1]}, {color[2]})"
        labels.append(text)
    chart_colors = [tuple(color / 255.0) for color in top_colors]
    plt.pie(
        top_counts,
        labels = labels,
        colors = chart_colors,
        autopct = "%1.1f%%",
        explode = [0.05,0,0,0,0],
        shadow = True,
        wedgeprops={"edgecolor": "black", "linewidth": 1.5}
    )

    plt.title("Top 5 Dominant Colors in the Image")
    plt.axis("equal")
    plt.show()



plot_top_colors(top_colors, top_counts)
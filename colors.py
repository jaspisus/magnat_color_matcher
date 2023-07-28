import json

def rgb_distance(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return ((r2 - r1) ** 2 + (g2 - g1) ** 2 + (b2 - b1) ** 2) ** 0.5

# The given RGB color
target_color = (188,101,135)

# JSON data with color codes as keys and background colors as values
json_data = open("colors.json")

# Parse the JSON data
color_data = json.load(json_data)

# Convert the color strings to RGB tuples
colors_rgb = {key: tuple(map(int, value[4:-1].split(','))) for key, value in color_data.items()}

# Find the most similar color
min_distance = float('inf')
most_similar_color = None

for color_code, color_rgb in colors_rgb.items():
    distance = rgb_distance(target_color, color_rgb)
    if distance < min_distance:
        min_distance = distance
        most_similar_color = color_code

print("Most similar color code:", most_similar_color)
print("Most similar color:", colors_rgb[most_similar_color])



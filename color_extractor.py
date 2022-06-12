import colorgram

def extract_colors(color_types):
    colors = colorgram.extract('dots.jpeg', color_types)
    for color_type in range(color_types):
        r = colors[color_type].rgb.r
        g = colors[color_type].rgb.g
        b = colors[color_type].rgb.b
        new_color = (r, g, b)
        final_colors.append(new_color)

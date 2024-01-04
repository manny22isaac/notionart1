from fileinput import filename
import matplotlib.pyplot as plt
import numpy as np
from math import ceil, sqrt
import matplotlib.colors as mcolors

def is_prime(n):

    if n <= 1:
        return False
    if n == 2:
        return True

    divisor_candidates = list(range(ceil(sqrt(n)+1)))
    for count in divisor_candidates[2:]:
        if n % count == 0:
            return False
    
    return True

def get_color(gap, max_gap):
    prime = mcolors.to_rgba('#0000FF')
    
    
    far_from_prime = mcolors.to_rgb('#2E8B57')
    
    
    blend_ratio = min(gap / max_gap, 1)
    
    
    blended_color = [
        prime[i] * (1 - blend_ratio) + far_from_prime[i] * blend_ratio
        for i in range(3)
    ]

    return mcolors.to_hex(blended_color)

def display_colored_squares(grid_height, grid_width, max_gap=10, filename='grid_image.png'):
    fig, ax = plt.subplots(figsize=(20, 5))
    last_prime = 0
    paired = False

    for i in range(grid_height):
        for j in range(grid_width):
            grid_position = i * grid_width + j + 1
            if is_prime(grid_position):
                if grid_position - last_prime == 2:
                    paired = True
                last_prime = grid_position
            gap_since_last_prime = grid_position - last_prime

            if grid_position == 1:
                color = 'yellow'
            elif paired == True:
                color = '#C2B280'
                paired = False
            elif gap_since_last_prime == 0:
                color = '#0000FF'
                if is_prime(grid_position + 2):
                    color = '#C2B280'
            else:
                color = get_color(gap_since_last_prime, max_gap)

            ax.add_patch(plt.Rectangle((j, i), 1, 1, color=color))

    ax.set_xlim(0, grid_width)
    ax.set_ylim(0, grid_height)
    ax.set_aspect('equal', adjustable='box')
    plt.xticks([])
    plt.yticks([])
    plt.savefig(filename, bbox_inches='tight')
    plt.show()


grid_height = 40
grid_width = 30

display_colored_squares(grid_height, grid_width)


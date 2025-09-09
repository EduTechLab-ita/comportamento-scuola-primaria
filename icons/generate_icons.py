#!/usr/bin/env python3
"""
Generate PNG icons from SVG template for PWA app
Creates all required sizes for school behavior evaluation app
"""

import os
from PIL import Image, ImageDraw
import io

def create_icon_png(size, output_path):
    """Create a PNG icon with the specified size"""
    # Create image with transparent background initially
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Calculate scaling factor and margins
    margin = size * 0.2  # 20% margin for maskable icons
    content_size = size - (2 * margin)
    
    # Background rounded rectangle
    corner_radius = size * 0.18  # Approximately 18% of size for rounded corners
    draw.rounded_rectangle(
        [0, 0, size, size], 
        radius=corner_radius, 
        fill='#1e88e5'
    )
    
    # Scale everything based on size
    scale = content_size / 512
    
    # Document background (white rectangle)
    doc_margin = margin * 1.5
    doc_width = content_size * 0.7
    doc_height = content_size * 0.8
    doc_x = (size - doc_width) // 2
    doc_y = doc_margin
    
    draw.rounded_rectangle(
        [doc_x, doc_y, doc_x + doc_width, doc_y + doc_height],
        radius=max(2, int(size * 0.04)),
        fill='white'
    )
    
    # Document content lines (simplified for small sizes)
    if size >= 128:
        line_height = max(2, int(size * 0.008))
        line_spacing = max(8, int(size * 0.06))
        line_start_x = doc_x + (doc_width * 0.15)
        line_end_x = doc_x + (doc_width * 0.85)
        
        # Header line
        header_y = doc_y + (doc_height * 0.2)
        draw.rectangle(
            [line_start_x, header_y, line_end_x, header_y + line_height],
            fill='#e0e0e0'
        )
        
        # Content lines
        for i in range(3):
            line_y = header_y + (i + 1) * line_spacing * 1.5
            line_width = (line_end_x - line_start_x) * (0.7 + i * 0.1)
            draw.rectangle(
                [line_start_x, line_y, line_start_x + line_width, line_y + line_height],
                fill='#e0e0e0'
            )
    
    # Stars (rating indicators) - only show if size is large enough
    if size >= 96:
        star_size = max(6, int(size * 0.025))
        star_x = doc_x + doc_width - (star_size * 2)
        star_colors = ['#4caf50', '#ffb300', '#4caf50']
        
        for i, color in enumerate(star_colors):
            if size >= 128:  # Only show multiple stars for larger sizes
                star_y = doc_y + (doc_height * 0.35) + (i * star_size * 2)
                draw_star(draw, star_x, star_y, star_size, color)
            elif i == 0:  # Show only one star for smaller sizes
                star_y = doc_y + (doc_height * 0.4)
                draw_star(draw, star_x, star_y, star_size, color)
    
    # Simple student figure (only for larger sizes)
    if size >= 144:
        figure_scale = size / 512
        figure_x = size // 2
        figure_y = doc_y + (doc_height * 0.75)
        
        # Head
        head_radius = max(3, int(8 * figure_scale))
        draw.ellipse(
            [figure_x - head_radius, figure_y - head_radius, 
             figure_x + head_radius, figure_y + head_radius],
            fill='#616161'
        )
        
        # Body
        body_width = max(4, int(12 * figure_scale))
        body_height = max(6, int(16 * figure_scale))
        draw.rounded_rectangle(
            [figure_x - body_width//2, figure_y + head_radius, 
             figure_x + body_width//2, figure_y + head_radius + body_height],
            radius=max(1, int(2 * figure_scale)),
            fill='#616161'
        )
    
    # Academic cap decoration (corner) - only for larger sizes
    if size >= 192:
        cap_size = max(8, int(size * 0.06))
        cap_x = size - cap_size * 2
        cap_y = cap_size
        
        # Simple triangle for graduation cap
        draw.polygon(
            [(cap_x, cap_y + cap_size//2), 
             (cap_x + cap_size, cap_y), 
             (cap_x + cap_size, cap_y + cap_size)],
            fill=(255, 255, 255, 80)  # Semi-transparent white
        )
    
    # Save the image
    img.save(output_path, 'PNG', optimize=True)
    print(f"Generated: {output_path} ({size}x{size})")

def draw_star(draw, x, y, size, color):
    """Draw a simple star shape"""
    # Simplified star for small sizes
    if size < 10:
        # Draw as a small diamond/square
        draw.rectangle([x-size//2, y-size//2, x+size//2, y+size//2], fill=color)
    else:
        # Draw a more detailed star
        points = []
        import math
        for i in range(5):
            angle = i * 2 * math.pi / 5 - math.pi / 2
            outer_x = x + size * math.cos(angle)
            outer_y = y + size * math.sin(angle)
            points.append((outer_x, outer_y))
            
            angle += math.pi / 5
            inner_x = x + size * 0.4 * math.cos(angle)
            inner_y = y + size * 0.4 * math.sin(angle)
            points.append((inner_x, inner_y))
        
        draw.polygon(points, fill=color)

def main():
    """Generate all required PNG sizes"""
    sizes = [72, 96, 128, 144, 152, 192, 384, 512]
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    print("Generating PWA icons for 'Generatore Valutazioni Comportamento Scuola Primaria'...")
    print("=" * 70)
    
    for size in sizes:
        filename = f"icon-{size}x{size}.png"
        output_path = os.path.join(base_path, filename)
        create_icon_png(size, output_path)
    
    print("=" * 70)
    print(f"Successfully generated {len(sizes)} icon files!")
    print("\nFiles created:")
    for size in sizes:
        filename = f"icon-{size}x{size}.png"
        print(f"  - {filename}")
    
    print(f"\nLocation: {base_path}")
    print("\nIcons are optimized for:")
    print("  - PWA app icons")
    print("  - Maskable icon compatibility")
    print("  - Professional school/education theme")
    print("  - Various device screen densities")

if __name__ == "__main__":
    main()
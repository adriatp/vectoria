from PIL import Image
import numpy as np
import svgwrite
from .arg_parse import *
from .shared_variables import *

args = parse_arguments()

def export_to_svg(vectors):
    dwg = svgwrite.Drawing(args.output_path, profile='tiny')
    for vector in vectors:
        dwg.add(dwg.line(vector[0], vector[1], stroke=svgwrite.rgb(10, 10, 16, '%')))
    dwg.save()

def image_to_vector(image_array):
    vectors = []
    # Get the dimensions of the image
    height, width, _ = image_array.shape
    
    # Iterate over each pixel in the image
    for y in range(height):
        for x in range(width):
            # Get the RGB values of the pixel
            r, g, b = image_array[y, x]
            
            # Create a vector with the pixel coordinates and RGB values
            vector = [(x, y), (r, g, b)]
            
            # Append the vector to the list of vectors
            vectors.append(vector)
    
    return vectors

def main():
    # Open the image from args
    try:
        image = Image.open(args.image_path)
        image_array = np.array(image)
        vectors = image_to_vector(image_array)
        export_to_svg(vectors)
    except IOError:
        print(f"Error: Can't open image at {args.image_path}. Please check the file path and try again.")
        sys.exit(1)


if __name__ == "__main__":
    main()
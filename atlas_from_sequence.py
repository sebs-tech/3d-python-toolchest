from PIL import Image
import os
import math

def create_atlas_from_sequence(input_folder, output_path, grid_width, grid_height):
    # List of all image file paths in the input folder
    image_files = sorted([os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith(('png', 'jpg', 'jpeg'))])

    # Open the first image to get dimensions
    if not image_files:
        print("No images found in the specified folder.")
        return

    first_image = Image.open(image_files[0])
    img_width, img_height = first_image.size

    # Determine atlas dimensions based on grid and image size
    atlas_width = grid_width * img_width
    atlas_height = grid_height * img_height

    # Create a blank canvas for the atlas
    atlas_image = Image.new('RGBA', (atlas_width, atlas_height))

    # Paste each image into the atlas
    for index, image_file in enumerate(image_files):
        img = Image.open(image_file)
        row = index // grid_width
        col = index % grid_width
        x = col * img_width
        y = row * img_height

        atlas_image.paste(img, (x, y))

    # Save the atlas image
    atlas_image.save(output_path)
    print(f"Atlas created and saved as '{output_path}'.")

# Parameters
input_folder = "/home/seb/ref_from_web"     # Folder with your image sequence
output_path = "/home/seb/ref_from_web/atlas.png"      # Output path for the atlas image
grid_width = 3                               # Number of images in each row of the atlas
grid_height = 3                              # Number of images in each column of the atlas

create_atlas_from_sequence(input_folder, output_path, grid_width, grid_height)

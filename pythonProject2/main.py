import urllib.request
import os
import io
from PIL import Image

# Define the URL pattern
url_pattern = "https://opac.biblioteca.ase.ro/fullTextPageService.svc?c=jttar92d684ba31f98dfd2b6008bac26d2c12&e=-{}.png"

# Specify the range of pages
start_page = 0
end_page = 229

# Specify the directory to save the images
save_directory = "downloaded_images"

# Create the directory if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

# Loop through the pages and download the images
for page_number in range(start_page, end_page + 1):
    # Construct the URL for the current page
    current_url = url_pattern.format(page_number)

    try:
        # Retrieve the image data
        image_data = urllib.request.urlopen(current_url).read()

        # Open the image using Pillow
        image = Image.open(io.BytesIO(image_data))

        # Save the image to the specified directory
        image.save(os.path.join(save_directory, f"page_{page_number}.png"))
        print(f"Page {page_number} downloaded successfully.")
    except Exception as e:
        print(f"Failed to download page {page_number}. Error: {e}")

print("All pages downloaded.")

import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

# Replace this URL with the direct link to the image you want to download
image_url = "https://imgs.xkcd.com/comics/curve_fitting.png"

try:
    # Step 1: Download the image data from the URL
    response = requests.get(image_url)
    response.raise_for_status()  # This will raise an HTTPError for bad responses (4xx or 5xx)

    # Step 2: Read the image data from the response content
    image_data = BytesIO(response.content)

    # Step 3: Open the image using Pillow (PIL)
    image = Image.open(image_data)

    # Step 4: Display the image
    # This will open a new window showing the image
    print("Displaying the image...")
    # image.show()
    plt.imshow(image)
    plt.show()
    print("Image displayed successfully.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the image: {e}")
except IOError as e:
    print(f"Error processing the image file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

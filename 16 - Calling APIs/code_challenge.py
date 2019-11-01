# Challenge #1
# Create an Azure Custom Vision Service
# Analyze an image and return the JSON describing the image.
# call_api.py is a completed solution, but it will not run unless
# you do the following:
#   Create a Custom Vision Service in Azure
#   Update the Key
#   Update the address of your service
#   Update the image file and location
import requests
import json
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# Add your Computer Vision subscription key and endpoint
# to your environment variables.
subscription_key = '5f5f2cc28dc44fa3a4a453ef65eea1a2'
endpoint = 'https://westus.api.cognitive.microsoft.com/'


analyze_url = endpoint + "vision/v2.1/analyze"
# Set image_path to the local path of an image that you want to analyze.
image_path = "./TestImages/FeedingKangaroo.jpg"

# Read the image into a byte array
image_data = open(image_path, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': subscription_key,
           'Content-Type': 'application/octet-stream'}
params = {'visualFeatures': 'Categories,Description,Color'}
response = requests.post(
    analyze_url, headers=headers, params=params, data=image_data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image.
# The most
# relevant caption for the image is obtained from the 'description' property.
analysis = response.json()
print(analysis)
image_caption = analysis["description"]["captions"][0]["text"].capitalize()

# Display the image and overlay it with the caption.
image = Image.open(BytesIO(image_data))
plt.imshow(image)
plt.axis("off")
_ = plt.title(image_caption, size="x-large", y=-0.1)


# Bonus Challenge
# Your skills are growing, it's time to start trying to figure things out on your own
# based on documentation. You have already called one function of the Computer Vision Service
# Now try calling another
# Instead of calling the analyze method of the service, try calling the OCR method
# Here is some helpful documentation
# https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/concept-recognizing-text#ocr-optical-character-recognition-api
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fc
# Use the documentation to figure out
#    The correct function name for the address
#    The parameters you need to pass the function
#    The HTTP Headers required
# Pass in an image containing text
# The JSON returned will contain the string of text in the image
# Good luck!

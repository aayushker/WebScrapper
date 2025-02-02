import requests
from bs4 import BeautifulSoup
import os

url = "https://github.com/aayushker"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Extract text
text = soup.get_text()
text = ' '.join(text.split())
text = text.replace(".", "\n")

# Use the URL variable to create a filename
os.makedirs("Content", exist_ok=True)
filename = os.path.join("Content", url.split("//")[-1].replace("/", "_") + ".txt")
with open(filename, "w") as file:
    file.write(text)

# Extract images
images = [img["src"] for img in soup.find_all("img") if "src" in img.attrs]

# Download images
os.makedirs("images", exist_ok=True)
for i, img_url in enumerate(images):
    if img_url.startswith("http"):
        img_data = requests.get(img_url).content
        with open(f"images/image_{i}.jpg", "wb") as img_file:
            img_file.write(img_data)

print("Extracted Text:", text[:500])  # Print first 500 characters
print("Image URLs:", images)

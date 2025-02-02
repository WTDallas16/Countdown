import os

# Define the folder containing the photos
PHOTO_FOLDER = "Photos"
JS_FILE = "images.js"

def generate_js():
    # Get all image filenames (JPG, JPEG, PNG)
    image_extensions = (".jpg", ".jpeg", ".JPG", ".png")
    images = [f"'{PHOTO_FOLDER}/{file}'" for file in os.listdir(PHOTO_FOLDER) if file.lower().endswith(image_extensions)]

    # Create JavaScript file content
    js_content = f"const images = [{', '.join(images)}];\n"
    
    # Save to images.js
    with open(JS_FILE, "w") as js_file:
        js_file.write(js_content)

    print(f"✅ {JS_FILE} updated with {len(images)} images.")

# Run script
if __name__ == "__main__":
    generate_js()

import os

# Folder containing the photos (Update this to the correct folder path)
folder_path = "photos"  # Change this if necessary

# Get all image files in the folder
image_extensions = (".jpg", ".jpeg", ".JPG", ".png")
images = [f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]

# Sort files to maintain order
images.sort()

# Rename images
for index, filename in enumerate(images, start=1):
    ext = os.path.splitext(filename)[1]  # Get file extension
    new_name = f"US{index}{ext}"  # Rename format: US<number>.ext
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)

    os.rename(old_path, new_path)
    print(f"Renamed: {filename} → {new_name}")

print("✅ All images renamed successfully!")

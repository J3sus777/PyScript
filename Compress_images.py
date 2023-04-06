from PIL import Image
import os

def compress_images(input_folder, max_size):
    output_folder = os.path.join(input_folder, "compressed_images")
    os.makedirs(output_folder, exist_ok=True)
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                input_path = os.path.join(root, file)
                with Image.open(input_path) as img:
                   
                    #data = list(img.getdata())
                    #img_without_metadata = Image.new(img.mode, img.size)
                    #img_without_metadata.putdata(data)
                    
                    
                    img.thumbnail((max_size, max_size))


                    output_path = os.path.join(output_folder, os.path.splitext(file)[0])
                    if file.endswith(".jpg"):
                        img.save(output_path + '.jpg', format='JPEG', optimize=True, quality=85)
                    elif file.endswith(".png"):
                        img.save(output_path + '.png', format='PNG', optimize=True, quality=85)


input_folder = input('path: ') 
max_size = 1500 
compress_images(input_folder, max_size)
print("SAVE")


from PIL import Image
import random

def truncate_image(input_image, output_image, num_bytes_to_truncate=None, add_noise=False):
    try:
        with Image.open(input_image) as img:
            img_data = img.tobytes()
            
            if num_bytes_to_truncate is not None:
                if num_bytes_to_truncate < len(img_data):
                    img_data = img_data[:num_bytes_to_truncate]
            elif add_noise:
                img_data = bytearray(img_data)
                for i in range(len(img_data)):
                    random_noise = random.randint(0, 255)  # Generate a random value between 0 and 255
                    img_data[i] = img_data[i] ^ random_noise  # Add noise by flipping bits

            truncated_img = Image.frombytes(img.mode, img.size, bytes(img_data))
            truncated_img.save(output_image)
    except Exception as e:
        print(f"Error: {e}")

name = "b88.png"
path = f"./examples/base/{name}"
path_out_invalid = f"./examples/invalid/1_{name}"

# Create a corrupted image with added noise
truncate_image(path, path_out_invalid, add_noise=True)


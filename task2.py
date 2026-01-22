from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )
    img.save("encrypted.png")
    print("Image encrypted and saved as encrypted.png")

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )
    img.save("decrypted.png")
    print("Image decrypted and saved as decrypted.png")

try:
    choice = input("Type encrypt or decrypt: ").lower()
    print(f"Choice entered: {choice}")

    key = int(input("Enter key value: "))
    print(f"Key entered: {key}")

    if choice == "encrypt":
        encrypt_image("input.png", key)
    elif choice == "decrypt":
        decrypt_image("encrypted.png", key)
    else:
        print("Invalid choice")

except Exception as e:
    print(f"Error occurred: {e}")

input("Press Enter to exit...")

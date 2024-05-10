from PIL import Image, ImageFilter
import asyncio
import time
import os
from concurrent.futures import ThreadPoolExecutor
from functools import wraps
def convert_to_grayscale(image):
    """Convierte la imagen a escala de grises."""
    return image.convert('L')

def apply_edge_detection(image):
    """Aplica detección de bordes a la imagen."""
    return image.filter(ImageFilter.FIND_EDGES)


def time_it(func):
    """Decorador que mide el tiempo de ejecución de una función."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds to run.")
        return result
    return wrapper

def parallelize_image_processing(function):
    """Decorador que paraleliza el procesamiento de imágenes."""
    @wraps(function)
    def wrapper(images):
        with ThreadPoolExecutor(max_workers=5) as executor:
            results = list(executor.map(function, images))
        return results
    return wrapper
@time_it
@parallelize_image_processing
def process_images(images):
    """Procesa una lista de imágenes aplicando las funciones de procesamiento."""
    processed_images = [convert_to_grayscale(img) for img in images]
    processed_images = [apply_edge_detection(img) for img in processed_images]
    return processed_images
async def main():
    folder_path = r'C:\Users\Vanesa Nelsy\Downloads\Evaluacion_5'
    images = []
    for i in range(5):
        image_path = os.path.join(folder_path, f'my_image_{i+1}.jpg')
        image = Image.open(image_path)
        images.append([image])
    processed_images = process_images(images)
    for i, processed_image_list in enumerate(processed_images):
        processed_image = processed_image_list[0]
        processed_image.save(os.path.join(folder_path , f'my_image_{i+1}_modificada.jpg'))

if __name__ == "__main__":
    asyncio.run(main())

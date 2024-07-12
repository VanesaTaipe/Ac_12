import cv2
import numpy as np
from multiprocessing import Pool

def apply_blur(segment):
    return cv2.GaussianBlur(segment, (15, 15), 0)

def parallel_image_processing(image_path):
    # Cargar la imagen
    image = cv2.imread(image_path)
    
    # Obtener las dimensiones de la imagen
    height, width, _ = image.shape
    
    # Dividir la imagen en segmentos 
    segments = np.array_split(image, 4, axis=1)
  
    # Crear un pool de procesos
    with Pool(processes=4) as pool:
        # Aplicar el filtro de desenfoque a cada segmento en paralelo
        blurred_segments = pool.map(apply_blur, segments)

    # Unir los segmentos procesados horizontalmente
    blurred_image = np.hstack(blurred_segments)
    
    # Guardar la imagen resultante
    cv2.imwrite('blurred_image.png', blurred_image)

# Llamar a la función con la ruta de la imagen
parallel_image_processing('images (3).png')

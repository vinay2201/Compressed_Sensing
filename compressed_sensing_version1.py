import numpy as np
import time

def read_image(filepath):
    start_time = time.time()
    with open(filepath, 'rb') as file:
        data = file.read()
    read_time = time.time() - start_time
    return np.frombuffer(data, dtype=np.uint8), read_time 

def create_sensing_matrix(M, N):
    start_time = time.time()
    Phi = np.random.randn(M, N)
    create_time = time.time() - start_time
    return Phi, create_time

def compressive_sensing(image, Phi):
    start_time = time.time()
    compressed_image = Phi @ image
    compress_time = time.time() - start_time
    print('compressed_image ',compressed_image[0])
    return compressed_image, compress_time

def scalar_quantization(y, step_size):
    start_time = time.time()
    quantized = np.round(y / step_size) * step_size
    quantize_time = time.time() - start_time
    print('quantized', quantized[0])
    return quantized, quantize_time


filepath = 'C:/Users/vinay/OneDrive/Pictures/Screenshots/jpg-vs-jpeg.jpg'
image, read_time = read_image(filepath)
image_size = len(image)
compression_ratio = 0.25
M = int(compression_ratio * image_size)
Phi, create_time = create_sensing_matrix(M, image_size)
print(image)
compressed_measurements, compress_time = compressive_sensing(image, Phi)
quantized_measurements, quantize_time = scalar_quantization(compressed_measurements, step_size=10)


print(f"Original data size: {len(image)/1024:.2f} KB")
print(f"Compressed data size: {len(quantized_measurements)/1024:.2f} KB")
print(f"Time taken to read image: {read_time:.2f} seconds")
print(f"Time to create sensing matrix: {create_time:.2f} seconds")
print(f"Time to compress data: {compress_time:.2f} seconds")
print(f"Time to quantize data: {quantize_time:.2f} seconds")

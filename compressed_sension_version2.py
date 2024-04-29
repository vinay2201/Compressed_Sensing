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
    return compressed_image, compress_time

def scalar_quantization(y, step_size):
    start_time = time.time()
    quantized = np.round(y / step_size) * step_size
    quantize_time = time.time() - start_time
    return quantized, quantize_time

def decode_quantized_measurements(quantized_measurements, Phi):
    start_time = time.time()
    Phi_pseudo_inv = np.linalg.pinv(Phi)
    reconstructed_image = Phi_pseudo_inv @ quantized_measurements
    decode_time = time.time() - start_time
    return reconstructed_image, decode_time

# Parameters
filepath = 'C:/Users/vinay/OneDrive/Pictures/Screenshots/jpg-vs-jpeg.jpg'
image, read_time = read_image(filepath)
image_size = len(image)
compression_ratio = 0.5
M = int(compression_ratio * image_size)

# Main process
Phi, create_time = create_sensing_matrix(M, image_size)
compressed_measurements, compress_time = compressive_sensing(image, Phi)
quantized_measurements, quantize_time = scalar_quantization(compressed_measurements, 10)

# Decoding process
reconstructed_image, decode_time = decode_quantized_measurements(quantized_measurements, Phi)

# Output the size and time
print(f"Original data size: {len(image)/1024:.2f} KB")
print(f"Compressed data size: {len(quantized_measurements)/1024:.2f} KB")
print(f"Decoded data size: {len(reconstructed_image)/1024:.2f} KB")
print(f"Time taken to read image: {read_time:.2f} seconds")
print(f"Time to create sensing matrix: {create_time:.2f} seconds")
print(f"Time to compress data: {compress_time:.2f} seconds")
print(f"Time to quantize data: {quantize_time:.2f} seconds")
print(f"Time to decode data: {decode_time:.2f} seconds")

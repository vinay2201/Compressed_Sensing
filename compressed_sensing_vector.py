import numpy as np
import time
from sklearn.cluster import KMeans

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

def vector_quantization(y, num_clusters):
    start_time = time.time()
    y = y.reshape(-1, 1)  # Reshape y for clustering, if y is a 1D array of measurements
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(y)
    quantized = kmeans.cluster_centers_[kmeans.labels_].flatten()  # Use labels to assign cluster centers
    quantize_time = time.time() - start_time
    print('quantized', quantized[:5])  # Print the first few quantized values
    return quantized, quantize_time

filepath = 'C:/Users/vinay/OneDrive/Pictures/Screenshots/jpg-vs-jpeg.jpg'
image, read_time = read_image(filepath)
image_size = len(image)
compression_ratio = 0.25
M = int(compression_ratio * image_size)
Phi, create_time = create_sensing_matrix(M, image_size)
compressed_measurements, compress_time = compressive_sensing(image, Phi)

# Assuming you want to use 10 clusters for the vector quantization
num_clusters = 10
quantized_measurements, quantize_time = vector_quantization(compressed_measurements, num_clusters)

print(f"Original data size: {len(image)/1024:.2f} KB")
print(f"Compressed data size: {len(quantized_measurements)/1024:.2f} KB")
print(f"Time taken to read image: {read_time:.2f} seconds")
print(f"Time to create sensing matrix: {create_time:.2f} seconds")
print(f"Time to compress data: {compress_time:.2f} seconds")
print(f"Time to quantize data: {quantize_time:.2f} seconds")
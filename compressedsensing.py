import numpy as np
import zlib
from PIL import Image

def generate_sensing_matrix(M, N):
    """ Generate a simple random sensing matrix with reduced memory footprint """
    return np.random.randn(M, N).astype(np.float32)

def compressive_sensing(image_vector, phi):
    """ Apply the sensing matrix to the image vector """
    return np.dot(phi, image_vector)

def quantize(measurements, step_size=1):
    """ Quantize measurements with a uniform quantizer """
    return np.round(measurements / step_size) * step_size

def entropy_encode(quantized_measurements):
    """ Use zlib for entropy encoding as a proxy for Huffman or arithmetic coding """
    data = quantized_measurements.astype(np.int16).tobytes()
    return zlib.compress(data)

def compress_image(image_path, M, step_size=1):
    # Load an image from file and convert to grayscale
    image = Image.open(image_path).convert('L')
    image_array = np.array(image)
    
    N = image_array.size
    phi = generate_sensing_matrix(M, N)
    measurements = compressive_sensing(image_array.flatten(), phi)
    quantized = quantize(measurements, step_size)
    encoded = entropy_encode(quantized)
    return encoded

# Example Usage
image_path = 'C:/Users/vinay/OneDrive/Pictures/Screenshots/jpg-vs-jpeg.jpg'  # Specify the path to your image file
compressed_data = compress_image(image_path, M=1000, step_size=5)

compressed_size_kb = len(compressed_data) / 1024  # Convert bytes to kilobytes
print(f"Compression complete. Compressed size: {compressed_size_kb:.2f} KB")

import numpy as np

def read_image(filepath):
    """Read raw image data from a file."""
    with open(filepath, 'rb') as file:
        data = file.read()
    return np.frombuffer(data, dtype=np.uint8)  # Reading directly as bytes

def create_sensing_matrix(M, N):
    """Create a random Gaussian sensing matrix."""
    return np.random.randn(M, N)

def compressive_sensing(chunks, Phi):
    """Apply the sensing matrix to chunks of the image (compressive sensing)."""
    compressed_data = []
    for chunk in chunks:
        compressed_data.append(Phi @ chunk)
    return np.concatenate(compressed_data)

def scalar_quantization(y, step_size):
    """Apply scalar quantization to the measurements."""
    return np.round(y / step_size) * step_size

def process_image_in_chunks(image, chunk_size, compression_ratio):
    """Process the image in manageable chunks."""
    chunk_measurements = []
    for i in range(0, len(image), chunk_size):
        chunk = image[i:i + chunk_size]
        M = int(compression_ratio * len(chunk))
        Phi = create_sensing_matrix(M, len(chunk))
        compressed_chunk = compressive_sensing([chunk], Phi)
        quantized_chunk = scalar_quantization(compressed_chunk, step_size=10)
        chunk_measurements.append(quantized_chunk)
    return np.concatenate(chunk_measurements)

# Parameters
filepath = 'C:/Users/vinay/OneDrive/Pictures/Screenshots/bitmapimage.bmp'  # Update with the actual path
image = read_image(filepath)
chunk_size = 1024  # Define chunk size based on expected memory limits
compression_ratio = 0.5

# Process the image
quantized_measurements = process_image_in_chunks(image, chunk_size, compression_ratio)

# Output the size of the compressed data
original_size_kb = len(image) / 1024
compressed_size_kb = len(quantized_measurements) * 8 / 1024  # Assuming each quantized value is stored as a float (8 bytes)

print(f"Original data size: {original_size_kb:.2f} KB")
print(f"Compressed data size: {compressed_size_kb:.2f} KB")

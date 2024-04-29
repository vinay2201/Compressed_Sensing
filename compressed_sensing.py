import lzma
import numpy as np
import os

def lzma_compress(data):
    """Compress data using LZMA algorithm."""
    compressed_data = lzma.compress(data)
    return compressed_data

def lzma_decompress(compressed_data):
    """Decompress LZMA compressed data."""
    decompressed_data = lzma.decompress(compressed_data)
    return decompressed_data

def load_data(filepath):
    """Load data from a file into a byte array."""
    with open(filepath, 'rb') as file:
        data = file.read()
    return data

def save_compressed_data(filepath, compressed_data):
    """Save compressed data to a file."""
    with open(filepath, 'wb') as file:
        file.write(compressed_data)

# Example usage:
filepath = 'D:/RobSenCom/features/features/features_0.pth'
data = load_data(filepath)
compressed_data = lzma_compress(data)
save_compressed_data('compressed_file.xz', compressed_data)
print(compressed_data)

compressed_size_kb = len(compressed_data) / 1024
original_file_size = os.path.getsize(filepath) / 1024
print(f"Original file size: {original_file_size:.2f} KB")
print(f"Compressed file size: {compressed_size_kb:.2f} KB")

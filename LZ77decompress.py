# Author: Léon Brodbeck & Simon Durrer

# Define the compressed data
compressed_data = [(0, 0, 'y'), (0, 0, 'o'), (0, 0, 'u'), (0, 0, 'r'), (1, 3, 's'), (6, 5, 'e'), (3, 2, 't'), (2, 2, 'e'), (1, 1, 'r')]

# Define the decompression function
def lz77_decompress(compressed):
    # Initialize the decompressed output
    decompressed = ''

    # Process each tuple in the compressed data
    for offset, length, next_char in compressed:
        if length > 0:
            # Calculate the start position for repetition
            start = len(decompressed) - offset
            # Append the repeated sequence and the next character
            decompressed += decompressed[start:start + length]
        # Append the next character
        decompressed += next_char

    return decompressed

# Example usage
decompressed_data = lz77_decompress(compressed_data)
print("Decompressed Data:", decompressed_data)

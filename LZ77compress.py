# Author: Léon Brodbeck & Simon Durrer

def format_compressed(compressed):
    # Format the compressed output as a table
    formatted = "Distance | Length | Next Char\n" + "-" * 30 + "\n"
    for distance, length, next_char in compressed:
        formatted += "{:^9} | {:^6} | {}\n".format(distance, length, next_char)
    return formatted

def lz77_compress(text):
    # Window size and look-ahead buffer size
    window_size = 20
    look_ahead_buffer_size = 15

    i = 0
    result = []

    while i < len(text):
        match = ''
        match_distance = -1
        match_length = -1

        # Search for the longest match
        for j in range(max(i - window_size, 0), i):
            substring = text[j:i]
            if text.startswith(substring, i) and len(substring) > len(match):
                match = substring
                match_distance = i - j
                match_length = len(substring)

        # Add the longest match to the result
        if match_length > 1:
            result.append((match_distance, match_length, text[i + match_length]))
            i += match_length + 1
        else:
            result.append((0, 0, text[i]))
            i += 1

    return result

def lz77_decompress(compressed):
    result = ''
    for distance, length, next_char in compressed:
        if length > 0:
            start = len(result) - distance
            result += result[start:start + length]
        result += next_char
    return result

# Test the compression
text = "your sample text here"
compressed = lz77_compress(text)
print("Compressed:\n" + format_compressed(compressed))

# Decompress
decompressed = lz77_decompress(compressed)
print("Decompressed:", decompressed)

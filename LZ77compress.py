# Author: Léon Brodbeck & Simon Durrer

# Adjustable Parameters
WINDOW_SIZE = 20
LOOK_AHEAD_BUFFER_SIZE = 15

# Input Text
INPUT_TEXT = "your sample text here"

def format_compressed(compressed):
    # Format the compressed output as a table
    formatted = "Distance | Length | Next Char\n" + "-" * 30 + "\n"
    for distance, length, next_char in compressed:
        formatted += "{:^9} | {:^6} | {}\n".format(distance, length, next_char)
    return formatted

def lz77_compress(text):
    i = 0
    result = []

    while i < len(text):
        match = ''
        match_distance = -1
        match_length = -1

        # Search for the longest match
        for j in range(max(i - WINDOW_SIZE, 0), i):
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
compressed = lz77_compress(INPUT_TEXT)
print("Compressed:\n" + format_compressed(compressed))

# Decompress
decompressed = lz77_decompress(compressed)
print("Decompressed:", decompressed)

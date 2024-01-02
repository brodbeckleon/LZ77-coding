def lz77_compress(text, window_size, look_ahead_buffer_size):
    i = 0
    result = []

    while i < len(text):
        max_match_distance = 0
        max_match_length = 0
        next_char = ''

        # Search for the longest match within the window and lookahead buffer
        for j in range(max(i - window_size, 0), i):
            match_length = 0
            while match_length < look_ahead_buffer_size and i + match_length < len(text) and text[j + match_length] == text[i + match_length]:
                match_length += 1

            if match_length > max_match_length:
                max_match_distance = i - j
                max_match_length = match_length
                if i + match_length < len(text):
                    next_char = text[i + match_length]

        # Add the longest match to the result
        if max_match_length > 0:
            result.append((max_match_distance, max_match_length, next_char))
            i += max_match_length + 1
        else:
            result.append((0, 0, text[i]))
            i += 1

    return result

# Test the compression
text = "aacaacabcababac"
window_size = 6
look_ahead_buffer_size = 4
compressed = lz77_compress(text, window_size, look_ahead_buffer_size)

# Display the compressed result
print("Compressed:", compressed)

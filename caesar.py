import string

# Ciphertext to decrypt
ciphertext = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."

# Function to decrypt Caesar cipher with a given shift
def caesar_decrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():  # Only decrypt letters
            is_upper = char.isupper()
            base = ord('A') if is_upper else ord('a')
            new_char = chr((ord(char) - base - shift) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)  # Leave non-alphabet characters unchanged
    return ''.join(result)

# Function to perform frequency analysis (naive approach)
def frequency_analysis(text):
    # Approximate frequency of letters in English text
    english_freq = {
        'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0, 'N': 6.7,
        'S': 6.3, 'H': 6.1, 'R': 6.0, 'D': 4.3, 'L': 4.0, 'C': 2.8,
        'U': 2.8, 'M': 2.4, 'W': 2.4, 'F': 2.2, 'G': 2.0, 'Y': 2.0,
        'P': 1.9, 'B': 1.5, 'V': 1.0, 'K': 0.8, 'J': 0.2, 'X': 0.2,
        'Q': 0.1, 'Z': 0.1
    }
    # Calculate frequencies in the ciphertext
    text = text.upper()
    letter_counts = {char: text.count(char) for char in string.ascii_uppercase}
    total_letters = sum(letter_counts.values())
    letter_freqs = {char: (count / total_letters) * 100 for char, count in letter_counts.items()}
    
    # Compare with English frequencies
    score = {shift: sum(abs(letter_freqs.get(chr((ord('A') + (i - shift)) % 26 + ord('A')), 0) - freq)
                        for i, (char, freq) in enumerate(english_freq.items()))
             for shift in range(26)}
    # Return the shift with the smallest score
    return min(score, key=score.get)

# Brute-force attack: try all shifts
print("Brute-Force Results:")
for shift in range(26):
    print(f"Shift {shift}: {caesar_decrypt(ciphertext, shift)}")

# Frequency analysis to suggest the most likely shift
best_shift = frequency_analysis(ciphertext)
print("\nFrequency Analysis Suggestion:")
print(f"Suggested Shift: {best_shift}")
print(f"Decrypted Text: {caesar_decrypt(ciphertext, best_shift)}")

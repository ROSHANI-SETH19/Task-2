def count_vowels_consonants(s):
    vowels = set('aeiou')
    s = s.lower()  # Convert to lowercase
    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return vowel_count, consonant_count

# Example usage:
string = "Hello, World!"
print("String:", string)
vowels, consonants = count_vowels_consonants(string)
print("Vowels:", vowels)
print("Consonants:", consonants)

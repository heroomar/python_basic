# Check if a character is a vowel or consonant:

char = input("Enter a character: ").lower()
if char in 'aeiou':
    print("Vowel")
else:
    print("Consonant")
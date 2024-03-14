def is_hard_word(word):
    vowels = "aeiouAEIOU"
    consecutive_consonants_count = 0
    consonants_count = 0

    for char in word:
        if char.isalpha():
            if char not in vowels:
                consonants_count += 1
                consecutive_consonants_count += 1
                if consecutive_consonants_count == 3:
                    return True
            else:
                consecutive_consonants_count = 0

    return consonants_count > len(word) - consonants_count


def calculate_difficulty_quotient(input_string):
    words = input_string.split()

    hard_words = 0
    easy_words = 0

    for word in words:
        if is_hard_word(word):
            hard_words += 1
        else:
            easy_words += 1

    difficulty_quotient = (5 * hard_words) - (2 * easy_words)
    return difficulty_quotient


length_of_string = int(input())
input_string = input()
print(calculate_difficulty_quotient(input_string))

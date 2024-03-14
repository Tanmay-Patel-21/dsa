def longest_even_length_substring(s):
    n = len(s)
    max_length = 0

    for i in range(n - 1):
        for j in range(i + 1, n, 2):
            k = (j - i + 1) // 2  # Length of the substring
            first_half = sum(map(int, s[i:i+k]))
            second_half = sum(map(int, s[j-k+1:j+1]))

            if first_half == second_half and j - i + 1 > max_length:
                max_length = j - i + 1

    return max_length

n=input()
s=input
print(longest_even_length_substring(s))

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def highest_index(n):
    char_list = [*n]
    char_sort = sorted(char_list)
    for i in range(26):
        if alphabet[i]==char_sort[-1]:
            return i+1, alphabet[i]

n = input("Enter a word: ")
print(str(highest_index(n)[0])+highest_index(n)[1])

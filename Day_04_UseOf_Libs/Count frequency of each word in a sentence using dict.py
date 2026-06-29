s = input("Enter a sentence: ")
words = s.split()

freq_dict = {}

for word in words:
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1

print(freq_dict)


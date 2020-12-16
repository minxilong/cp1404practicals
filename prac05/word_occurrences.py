text = input('Text: ')
word_to_number = {}
word_list = text.split()
for word in word_list:
    if word not in word_to_number:
        word_to_number[word] = 1
    else:
        word_to_number[word] += 1
sorted(word_to_number, key=lambda d:d[0])
length = 0
for key in word_to_number:
    if len(key) > length:
        length = len(key)
for key, value in word_to_number.items():
    print('{:{}} : {}'.format(key, length, value))
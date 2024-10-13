string = "Мы обязательно научимся программировать!"

#1
print(string[2])

#2
print(string[-2])

#3
print(string[:5])

#4
print(string[:-2])

#5
print(string[::2])

#6
print(string[1::2])

#7
middle_index = len(string) // 2
print(string[middle_index-2:middle_index+2])

#8
print(string[::3])

#9
print(string[::-1])

#10
print(string[-1::-2])

#11
words = string.split()
del words[1]
new_string = " ".join(words)
print(new_string)

#12
words = string.split()
words[1] = "никогда не"
new_string = " ".join(words)
print(new_string)

#13
print(string + " на Python")

#14
words = string.split()
words.insert(0, words.pop())
new_string = " ".join(words)
print(new_string)

#15
print(len(string))
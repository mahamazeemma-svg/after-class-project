text = input("enter a sentence:")

words = text.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] +=1
    else:
        frequency[word] =1

print("Word frequency:")
print(frequency)
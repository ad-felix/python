sentence = input("Enter a sentence: ")
result = ""
words = sentence.split()
for i in words:
  if len(i)<=4:
    result += i + " "
  else:
    result += i[::-1] + " "
print(result[:-1])

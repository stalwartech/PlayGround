letter = ["a""e","i","o","u"]
dict = {"a":"e", "e":"i", "i":"o","o":"u","u":"a"}
word = input("Enter your word: ")
word = [dict.get(i,i) for i in word]
word = "".join(word)
print(word)

import re
string = "Hello this is stalwart computer tech, Hello"
print(re.search("Hello",string))
greetings = (re.search("Hello",string))
print(greetings)
position1 = greetings.start()
position2 = greetings.end()
print(position1, position2)
print(string[position1:position2])

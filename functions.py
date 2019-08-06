def greet_user():
    print("Hi User")
    print("welcome")


print("start")
greet_user()
print("finish")


# with parameters
def greet_user_with_param(name):
    print("Hi", name)
    print("welcome")


print("start")
greet_user_with_param("John")
print("finish")


# with  more parameters and keyword arguments
# keyword arguments should be after positional arguments
def greet_user_with_two_param(first_name, last_name):
    print("Hi", first_name, last_name)
    print("welcome")


print("start")
greet_user_with_two_param(last_name='denis', first_name='john')
print("finish")


# return keyword
def square(number):
    return number * number;


print(square(5))


# reuse application
#  function

def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        "sad": ":)",
        "happy": ":(",
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))

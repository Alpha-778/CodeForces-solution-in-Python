def original_message(direction, typed_text):
    keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"
    result = ""
    shift = -1 if direction == 'R' else 1
    for char in typed_text:
        index = keyboard.index(char)
        result += keyboard[index + shift]
    return result
direction = input()
typed_text = input()
print(original_message(direction, typed_text))

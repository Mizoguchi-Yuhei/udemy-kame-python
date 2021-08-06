def print_dict(input_dict):
    for k, v in input_dict.items():
        print(f"key: {k}, value: {v}.")
    # return None


a = {"one": 1, "two": 2}
print(a)
print_dict(a)
return_value = print_dict(a)
print(return_value)


def get_firts_last_word(text):
    text = text.replace(",", "")
    text = text.replace(".", "")
    words = text.split()
    return words[0], words[-1]

text = "Hello, My name is Mike."
first, last = get_firts_last_word(text)
print(f"first word is {first}, last word is {last}.")
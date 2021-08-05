# mutable: 変更可能なオブジェクト list, dict, set
# fruits = ["apple", 'peach', 'banana']
# print(f"fruitsのIDは{id(fruits)}")
# fruits.append('lemon')
# print(fruits)
# print(f"fruitsのIDは{id(fruits)}")
#
# # immutable: 変更な不可能なオブジェクト int, float, str, bool, tuple
# fruit = "apple"
# print(f"fruitのIDは{id(fruit)}")
# fruit += ", lemon"
# print(fruit)
# print(f"fruitのIDは{id(fruit)}")

# immutable
text = "" # 1-2-3-4-5-6-7-...
for i in range(1, 11):
    if i == 1:
        text += str(i)
    else:
        text += '-' + str(i)
print(text)

# mutable
text_list = []
for i in range(1, 11):
    text_list.append(str(i))

text = "-".join(text_list)
print(text)
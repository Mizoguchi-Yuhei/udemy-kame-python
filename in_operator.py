# in演算子
fruits = ["apple", "peach", "grapes", "banana"]
print('apple' in fruits)
print('lemon' in fruits)
print('lemon' not in fruits)

print('h' in 'hello')

# challenge
favorite = input("好きなフルーツはなんですか？")
if "favorite" in fruits:
    print("{}ですね。差し上げます。".format(favorite))
    fruits.remove(favorite)
else:
    fruits.append(favorite)
    print("{}ですね。仕入れました！".format(favorite))

print("今あるフルーツはこちらです。{}".format(fruits))
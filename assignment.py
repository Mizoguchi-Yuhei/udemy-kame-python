# 変数へ代入：assignment
hello = "こんにちは"
world = "世界"
print(hello + world)
print("こんにちは" + "世界")  # ハードコーディング

# format
"hello {}".format("world")
print("{} {}".format(hello, world))

name = "Emily"
print("Hey, {}!! How are you doing?".format(name))
print(f"Hey, {name}!! How are you doing?")


balance = 100
print("balance: {}".format(balance))
print(f"balance: {balance}")


# fstring
print(f"{hello} {world}")
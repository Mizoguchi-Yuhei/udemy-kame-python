# ローカル変数
def print_name_local():
    first_name = "Taro"
    last_name = "Yamada"
    print(f"I'm {first_name} {last_name}.")


print_name_local()
# print(first_name)
# 関数内で定義した変数は関数の中でした使えない

# グローバル変数 (モジュール変数)
age = 30

def print_age():
    # age = 20  # ローカル変数
    print(f"I'm {age} years old.")

print_age()
print(age)
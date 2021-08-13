# 再帰関数 (recursive function): 関数内で自身の関数をcallする関数
# 階乗 (factoria): 3! = 3 x 2 x 1 = 6
# n! = n * (n-1) * (n-2) * ... * 1
# n! = n * (n-1)!

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(3))


def fibonacci_recursive(n):
    if n < 2:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(6))


def fibonacci(n):
    if n < 2:
        return n
    else:
        n_1 = 1
        n_2 = 0
        for _ in range(n-1):
            result = n_2 + n_1
            n_2 = n_1
            n_1 = result
        return result

print(fibonacci(6))

for i in range(50):
    # print(i, fibonacci_recursive(i))  # コードがすっきりする
    print(fibonacci(i))  # こっちのが処理は断然速い
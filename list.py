# リスト(lists)：複数のオブジェクトを順序づけて保存するデータ型
# []でくくって、 ,(カンマ)で各オブジェクトを区切る

fruits = ["apple", "peach", "melon", "grapes"]

hetero_list = ["string", 1, 3.4, True, fruits]
print(hetero_list)
print(fruits[0])
print(fruits[-1])
print(fruits[-2])
print(hetero_list[-1])
print(hetero_list[-1][-3])

print("hello world"[2])


# .append: 新しいオブジェクトを追加する
fruits.append("banana")
print(fruits)
# .insert: 指定したindexに指定したオブジェクトを追加する
fruits.insert(3, 'lemon')
print(fruits)
# .remove: マッチした最初のオブジェクトを除く
fruits.remove('peach')
print(fruits)
# .sort: 昇順に並び替える
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
# len(): リストの要素数を取得する len = length
print(len(fruits))
print(len("hello world"))
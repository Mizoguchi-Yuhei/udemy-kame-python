age = int(input("何歳ですか？"))

casino_age = 18
game_text = """プレイするゲームを選択してください。
1: ルーレット
2: ブラックジャック
3: ポーカー
"""
game_dict = {'a': "ルーレット", 'b': "ブラックジャック", 'c': "ポーカー"}
# game_dict = {'a': "バカラ", 'b': "ブラックジャック", 'c': "ポーカー", 'd': 'スロット'}

if age >= casino_age:
    print("どうぞカジノにお入りください。")
    while True:
        print("プレイするゲームを選択してください。")
        for num, game_name in game_dict.items():
            print(f"{num}: {game_name}")
        game = input(":")
        if game in game_dict:
            print(f"あなたは{game_dict[game]}を選びました。")
            break
        else:
            print("a~cを選択してください。")
else:
    print(f"{casino_age}歳未満の方はカジノに入れません。")
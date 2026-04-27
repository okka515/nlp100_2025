import random

def typoglycemia(s: str) -> str:
    def shuffle_word(word: str) -> str:
        if len(word) <= 4:
            return word
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + "".join(middle) + word[-1]

    return " ".join(shuffle_word(w) for w in s.split(" "))

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia(s))

'''
＃09
英文をスペースで分割、各単語を引数としてshuffle_word()へ

語長が5以上の場合、先頭と末尾を除いた箇所をシャッフル
  ・-1は末尾
  ・pythonにおける文字列は変更不可能（イミュータブル）のため
  　random.shuffle()関数の利用にはlist()による文字配列変換が必要
  ・random.shuffle()関数の戻り値は None であるため、
  　まるごとjoin関数の引数に入れるとエラーが出るので注意
　・先頭, 間(リスト→文字列変換後), 末尾を結合
'''
s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = s.split()
one_get_char = [1, 5, 6, 7, 8, 9, 15, 16, 19]

result = {w[:1 if i in one_get_char else 2]: i for i, w in enumerate(words, 1)}

print(result)

'''
enumerate(words, 1)
単語リストを（位置番号、単語）のペアで返す。1を渡すことで1から始まるね。

i in one_get_char => 位置番号iが、one_get_charに含まれているかを判定している。

w[:1 if i in one_get_char else 2]
前提として、wには単語が格納されている。
リストに含まれる場合 => w[:1]
リストに含まれない場合 => w[:2]
'''
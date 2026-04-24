def n_gram(s, n):
  return [s[i:i+n] for i in range(len(s) - n + 1)]

s = 'I am an NLPer'

# 文字tri-gram
print(n_gram(s, 3))

words = s.split()
print(n_gram(words, 2))
 
'''
解説

n_gramメソッドの作成
これは。入力された文字列 - n + 1で、窓を移動させる回数を取得している。
それをrangeすることで、iには回数が格納されている。

s[i:i+n]により、i番目から+nしたものを取得することができ、それを出力することができる。
'''
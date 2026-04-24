def n_gram(s, n):
  return [s[i:i+n] for i in range(len(s) - n + 1)]

paradise = "paraparaparadise"
paragraph = "paragraph"

X = set(n_gram(paradise, 2))
Y = set(n_gram(paragraph, 2))


print("X:", X)
print("Y:", Y)
print("和集合：", X | Y)
print("積集合", X & Y)
print("差集合", X - Y)
print("se" in X)
print("se" in Y)

'''
解説
setメソッドとは
重複を持たないデータ構造を作成してくれる。
今回は後々、和集合や積集合など、重複に意味を持たないものなのでsetメソッドによってシンプルにしている。

集合計算に関しては、|が和、&が積、差は-で表現できるため、それを記述すれば良い。
se in Xに関しては、Xにseがあるかどうかを真偽地で返す。

'''
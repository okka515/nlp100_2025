s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = s.split()
result = [len(w.strip(".,")) for w in words]
print(result)

'''
split()は、空白で区切るものである。wordsにはその区切られたものが配列として格納されている。

3行目は、wに配列が順次格納されている。そこで
w.strip(".,")を使用することで、.,を除去している。
len()にそれが入っているので、除去後の文字列数を取得している。
'''

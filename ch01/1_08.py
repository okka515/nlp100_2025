def cipher(s: str) -> str:
    return "".join(
        chr(219 - ord(c)) if c.islower() else c
        for c in s
    )

message = "I couldn't believe that I could actually understand what I was reading."

encrypted = cipher(message)
decrypted = cipher(encrypted)

print("元文字列:", message)
print("暗号化:  ", encrypted)
print("復号化:  ", decrypted)


'''
#08
小文字かチェック
小文字の場合, 所定の変換を施す

暗号文に対し, 再度関数を適用することで元に戻る理由 ↓
・暗号分への変換において, 小文字 → 小文字 の変換のみがされる (219-122=97, 219-97=122)
　すなわち、暗号分と平文の相違点は小文字の部分のみ
・暗号分の小文字に対して再度 219 - ord(c(暗)) を適用することは
　219 - (219 - ord(c(平))) = ord(c(平)) に該当
'''
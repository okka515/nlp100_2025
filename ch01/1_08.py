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

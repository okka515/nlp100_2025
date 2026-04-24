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

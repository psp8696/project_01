# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    return s.replace("!","")

# Тесты
# s = "Hi! Hello!"
# s = ""
# s = "Oh, no!!!"

# print(remove_exclamation_marks(s))

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if s.endswith('!'):
        return s[:-1]
    else:
        return s
        
# Тесты
# s = "Hi!"
# s = "Hi!!!"
# s = "!Hi"
# print(remove_last_em(s))

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    words = s.split()
    result =[]
    for word in words:
        if word.count('!') !=1:
            result.append(word)
    return ''.join(result)

# s = "Hi!"
# s = "Hi! Hi!"
# s = "Hi! Hi! Hi!"
# s = "Hi Hi! Hi!"
# s = "Hi! !Hi Hi!"
# s = "Hi! Hi!! Hi!"
s = "Hi! !Hi! Hi!"
print(remove_word_with_one_em(s))
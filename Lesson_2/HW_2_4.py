text = input("Введите какое-нибудь предложение: ")
user_text = text.split()
for word, srez in enumerate(user_text, 1):
    print(word, srez[:10])
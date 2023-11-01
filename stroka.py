text = input("Введите предложение: ")
cleaned_text = ""
for i in range(len(text)):
    if text[i] == " ":
        if i+1 < len(text) and text[i+1] == " ":
            continue
    cleaned_text += text[i]
print("Чисто:", cleaned_text)
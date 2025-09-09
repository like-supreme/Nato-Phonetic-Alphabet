import pandas as pd

csv_data = pd.read_csv("C:/Users/mdeha/OneDrive/Masaüstü/python/day30/nato_alphabet_advanced/nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter:row.code for (index,row) in csv_data.iterrows()}
print(nato_alphabet)


def generate_phonetic():
    word = input("Enter your name. ").upper() #dog -> DOG
    try:
        user_list = [print(f"{letter} for {nato_alphabet[letter]}") for letter in word]
        # çok önerilmez ama olur dendi. 
    except KeyError:
        print("Sorry, only letters in the latin alphabet please")
        generate_phonetic()


generate_phonetic()

import pandas as pd

csv_data = pd.read_csv("C:/Users/mdeha/OneDrive/Masaüstü/python/day26/nato_alphabet/nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter:row.code for (index,row) in csv_data.iterrows()}
print(nato_alphabet)

word = input("Enter your name. ").upper() #dog -> DOG

user_list = [print(f"{letter} for {nato_alphabet[letter]}") for letter in word]
# çok önerilmez ama olur dendi. 




# Nato-Phonetic-Alphabet
A small Python program that converts any word or name into its NATO phonetic alphabet spelling.   It reads a CSV dataset (A→Z) with code words, builds a mapping, then prints each character as `&lt;LETTER> for &lt;CodeWord>` (e.g., `D for Delta`).


# NATO Phonetic Alphabet Converter

A small Python program that converts any word or name into its NATO phonetic alphabet spelling.  
It reads a CSV dataset (A→Z) with code words, builds a mapping, then prints each character as
`<LETTER> for <CodeWord>` (e.g., `D for Delta`).

---

## ✨ Features

- **CSV-driven mapping**: Easily swap or customize the dataset without changing code.
- **Clean console output**: Prints each letter on a new line in `L for Lima` format.
- **Simple & readable**: Minimal Python + pandas—great for beginners practicing file I/O & dict comprehensions.

---

## 🧰 Requirements

- Python 3.x
- [pandas](https://pypi.org/project/pandas/)

Install dependency:

pip install pandas
Optional (recommended): Use a virtual environment:


python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install pandas
▶️ Usage
Run the script from the repository root:


python main.py
When prompted, enter a word or name:


Enter your name: dog
D for Delta
O for Oscar
G for Golf
🗂️ Project Structure


.
├── main.py                       # Main script (reads CSV, builds dict, prints codes)
└── nato_phonetic_alphabet.csv    # Data source (columns: letter, code)
CSV format (example):


letter,code
A,Alfa
B,Bravo
C,Charlie
...
Z,Zulu
Note: The dataset uses “Alfa” spelling (NATO/ICAO standard) instead of “Alpha”.

🧠 How It Works (high level)
Load nato_phonetic_alphabet.csv with pandas.

Build a dictionary via a row-wise iteration (e.g., {row.letter: row.code}).

Read input, uppercase it, then for each character print "<LETTER> for <CodeWord>".

📝 Behavior & Notes
Input is uppercased internally, so both dog and DOG work the same.

The current script expects A–Z letters.

If you enter digits or symbols, you’ll need to add simple validation or try/except to skip them or show a friendly message.

If you’d like “one-line output”, you can join the lines yourself (e.g., " • ".join(...))—left as an easy extension.

🔧 Extending
Custom alphabets: Replace the CSV with another mapping (e.g., Turkish letters or different radio alphabets).

Input validation: Ignore non-letters or prompt the user again.

GUI: Wrap the converter with Tkinter for a quick desktop tool.

CLI flags: Add argparse to accept input as a command-line argument instead of input().


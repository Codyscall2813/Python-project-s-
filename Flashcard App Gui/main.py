import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style

# Database operations
def create_tables(conn):
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS flashcard_sets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS flashcards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                set_id INTEGER NOT NULL,
                word TEXT NOT NULL,
                definition TEXT NOT NULL,
                FOREIGN KEY (set_id) REFERENCES flashcard_sets(id)
            )
        ''')

def add_set(conn, name):
    with conn:
        cursor = conn.execute('INSERT INTO flashcard_sets (name) VALUES (?)', (name,))
    return cursor.lastrowid

def add_card(conn, set_id, word, definition):
    with conn:
        cursor = conn.execute('''
            INSERT INTO flashcards (set_id, word, definition)
            VALUES (?, ?, ?)
        ''', (set_id, word, definition))
    return cursor.lastrowid

def get_sets(conn):
    cursor = conn.execute('SELECT id, name FROM flashcard_sets')
    return {row[1]: row[0] for row in cursor.fetchall()}

def get_cards(conn, set_id):
    cursor = conn.execute('SELECT word, definition FROM flashcards WHERE set_id = ?', (set_id,))
    return [(row[0], row[1]) for row in cursor.fetchall()]

def delete_set(conn, set_id):
    with conn:
        conn.execute('DELETE FROM flashcard_sets WHERE id = ?', (set_id,))
        conn.execute('DELETE FROM flashcards WHERE set_id = ?', (set_id,))

# GUI operations
def create_set():
    set_name = set_name_var.get().strip()
    if set_name and set_name not in get_sets(conn):
        add_set(conn, set_name)
        populate_sets_combobox()
        set_name_var.set('')

def add_word():
    set_name = set_name_var.get().strip()
    word = word_var.get().strip()
    definition = definition_var.get().strip()

    if set_name and word and definition:
        sets = get_sets(conn)
        if set_name not in sets:
            set_id = add_set(conn, set_name)
        else:
            set_id = sets[set_name]
        add_card(conn, set_id, word, definition)
        word_var.set('')
        definition_var.set('')
        populate_sets_combobox()

def populate_sets_combobox():
    sets_combobox['values'] = list(get_sets(conn).keys())

def delete_selected_set():
    set_name = sets_combobox.get()
    if set_name:
        result = messagebox.askyesno('Confirmation', f'Are you sure you want to delete the "{set_name}" set?')
        if result:
            set_id = get_sets(conn)[set_name]
            delete_set(conn, set_id)
            populate_sets_combobox()
            clear_flashcard_display()

def select_set():
    set_name = sets_combobox.get()
    if set_name:
        set_id = get_sets(conn)[set_name]
        cards = get_cards(conn, set_id)
        display_flashcards(cards)
    else:
        clear_flashcard_display()

def display_flashcards(cards):
    global card_index, current_cards
    current_cards = cards
    card_index = 0
    show_card()

def show_card():
    if current_cards:
        word, _ = current_cards[card_index]
        word_label.config(text=word)
        definition_label.config(text='')
    else:
        clear_flashcard_display()

def flip_card():
    if current_cards:
        _, definition = current_cards[card_index]
        definition_label.config(text=definition)

def next_card():
    global card_index
    if current_cards:
        card_index = min(card_index + 1, len(current_cards) - 1)
        show_card()

def prev_card():
    global card_index
    if current_cards:
        card_index = max(card_index - 1, 0)
        show_card()

def clear_flashcard_display():
    word_label.config(text='')
    definition_label.config(text='')

if __name__ == '__main__':
    # Database connection
    conn = sqlite3.connect('flashcards.db')
    create_tables(conn)

    # GUI setup
    root = tk.Tk()
    root.title('Flashcards App')
    root.geometry('500x400')

    style = Style(theme='superhero')
    style.configure('TLabel', font=('TkDefaultFont', 18))
    style.configure('TButton', font=('TkDefaultFont', 16))

    # Variables
    set_name_var = tk.StringVar()
    word_var = tk.StringVar()
    definition_var = tk.StringVar()

    # Notebook and tabs
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Create Set tab
    create_set_frame = ttk.Frame(notebook)
    notebook.add(create_set_frame, text='Create Set')

    ttk.Label(create_set_frame, text='Set Name:').pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=set_name_var, width=30).pack(padx=5, pady=5)
    ttk.Label(create_set_frame, text='Word:').pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=word_var, width=30).pack(padx=5, pady=5)
    ttk.Label(create_set_frame, text='Definition:').pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=definition_var, width=30).pack(padx=5, pady=5)
    ttk.Button(create_set_frame, text='Add Word', command=add_word).pack(padx=5, pady=10)
    ttk.Button(create_set_frame, text='Save Set', command=create_set).pack(padx=5, pady=10)

    # Select Set tab
    select_set_frame = ttk.Frame(notebook)
    notebook.add(select_set_frame, text="Select Set")

    sets_combobox = ttk.Combobox(select_set_frame, state='readonly')
    sets_combobox.pack(padx=5, pady=40)
    ttk.Button(select_set_frame, text='Select Set', command=select_set).pack(padx=5, pady=5)
    ttk.Button(select_set_frame, text='Delete Set', command=delete_selected_set).pack(padx=5, pady=5)

    # Learn Mode tab
    flashcards_frame = ttk.Frame(notebook)
    notebook.add(flashcards_frame, text='Learn Mode')

    word_label = ttk.Label(flashcards_frame, text='', font=('TkDefaultFont', 24))
    word_label.pack(padx=5, pady=40)
    definition_label = ttk.Label(flashcards_frame, text='')
    definition_label.pack(padx=5, pady=5)

    ttk.Button(flashcards_frame, text='Flip', command=flip_card).pack(side='left', padx=5, pady=5)
    ttk.Button(flashcards_frame, text='Next', command=next_card).pack(side='right', padx=5, pady=5)
    ttk.Button(flashcards_frame, text='Previous', command=prev_card).pack(side='right', padx=5, pady=5)

    populate_sets_combobox()
    root.mainloop()

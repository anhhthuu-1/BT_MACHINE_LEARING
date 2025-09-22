import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

class TextTranslatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Text Translator")

        self.create_widgets()

    def create_widgets(self):
        label1 = tk.Label(self.root, text="Enter text to translate:")
        self.entry = tk.Entry(self.root, width=50)

        label2 = tk.Label(self.root, text="Choose source language:")
        self.source_lang = ttk.Combobox(self.root, values=["auto", "en", "es", "fr", "vi", "ja", "zh"])
        self.source_lang.set("auto")  # tự nhận diện

        label3 = tk.Label(self.root, text="Choose target language:")
        self.target_lang = ttk.Combobox(self.root, values=["en", "es", "fr", "vi", "ja", "zh"])
        self.target_lang.set("vi")

        translate_button = tk.Button(self.root, text="Translate", command=self.translate_text)

        self.result_label = tk.Label(self.root, text="Translated text will appear here.", wraplength=400, justify="left")

        # Layout
        label1.grid(row=0, column=0, padx=10, pady=10)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        label2.grid(row=1, column=0, padx=10, pady=10)
        self.source_lang.grid(row=1, column=1, padx=10, pady=10)

        label3.grid(row=2, column=0, padx=10, pady=10)
        self.target_lang.grid(row=2, column=1, padx=10, pady=10)

        translate_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def translate_text(self):
        text_to_translate = self.entry.get()
        src = self.source_lang.get()
        dest = self.target_lang.get()

        try:
            translated = GoogleTranslator(source=src, target=dest).translate(text_to_translate)
            self.result_label.config(text=translated)
        except Exception as e:
            self.result_label.config(text=f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextTranslatorApp(root)
    root.mainloop()

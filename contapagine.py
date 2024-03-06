import os
import PyPDF2

def conta_pagine(file_path):
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            return len(pdf_reader.pages)
    except Exception as e:
        print(f"Errore nella lettura del file {file_path}: {e}")
        return 0

def conta_pagine_cartella(cartella):
    total_pagine = 0

    for root, _, files in os.walk(cartella):
        for file in files:
            if file.lower().endswith('.pdf'):
                file_path = os.path.join(root, file)
                total_pagine += conta_pagine(file_path)

    return total_pagine

if __name__ == "__main__":
    cartella_input = input("Inserisci il percorso della cartella: ")
    numero_pagine = conta_pagine_cartella(cartella_input)
    print(f"I file PDF nella cartella contengono complessivamente {numero_pagine} pagine.")

import tkinter as tk
from tkinter import ttk

from core.classes.misure_segmento import Misure_segmento
from core.classes.segmento import Segmento


class ShowSegments:
    def __init__(self, root, lista_segmenti):
        self.root = root
        self.root.title("Tabella segmenti inseriti")
        tree = ttk.Treeview(root, columns=(
            "Segmento ID", "Lunghezza esterna", "Lunghezza interna", "Spessore", "Angolo sinistro",
            "Angolo destro"))

        for col in ["Segmento ID", "Lunghezza esterna", "Lunghezza interna", "Spessore", "Angolo sinistro",
                    "Angolo destro"]:
            tree.column(col, anchor=tk.W, width=150)
            tree.heading(col, text=col, anchor=tk.W)

        for key, value in lista_segmenti.items():
            prima_chiave = next(iter(value))
            tmp: Misure_segmento = value[prima_chiave]
            data = (key, tmp.segmento.l_esterna, tmp.segmento.l_interna,
                    tmp.segmento.spessore_sbarra, tmp.segmento.angolo_sx, tmp.segmento.angolo_dx)
            tree.insert("", tk.END, values=data)
        tree.pack(fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.configure(yscrollcommand=scrollbar.set)

        # Pulsante per tornare alla Finestra Principale
        back_button = ttk.Button(root, text="Chiudi", command=self.back_to_main)
        back_button.pack(pady=10)

    def back_to_main(self):
        # Chiudi la Finestra 1 e torna alla Finestra Principale
        self.root.destroy()

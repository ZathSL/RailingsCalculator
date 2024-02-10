import sys
import tkinter as tk
from tkinter import ttk, messagebox

from core.classes.contatore import Contatore
from core.clustering.clustering_util import clustering_misure
from gui.insert_segment import InsertSegment
from gui.show_segments import ShowSegments
from gui.show_clusters import ShowClusters


def on_closing():
    sys.exit(0)


class MainWindow:
    def __init__(self, root, lista_segmenti, contatore: Contatore, numero_misure_diverse,
                 n_max_busoni_acciaio, n_min_busoni_acciaio, n_max_busoni_alluminio,
                 n_min_busoni_alluminio, min_distanza_fine_sbarra_lato_busone, max_distanza_fine_sbarra_lato_busone):
        self.root = root
        self.root.title("Ringhiere calculator")
        self.lista_segmenti = lista_segmenti
        self.contatore = contatore
        self.numero_misure_diverse = numero_misure_diverse
        self.n_max_busoni_acciaio = n_max_busoni_acciaio
        self.n_min_busoni_acciaio = n_min_busoni_acciaio
        self.n_max_busoni_alluminio = n_max_busoni_alluminio
        self.n_min_busoni_alluminio = n_min_busoni_alluminio
        self.min_distanza_fine_sbarra_lato_busone = min_distanza_fine_sbarra_lato_busone
        self.max_distanza_fine_sbarra_lato_busone = max_distanza_fine_sbarra_lato_busone
        self.updated = contatore.id_segmenti
        self.cluster = None
        # Imposta la dimensione e il posizionamento della finestra al centro
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = 400
        window_height = 300
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Etichetta di benvenuto
        welcome_label = ttk.Label(root, text="Benvenuto in Ringhiere Calculator, scegli un'azione",
                                  font=("Helvetica", 12))
        welcome_label.pack(pady=20)

        # Pulsanti per le azioni
        action_button1 = ttk.Button(root, text="Inserisci un segmento", command=self.open_window1)
        action_button1.pack(pady=10)
        action_button1.config(width=40)

        action_button2 = ttk.Button(root, text="Mostra i segmenti inseriti", command=self.open_window2)
        action_button2.pack(pady=10)
        action_button2.config(width=40)

        action_button3 = ttk.Button(root, text="Mostra i possibili insiemi", command=self.open_window3)
        action_button3.pack(pady=10)
        action_button3.config(width=40)

        action_button4 = ttk.Button(root, text="Esci", command=sys.exit)
        action_button4.pack(pady=10)
        action_button4.config(width=40)
        self.root.mainloop()
        self.root.protocol("WM_DELETE_WINDOW", on_closing())

    def open_window1(self):
        # Crea un'istanza di Window1
        window1_root = tk.Toplevel(self.root)
        InsertSegment(window1_root, self.lista_segmenti, self.contatore, self.numero_misure_diverse,
                      self.n_max_busoni_acciaio, self.n_min_busoni_acciaio, self.n_max_busoni_alluminio,
                      self.n_min_busoni_alluminio, self.min_distanza_fine_sbarra_lato_busone,
                      self.max_distanza_fine_sbarra_lato_busone)

    def open_window2(self):
        # Crea un'istanza di Window1
        window1_root = tk.Toplevel(self.root)
        ShowSegments(window1_root, self.lista_segmenti)

    def open_window3(self):
        if len(self.lista_segmenti) == 0:
            messagebox.showerror("Risultati", "Inserisci prima dei segmenti")
            return
        else:
            if self.updated != self.contatore.id_segmenti:
                self.cluster = clustering_misure(self.lista_segmenti)
                self.updated = self.contatore.id_segmenti
            window1_root = tk.Toplevel(self.root)
            ShowClusters(window1_root, self.lista_segmenti, self.cluster)

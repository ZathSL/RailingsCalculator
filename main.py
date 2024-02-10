import tkinter as tk

from core.classes.contatore import Contatore
from gui.main_window import MainWindow


def main():
    lista_segmenti = {}
    numero_misure_diverse = 50
    n_max_busoni_acciaio = 50
    n_min_busoni_acciaio = 1
    n_max_busoni_alluminio = 50
    n_min_busoni_alluminio = 1
    min_distanza_fine_sbarra_lato_busone = 20
    max_distanza_fine_sbarra_lato_busone = 30
    root = tk.Tk()
    contatore = Contatore()
    MainWindow(root, lista_segmenti, contatore, numero_misure_diverse,
               n_max_busoni_acciaio, n_min_busoni_acciaio, n_max_busoni_alluminio,
               n_min_busoni_alluminio, min_distanza_fine_sbarra_lato_busone, max_distanza_fine_sbarra_lato_busone)
    root.mainloop()


if __name__ == "__main__":
    main()

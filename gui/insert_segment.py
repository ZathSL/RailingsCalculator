import tkinter as tk
from tkinter import ttk, messagebox

from core.classes.contatore import Contatore
from core.classes.segmento import Segmento
from core.tracciature import calculate


class InsertSegment:
    def __init__(self, root, lista_segmenti, contatore: Contatore, numero_misure_diverse,
                 n_max_busoni_acciaio, n_min_busoni_acciaio, n_max_busoni_alluminio,
                 n_min_busoni_alluminio, min_distanza_fine_sbarra_lato_busone, max_distanza_fine_sbarra_lato_busone):

        self.root = root
        self.root.title("Inserisci le misure del nuovo segmento")

        self.lista_segmenti = lista_segmenti
        self.contatore = contatore
        self.numero_misure_diverse = numero_misure_diverse
        self.n_max_busoni_acciaio = n_max_busoni_acciaio
        self.n_min_busoni_acciaio = n_min_busoni_acciaio
        self.n_max_busoni_alluminio = n_max_busoni_alluminio
        self.n_min_busoni_alluminio = n_min_busoni_alluminio
        self.min_distanza_fine_sbarra_lato_busone = min_distanza_fine_sbarra_lato_busone
        self.max_distanza_fine_sbarra_lato_busone = max_distanza_fine_sbarra_lato_busone

        # Labels
        self.label_lunghezza_tracciatura = tk.Label(self.root,
                                                    text="Inserisci la lunghezza su cui vuoi fare la tracciatura")
        self.label_lunghezza_muro = tk.Label(self.root,
                                             text="Inserisci lunghezza partendo dal muro fino alla punta opposta della ringhiera in mm")
        self.label_distanza_muro = tk.Label(self.root,
                                            text="Inserisci la distanza tra il muro e l'inizio della lunghezza esterna in mm")
        self.label_lunghezza_esterna = tk.Label(self.root, text="Inserisci lunghezza esterna della ringhiera in mm")
        self.label_spessore_sbarra = tk.Label(self.root, text="Inserisci spessore sbarra della ringhiera in mm")
        self.label_angolo_sinistro = tk.Label(self.root, text="Inserisci apertura angolo sinistro in gradi")
        self.label_angolo_destro = tk.Label(self.root, text="Inserisci apertura angolo destro in gradi")
        self.label_lunghezza_busone = tk.Label(self.root,
                                               text="Inserisci lunghezza busone grande (dove inserire sbarre di acciaio) in mm")
        self.label_lunghezza_alluminio = tk.Label(self.root,
                                                  text="Inserisci lunghezza busone piccolo (dove inserire sbarre di alluminio) in mm")
        self.label_profondita_busone_alluminio = tk.Label(self.root,
                                                          text="Inserisci la profondità del busone di alluminio")
        self.label_distanza_minima = tk.Label(self.root, text="Inserisci la distanza minima tra i busoni piccoli in mm")

        # Entry
        self.entry_lunghezza_tracciatura = tk.Entry(root)
        self.entry_lunghezza_esterna_muro = tk.Entry(root)
        self.entry_distanza_muro = tk.Entry(root)
        self.entry_lunghezza_esterna = tk.Entry(root)
        self.entry_spessore_sbarra = tk.Entry(root)
        self.entry_angolo_sinistro = tk.Entry(root)
        self.entry_angolo_destro = tk.Entry(root)
        self.entry_lunghezza_busone = tk.Entry(root)
        self.entry_lunghezza_alluminio = tk.Entry(root)
        self.entry_profondita_busone = tk.Entry(root)
        self.entry_distanza_minima = tk.Entry(root)

        self.opzioni = ["Parte sinistra in prossimita del muro", "Parte destra in prossimita del muro",
                   "Entrambe le parti in prossimita del muro", "Nessuna parte in prossimita del muro",
                   "Tracciatura di uno spazio"]

        self.combo_var = tk.StringVar(value=self.opzioni[3])
        self.combo = ttk.Combobox(root, textvariable=self.combo_var, values=self.opzioni, width=37, )
        self.combo.grid(row=0, column=2, pady=10, padx=20)
        self.combo.set("Nessuna parte in prossimita del muro")
        # Aggiunta dell'evento di cambio selezione alla casella di selezione
        self.combo_var.trace_add('write', self.scelta_opzioni)

        # Pulsante per tornare alla Finestra Principale
        self.back_button = ttk.Button(root, text="Chiudi", command=self.back_to_main)
        self.insert_button = tk.Button(root, text="Inserisci", command=self.insert_segment)
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_entry)
        self.clean_window()
        self.set_window2()
        self.root.mainloop()
        self.root.protocol("WM_DELETE_WINDOW", self.back_to_main())


    def insert_segment(self):
        try:
            l_tracciatura = l_muro = distanza_muro = distanza_minima = 0
            combo_var = str(self.combo_var.get())
            if combo_var == "Parte sinistra in prossimita del muro" or \
                    combo_var == "Parte destra in prossimita del muro" or \
                    combo_var == "Entrambe le parti in prossimita del muro":
                segmento = Segmento(self.contatore.id_segmenti + 1, float(0),
                                    float(self.entry_spessore_sbarra.get()), float(self.entry_angolo_sinistro.get()),
                                    float(self.entry_angolo_destro.get()), float(self.entry_lunghezza_busone.get()),
                                    float(self.entry_lunghezza_alluminio.get()), float(self.entry_profondita_busone.get()))
                l_muro = float(self.entry_lunghezza_esterna_muro.get())
                distanza_muro = float(self.entry_distanza_muro.get())
            elif combo_var == "Nessuna parte in prossimita del muro":
                segmento = Segmento(self.contatore.id_segmenti + 1, float(self.entry_lunghezza_esterna.get()),
                            float(self.entry_spessore_sbarra.get()), float(self.entry_angolo_sinistro.get()),
                            float(self.entry_angolo_destro.get()), float(self.entry_lunghezza_busone.get()),
                            float(self.entry_lunghezza_alluminio.get()), float(self.entry_profondita_busone.get()))
            else:
                segmento = Segmento(self.contatore.id_segmenti + 1, float(0), float(0), float(0), float(0), float(0),
                        float(self.entry_lunghezza_alluminio.get()), float(self.entry_profondita_busone.get()))
                l_tracciatura = float(self.entry_lunghezza_tracciatura.get())
            distanza_minima = float(self.entry_distanza_minima.get())

            self.contatore.increase()
            self.lista_segmenti[self.contatore.id_segmenti] = calculate.calcola_risultati(segmento, l_tracciatura, distanza_minima,
                                                                                distanza_muro, l_muro, combo_var, self.numero_misure_diverse,
                                                                                self.n_max_busoni_acciaio, self.n_min_busoni_acciaio,
                                                                                self.n_max_busoni_alluminio, self.n_min_busoni_alluminio,
                                                                                self.min_distanza_fine_sbarra_lato_busone,
                                                                                self.max_distanza_fine_sbarra_lato_busone)
            self.back_to_main()
            messagebox.showinfo("Successo", "Segmento inserito con successo!")
        except ValueError:
            messagebox.showerror("Errore", "Inserisci valori validi")
            return

    def scelta_opzioni(self, *args):
        scelta_selezionata = self.combo_var.get()
        if scelta_selezionata == "Parte sinistra in prossimita del muro" or \
                scelta_selezionata == "Parte destra in prossimita del muro" or \
                scelta_selezionata == "Entrambe le parti in prossimita del muro":
            self.clean_window()
            self.set_window1()
        elif scelta_selezionata == "Nessuna parte in prossimita del muro":
            self.clean_window()
            self.set_window2()
        else:
            self.clean_window()
            self.set_window3()

    def set_window1(self):
        self.label_lunghezza_muro.grid(row=0, column=0, padx=10, pady=10)
        self.entry_lunghezza_esterna_muro.grid(row=0, column=1, padx=10, pady=10)
        self.label_distanza_muro.grid(row=1, column=0, padx=10, pady=10)
        self.entry_distanza_muro.grid(row=1, column=1, padx=10, pady=10)
        self.label_spessore_sbarra.grid(row=2, column=0, padx=10, pady=10)
        self.entry_spessore_sbarra.grid(row=2, column=1, padx=10, pady=10)
        self.label_angolo_sinistro.grid(row=3, column=0, padx=10, pady=10)
        self.entry_angolo_sinistro.grid(row=3, column=1, padx=10, pady=10)
        self.label_angolo_destro.grid(row=4, column=0, padx=10, pady=10)
        self.entry_angolo_destro.grid(row=4, column=1, padx=10, pady=10)
        self.label_lunghezza_busone.grid(row=5, column=0, padx=10, pady=10)
        self.entry_lunghezza_busone.grid(row=5, column=1, padx=10, pady=10)
        self.label_lunghezza_alluminio.grid(row=6, column=0, padx=10, pady=10)
        self.entry_lunghezza_alluminio.grid(row=6, column=1, padx=10, pady=10)
        self.label_profondita_busone_alluminio.grid(row=7, column=0, padx=10, pady=10)
        self.entry_profondita_busone.grid(row=7, column=1, padx=10, pady=10)
        self.label_distanza_minima.grid(row=8, column=0, padx=10, pady=10)
        self.entry_distanza_minima.grid(row=8, column=1, padx=10, pady=10)
        self.insert_button.grid(row=9, column=0, columnspan=2, pady=10)
        self.reset_button.grid(row=9, column=1, columnspan=2, pady=10)
        self.back_button.grid(row=9, column=2, columnspan=2, pady=10)

    def set_window2(self):
        self.label_lunghezza_esterna.grid(row=0, column=0, padx=10, pady=10)
        self.entry_lunghezza_esterna.grid(row=0, column=1, padx=10, pady=10)
        self.label_spessore_sbarra.grid(row=1, column=0, padx=10, pady=10)
        self.entry_spessore_sbarra.grid(row=1, column=1, padx=10, pady=10)
        self.label_angolo_sinistro.grid(row=2, column=0, padx=10, pady=10)
        self.entry_angolo_sinistro.grid(row=2, column=1, padx=10, pady=10)
        self.label_angolo_destro.grid(row=3, column=0, padx=10, pady=10)
        self.entry_angolo_destro.grid(row=3, column=1, padx=10, pady=10)
        self.label_lunghezza_busone.grid(row=4, column=0, padx=10, pady=10)
        self.entry_lunghezza_busone.grid(row=4, column=1, padx=10, pady=10)
        self.label_lunghezza_alluminio.grid(row=5, column=0, padx=10, pady=10)
        self.entry_lunghezza_alluminio.grid(row=5, column=1, padx=10, pady=10)
        self.label_profondita_busone_alluminio.grid(row=6, column=0, padx=10, pady=10)
        self.entry_profondita_busone.grid(row=6, column=1, padx=10, pady=10)
        self.label_distanza_minima.grid(row=7, column=0, padx=10, pady=10)
        self.entry_distanza_minima.grid(row=7, column=1, padx=10, pady=10)
        self.insert_button.grid(row=9, column=0, columnspan=2, pady=10)
        self.reset_button.grid(row=9, column=1, columnspan=2, pady=10)
        self.back_button.grid(row=9, column=2, columnspan=2, pady=10)

    def set_window3(self):
        self.label_lunghezza_tracciatura.grid(row=0, column=0, padx=10, pady=10)
        self.entry_lunghezza_tracciatura.grid(row=0, column=1, padx=10, pady=10)
        self.label_lunghezza_alluminio.grid(row=1, column=0, padx=10, pady=10)
        self.entry_lunghezza_alluminio.grid(row=1, column=1, padx=10, pady=10)
        self.label_profondita_busone_alluminio.grid(row=2, column=0, padx=10, pady=10)
        self.entry_profondita_busone.grid(row=2, column=1, padx=10, pady=10)
        self.label_distanza_minima.grid(row=3, column=0, padx=10, pady=10)
        self.entry_distanza_minima.grid(row=3, column=1, padx=10, pady=10)
        self.insert_button.grid(row=9, column=0, columnspan=2, pady=10)
        self.reset_button.grid(row=9, column=1, columnspan=2, pady=10)
        self.back_button.grid(row=9, column=2, columnspan=2, pady=10)

    def back_to_main(self):
        # Chiudi la Finestra 1 e torna alla Finestra Principale
        self.root.destroy()

    def reset_entry(self):
        self.entry_lunghezza_esterna_muro.delete(0, tk.END)
        self.entry_lunghezza_esterna.delete(0, tk.END)
        self.entry_distanza_muro.delete(0, tk.END)
        self.entry_spessore_sbarra.delete(0, tk.END)
        self.entry_angolo_sinistro.delete(0, tk.END)
        self.entry_angolo_destro.delete(0, tk.END)
        self.entry_lunghezza_busone.delete(0, tk.END)
        self.entry_lunghezza_alluminio.delete(0, tk.END)
        self.entry_profondita_busone.delete(0, tk.END)
        self.entry_distanza_minima.delete(0, tk.END)

    def clean_window(self):
        self.entry_lunghezza_esterna_muro.grid_forget()
        self.entry_distanza_muro.grid_forget()
        self.entry_lunghezza_esterna.grid_forget()
        self.entry_spessore_sbarra.grid_forget()
        self.entry_angolo_sinistro.grid_forget()
        self.entry_angolo_destro.grid_forget()
        self.entry_lunghezza_busone.grid_forget()
        self.entry_lunghezza_alluminio.grid_forget()
        self.entry_distanza_minima.grid_forget()
        self.entry_lunghezza_tracciatura.grid_forget()
        self.entry_profondita_busone.grid_forget()
        self.label_distanza_muro.grid_forget()
        self.label_lunghezza_muro.grid_forget()
        self.label_lunghezza_esterna.grid_forget()
        self.label_spessore_sbarra.grid_forget()
        self.label_angolo_sinistro.grid_forget()
        self.label_angolo_destro.grid_forget()
        self.label_lunghezza_busone.grid_forget()
        self.label_lunghezza_alluminio.grid_forget()
        self.label_distanza_minima.grid_forget()
        self.label_lunghezza_tracciatura.grid_forget()
        self.label_profondita_busone_alluminio.grid_forget()
        self.back_button.grid_forget()
        self.insert_button.grid_forget()
        self.reset_button.grid_forget()

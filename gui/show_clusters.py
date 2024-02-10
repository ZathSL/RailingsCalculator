import tkinter as tk
from tkinter import ttk, messagebox
import core.tracciature as tr
from core.classes.misure_segmento import Misure_segmento
from core.classes.segmento import Segmento
from core.clustering.clustering_util import clustering_misure
from core.tracciature.tracciatura import calcola_buchi


class ShowClusters:
    def __init__(self, root, lista_segmenti, cluster):
        self.root = root
        self.root.title("Possibili cluster")
        self.lista_segmenti = lista_segmenti
        self.notebook = ttk.Notebook(self.root)
        self.cluster = cluster
        self.root2 = {}
        self.check_box = {}
        self.check_var = {}
        self.frame2 = {}
        self.table2 = {}

        for key in self.cluster.keys():
            # devo considerare pure il primo segmento che nel cluster non lo sto tenendo in conto
            if (len(self.cluster[key]) + 1) != len(lista_segmenti):
                continue
            cluster_frame = ttk.Frame(self.notebook)
            table = ttk.Treeview(cluster_frame)
            tupla = (
                "Segmento ID", "Misura ID", "Numero busoni acciaio", "Distanza centro busoni acciaio",
                "Distanza lato busoni acciaio",
                "Numero busoni alluminio", "Distanza centro busoni alluminio", "Distanza lato busoni alluminio",
                "Distanza fine sbarra lato busone", "Distanza sbarra muro")
            table["columns"] = tupla
            table.column("Segmento ID", anchor=tk.W, width=100, stretch=tk.NO)
            table.column("Misura ID", anchor=tk.W, width=100)
            table.column("Numero busoni acciaio", anchor=tk.W, width=100)
            table.column("Distanza centro busoni acciaio", anchor=tk.W, width=200)
            table.column("Distanza lato busoni acciaio", anchor=tk.W, width=200)
            table.column("Numero busoni alluminio", anchor=tk.W, width=200)
            table.column("Distanza centro busoni alluminio", anchor=tk.W, width=200)
            table.column("Distanza lato busoni alluminio", anchor=tk.W, width=200)
            table.column("Distanza fine sbarra lato busone", anchor=tk.W, width=200)
            table.column("Distanza sbarra muro", anchor=tk.W, width=200)

            table.heading("Segmento ID", anchor=tk.W, text="Segmento ID")
            table.heading("Misura ID", anchor=tk.W, text="Misura ID")
            table.heading("Numero busoni acciaio", anchor=tk.W, text="Numero busoni acciaio")
            table.heading("Distanza centro busoni acciaio", anchor=tk.W, text="Distanza centro busoni acciaio")
            table.heading("Distanza lato busoni acciaio", anchor=tk.W, text="Distanza lato busoni acciaio")
            table.heading("Numero busoni alluminio", anchor=tk.W, text="Numero busoni alluminio")
            table.heading("Distanza centro busoni alluminio", anchor=tk.W, text="Distanza centro busoni alluminio")
            table.heading("Distanza lato busoni alluminio", anchor=tk.W, text="Distanza lato busoni alluminio")
            table.heading("Distanza fine sbarra lato busone", anchor=tk.W, text="Distanza fine sbarra lato busone")
            table.heading("Distanza sbarra muro", anchor=tk.W, text="Distanza sbarra muro")
            tmp_misura_primo_seg: Misure_segmento = lista_segmenti[0][key]
            if tmp_misura_primo_seg.distanza_fine_sbarra_lato_busone == -1 and \
                    tmp_misura_primo_seg.distanza_muro == -1:
                data = (
                    tmp_misura_primo_seg.segmento.id, tmp_misura_primo_seg.id_misura, tmp_misura_primo_seg.n_busoni_acciaio,
                    tmp_misura_primo_seg.distanza_centro_busoni_acciaio,
                    tmp_misura_primo_seg.distanza_lato_busoni_acciaio, tmp_misura_primo_seg.n_busoni_alluminio,
                    tmp_misura_primo_seg.distanza_centro_busoni_alluminio,
                    tmp_misura_primo_seg.distanza_lato_busoni_alluminio, "-", "-")
            elif tmp_misura_primo_seg.distanza_fine_sbarra_lato_busone != -1 and \
                    tmp_misura_primo_seg.distanza_muro == -1:
                data = (
                    tmp_misura_primo_seg.segmento.id, tmp_misura_primo_seg.id_misura, tmp_misura_primo_seg.n_busoni_acciaio,
                    tmp_misura_primo_seg.distanza_centro_busoni_acciaio,
                    tmp_misura_primo_seg.distanza_lato_busoni_acciaio, tmp_misura_primo_seg.n_busoni_alluminio,
                    tmp_misura_primo_seg.distanza_centro_busoni_alluminio,
                    tmp_misura_primo_seg.distanza_lato_busoni_alluminio,
                    tmp_misura_primo_seg.distanza_fine_sbarra_lato_busone, "-")
            elif tmp_misura_primo_seg.distanza_fine_sbarra_lato_busone == -1 and \
                    tmp_misura_primo_seg.distanza_muro != -1:
                data = (
                    tmp_misura_primo_seg.segmento.id, tmp_misura_primo_seg.id_misura, tmp_misura_primo_seg.n_busoni_acciaio,
                    tmp_misura_primo_seg.distanza_centro_busoni_acciaio,
                    tmp_misura_primo_seg.distanza_lato_busoni_acciaio, tmp_misura_primo_seg.n_busoni_alluminio,
                    tmp_misura_primo_seg.distanza_centro_busoni_alluminio,
                    tmp_misura_primo_seg.distanza_lato_busoni_alluminio, "-", tmp_misura_primo_seg.distanza_muro)
            else:
                data = (
                    tmp_misura_primo_seg.segmento.id, tmp_misura_primo_seg.id_misura, tmp_misura_primo_seg.n_busoni_acciaio,
                    tmp_misura_primo_seg.distanza_centro_busoni_acciaio,
                    tmp_misura_primo_seg.distanza_lato_busoni_acciaio, tmp_misura_primo_seg.n_busoni_alluminio,
                    tmp_misura_primo_seg.distanza_centro_busoni_alluminio,
                    tmp_misura_primo_seg.distanza_lato_busoni_alluminio,
                    tmp_misura_primo_seg.distanza_fine_sbarra_lato_busone, tmp_misura_primo_seg.distanza_muro)

            table.insert("", tk.END, values=data)
            for key2, value2 in self.cluster[key].items():
                tmp: Misure_segmento = value2
                if tmp.distanza_fine_sbarra_lato_busone == -1 and \
                        tmp.distanza_muro == -1:
                    data = (tmp.segmento.id, tmp.id_misura, tmp.n_busoni_acciaio, tmp.distanza_centro_busoni_acciaio,
                            tmp.distanza_lato_busoni_acciaio, tmp.n_busoni_alluminio,
                            tmp.distanza_centro_busoni_alluminio, tmp.distanza_lato_busoni_alluminio, "-", "-")
                elif tmp.distanza_fine_sbarra_lato_busone != -1 and \
                        tmp.distanza_muro == -1:
                    data = (tmp.segmento.id, tmp.id_misura, tmp.n_busoni_acciaio, tmp.distanza_centro_busoni_acciaio,
                            tmp.distanza_lato_busoni_acciaio, tmp.n_busoni_alluminio,
                            tmp.distanza_centro_busoni_alluminio, tmp.distanza_lato_busoni_alluminio,
                            tmp.distanza_fine_sbarra_lato_busone, "-")
                elif tmp.distanza_fine_sbarra_lato_busone == -1 and \
                        tmp.distanza_muro != -1:
                    data = (tmp.segmento.id, tmp.id_misura, tmp.n_busoni_acciaio, tmp.distanza_centro_busoni_acciaio,
                            tmp.distanza_lato_busoni_acciaio, tmp.n_busoni_alluminio,
                            tmp.distanza_centro_busoni_alluminio, tmp.distanza_lato_busoni_alluminio, "-",
                            tmp.distanza_muro)
                else:
                    data = (tmp.segmento.id, tmp.id_misura, tmp.n_busoni_acciaio, tmp.distanza_centro_busoni_acciaio,
                            tmp.distanza_lato_busoni_acciaio, tmp.n_busoni_alluminio,
                            tmp.distanza_centro_busoni_alluminio, tmp.distanza_lato_busoni_alluminio,
                            tmp.distanza_fine_sbarra_lato_busone, tmp.distanza_muro)

                table.insert("", tk.END, values=data)

            self.check_var[key] = tk.BooleanVar()
            self.check_var[key].set(False)

            def on_checkbox_change(i):
                if self.check_var[i].get():
                    self.check_var[i].set(True)
                else:
                    self.check_var[i].set(False)
                if self.check_var[i].get():
                    self.root2[i].deiconify()
                else:
                    self.root2[i].withdraw()

                # Aggiungi una funzione per gestire la chiusura della finestra
                def on_closing():
                    self.check_var[i].set(False)
                    self.root2[i].withdraw()
                    return

                # Associa la funzione on_closing all'evento di chiusura della finestra
                self.root2[i].protocol("WM_DELETE_WINDOW", on_closing)

            # Aggiungi checkbox per ogni scheda
            self.root2[key] = tk.Tk()
            self.root2[key].title(f"Misure dei segmenti nel cluster {key}")
            self.root2[key].withdraw()
            self.frame2[key] = ttk.Frame(self.root2[key])
            self.frame2[key].pack(fill=tk.BOTH, expand=True)
            self.table2[key] = self.crea_segmenti_table(self.frame2[key], self.cluster[key], key, self.lista_segmenti)
            # Aggiungi una scrollbar alla finestr
            scrollbar = ttk.Scrollbar(self.frame2[key], orient=tk.VERTICAL, command=table.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            self.table2[key].configure(yscrollcommand=scrollbar.set)
            self.check_box[key] = ttk.Checkbutton(cluster_frame, text=f"Mostra misure dei segmenti per il cluster {key}",
                                             variable=self.check_var[key], command=lambda i=key: on_checkbox_change(i))
            self.check_box[key].pack(fill=tk.Y)

            table.pack(fill=tk.BOTH, expand=True)
            self.notebook.add(cluster_frame, text=f"Cluster {key}")
            self.notebook.pack(fill=tk.BOTH, expand=True)

        # Pulsante per tornare alla Finestra Principale
        back_button = ttk.Button(root, text="Chiudi", command=self.back_to_main)
        back_button.pack(pady=10)
        self.root.mainloop()
        root.protocol("WM_DELETE_WINDOW", self.back_to_main())

    def crea_segmenti_table(self, frame, cluster_i, i, lista_segmenti):
        primo_segmento: Misure_segmento = lista_segmenti[0][i]

        lista_buchi: list[float] = calcola_buchi(primo_segmento)
        columns = ("Segmento ID", "Misura ID")
        for index, col in enumerate(lista_buchi):
            columns = columns + (f"buco {index}",)

        tree = ttk.Treeview(frame, columns=columns)

        # Aggiungi colonne
        tmp2: tuple[str] = ("Segmento ID", "Misura ID",) + tuple(lista_buchi)
        for index, col in enumerate(tmp2):
            if index < 2:
                tree.column(col, anchor=tk.W, width=150)
                tree.heading(col, text=col, anchor=tk.W)
            else:
                tree.column(index, anchor=tk.W, width=150)
                tree.heading(index, text=f"Buco {index-1}", anchor=tk.W)

        data = (0, i,) + tuple(lista_buchi)
        tree.insert("", tk.END, values=data)

        for key, value in cluster_i.items():
            segmento: Misure_segmento = lista_segmenti[key][value.id_misura]
            lista_buchi: list[float] = calcola_buchi(segmento)
            data = (key, value.id_misura,) + tuple(lista_buchi)
            tree.insert("", tk.END, values=data)
        tree.pack(fill=tk.BOTH, expand=True)
        return tree

    def back_to_main(self):
        # Chiudi la Finestra 1 e torna alla Finestra Principale
        self.root.destroy()

from tkinter import messagebox
import core.tracciature.tracciatura as tr
import core.tracciature.muro_dx as md
import core.tracciature.muro_sx as ms
import core.tracciature.muro_sx_dx as msd
import core.tracciature.no_muro_sx_dx as nm
import copy


def calcola_risultati(segmento, l_tracciatura, distanza_minima, distanza_muro, l_muro, combo_var, numero_misure_diverse,
                      n_max_busoni_acciaio, n_min_busoni_acciaio, n_max_busoni_alluminio,
                      n_min_busoni_alluminio, min_distanza_fine_sbarra_lato_busone, max_distanza_fine_sbarra_lato_busone):
    # risultati del tipo
    risultati_busoni_diversi = {}

    if combo_var == "Tracciatura di uno spazio":
        for i in range(n_max_busoni_alluminio, n_min_busoni_alluminio, -1):
            tmp = tr.calcola_distanze_tracciatura(segmento, l_tracciatura, distanza_minima,
                                                  i)
            if tmp.id_misura != -1:
                risultati_busoni_diversi[i] = tmp

    elif 0 < segmento.angolo_dx < 90 and 0 < segmento.angolo_sx < 90:
        for j in range(min_distanza_fine_sbarra_lato_busone, max_distanza_fine_sbarra_lato_busone, 1):
            n_busoni_acciaio = n_min_busoni_acciaio
            n_busoni_alluminio = n_max_busoni_alluminio
            best = 0
            for i in range(0, numero_misure_diverse, 1):
                if combo_var == "Parte sinistra in prossimita del muro":
                    tmp = ms.calcola_distanze_sx_muro_acuti(l_muro, distanza_muro, segmento,
                                                            i + j, j, distanza_minima,
                                                            n_busoni_acciaio,
                                                            n_busoni_alluminio,
                                                            n_max_busoni_acciaio,
                                                            n_min_busoni_alluminio)
                    # tolgo il busone aggiunto nella spezzatura
                elif combo_var == "Parte destra in prossimita del muro":
                    tmp = md.calcola_distanze_dx_muro_acuti(l_muro, distanza_muro, segmento,
                                                            i + j, j, distanza_minima,
                                                            n_busoni_acciaio,
                                                            n_busoni_alluminio,
                                                            n_max_busoni_acciaio,
                                                            n_min_busoni_alluminio)
                elif combo_var == "Entrambe le parti in prossimita del muro":
                    tmp = msd.calcola_distanze_sx_dx_muro_acuti(l_muro, distanza_muro,
                                                                segmento,
                                                                i + j, j, distanza_minima,
                                                                n_busoni_acciaio,
                                                                n_busoni_alluminio,
                                                                n_max_busoni_acciaio,
                                                                n_min_busoni_alluminio)
                else:
                    tmp = nm.calcola_distanze_no_muro_acuti(segmento,
                                                            i + j, distanza_minima,
                                                            n_busoni_acciaio,
                                                            n_busoni_alluminio,
                                                            n_max_busoni_acciaio,
                                                            n_min_busoni_alluminio)
                if tmp.n_busoni_acciaio > 0:
                    risultati_busoni_diversi[i + j] = copy.copy(tmp)
                    risultati_busoni_diversi[i + j].n_busoni_alluminio -= 1
                    if combo_var == "Parte sinistra in prossimita del muro":
                        risultati_busoni_diversi[i + j].n_busoni_acciaio -= 1
                    if combo_var == "Parte destra in prossimita del muro":
                        risultati_busoni_diversi[i + j].n_busoni_acciaio -= 1
                    if combo_var == "Nessuna parte in prossimita del muro":
                        risultati_busoni_diversi[i + j].n_busoni_acciaio -= 2
                    n_busoni_acciaio = tmp.n_busoni_acciaio
                    n_busoni_alluminio = tmp.n_busoni_alluminio - 1
                else:
                    n_busoni_acciaio = best + 1
                    n_busoni_alluminio = n_max_busoni_alluminio
            if combo_var == "Nessuna parte in prossimita del muro":
                break
    elif 0 < segmento.angolo_dx < 90 and segmento.angolo_sx == 90:
        for j in range(min_distanza_fine_sbarra_lato_busone, max_distanza_fine_sbarra_lato_busone, 1):
            n_busoni_acciaio = n_min_busoni_acciaio
            n_busoni_alluminio = n_max_busoni_alluminio
            best = 0
            for i in range(0, numero_misure_diverse, 1):
                if combo_var == "Parte sinistra in prossimita del muro":
                    tmp = ms.calcola_distanze_sx_muro_sx_acuto_dx_retto(l_muro,
                                                                        distanza_muro,
                                                                        segmento,
                                                                        i + j, j,
                                                                        distanza_minima,
                                                                        n_busoni_acciaio,
                                                                        n_busoni_alluminio,
                                                                        n_max_busoni_acciaio,
                                                                        n_min_busoni_alluminio)
                elif combo_var == "Parte destra in prossimita del muro":
                    tmp = md.calcola_distanze_dx_muro_sx_acuto_dx_retto(l_muro,
                                                                        distanza_muro,
                                                                        segmento,
                                                                        i + j, j,
                                                                        distanza_minima,
                                                                        n_busoni_acciaio,
                                                                        n_busoni_alluminio, n_max_busoni_acciaio,
                                                                        n_min_busoni_alluminio)

                elif combo_var == "Entrambe le parti in prossimita del muro":
                    tmp = msd.calcola_distanze_sx_dx_muro_sx_acuto_dx_retto(l_muro,
                                                                            distanza_muro,
                                                                            segmento,
                                                                            i + j, j,
                                                                            distanza_minima,
                                                                            n_busoni_acciaio,
                                                                            n_busoni_alluminio,
                                                                            n_max_busoni_acciaio,
                                                                            n_min_busoni_alluminio)
                else:
                    tmp = nm.calcola_distanze_no_muro_sx_acuto_dx_retto(segmento,
                                                                        i + j,
                                                                        distanza_minima,
                                                                        n_busoni_acciaio,
                                                                        n_busoni_alluminio,
                                                                        n_max_busoni_acciaio,
                                                                        n_min_busoni_alluminio)
                if tmp.n_busoni_acciaio > 0:
                    risultati_busoni_diversi[i + j] = copy.copy(tmp)
                    risultati_busoni_diversi[i + j].n_busoni_alluminio -= 1
                    if combo_var == "Parte sinistra in prossimita del muro":
                        risultati_busoni_diversi[i + j].n_busoni_acciaio -= 1
                    if combo_var == "Nessuna parte in prossimita del muro":
                        risultati_busoni_diversi[i + j].n_busoni_acciaio -= 1
                    best = tmp.n_busoni_acciaio
                    n_busoni_acciaio = tmp.n_busoni_acciaio
                    n_busoni_alluminio = tmp.n_busoni_alluminio - 1
                else:
                    n_busoni_acciaio = best + 1
                    n_busoni_alluminio = n_max_busoni_alluminio
            if combo_var == "Nessuna parte in prossimita del muro":
                break
    elif segmento.angolo_dx == 90 and 0 < segmento.angolo_sx < 90:
        for j in range(min_distanza_fine_sbarra_lato_busone, max_distanza_fine_sbarra_lato_busone, 1):
            n_busoni_acciaio = n_min_busoni_acciaio
            n_busoni_alluminio = n_max_busoni_alluminio
            best = 0
            for i in range(0, numero_misure_diverse, 1):
                if combo_var == "Parte sinistra in prossimita del muro":
                    tmp = ms.calcola_distanze_sx_muro_sx_retto_dx_acuto(l_muro,
                                                                        distanza_muro,
                                                                        segmento,
                                                                        i + j, j,
                                                                        distanza_minima,
                                                                        n_busoni_acciaio,
                                                                        n_busoni_alluminio,
                                                                        n_max_busoni_acciaio,
                                                                        n_min_busoni_alluminio)
                elif combo_var == "Parte destra in prossimita del muro":
                    tmp = md.calcola_distanze_dx_muro_sx_retto_dx_acuto(l_muro,
                                                                        distanza_muro,
                                                                        segmento,
                                                                        i + j, j,
                                                                        distanza_minima,
                                                                        n_busoni_acciaio,
                                                                        n_busoni_alluminio,
                                                                        n_max_busoni_acciaio,
                                                                        n_min_busoni_alluminio)

                elif combo_var == "Entrambe le parti in prossimita del muro":
                    tmp = msd.calcola_distanze_sx_dx_muro_sx_retto_dx_acuto(l_muro,
                                                                            distanza_muro,
                                                                            segmento,
                                                                            i + j, j,
                                                                            distanza_minima,
                                                                            n_busoni_acciaio,
                                                                            n_busoni_alluminio,
                                                                            n_max_busoni_acciaio,
                                                                            n_min_busoni_alluminio)
                else:
                    tmp = nm.calcola_distanze_no_muro_sx_retto_dx_acuto(segmento,
                                                                        i + j,
                                                                        distanza_minima,
                                                                        n_busoni_acciaio,
                                                                        n_busoni_alluminio,
                                                                        n_max_busoni_acciaio,
                                                                        n_min_busoni_alluminio)
                if tmp.n_busoni_acciaio > 0:
                    risultati_busoni_diversi[i + j] = copy.copy(tmp)
                    risultati_busoni_diversi[i + j].n_busoni_alluminio -= 1
                    if combo_var == "Parte destra in prossimita del muro":
                        risultati_busoni_diversi[i + j].n_busoni_acciaio -= 1
                    if combo_var == "Nessuna parte in prossimita del muro":
                        risultati_busoni_diversi[i + j].n_busoni_acciaio -= 1
                    best = tmp.n_busoni_acciaio
                    n_busoni_acciaio = tmp.n_busoni_acciaio
                    n_busoni_alluminio = tmp.n_busoni_alluminio - 1
                else:
                    n_busoni_acciaio = best + 1
                    n_busoni_alluminio = n_max_busoni_alluminio
            if combo_var == "Nessuna parte in prossimita del muro":
                break
    elif segmento.angolo_dx == 90 and segmento.angolo_sx == 90:
        for j in range(min_distanza_fine_sbarra_lato_busone, max_distanza_fine_sbarra_lato_busone, 1):
            n_busoni_acciaio = n_min_busoni_acciaio
            n_busoni_alluminio = n_max_busoni_alluminio
            best = 0
            for i in range(0, numero_misure_diverse, 1):
                if combo_var == "Parte sinistra in prossimita del muro":
                    tmp = ms.calcola_distanze_sx_muro_retti(l_muro, distanza_muro, segmento,
                                                            i + j, j, distanza_minima,
                                                            n_busoni_acciaio,
                                                            n_busoni_alluminio,
                                                            n_max_busoni_acciaio,
                                                            n_min_busoni_alluminio)
                elif combo_var == "Parte destra in prossimita del muro":
                    tmp = md.calcola_distanze_dx_muro_retti(l_muro, distanza_muro, segmento,
                                                            i + j, j, distanza_minima,
                                                            n_busoni_acciaio,
                                                            n_busoni_alluminio,
                                                            n_max_busoni_acciaio,
                                                            n_min_busoni_alluminio)

                elif combo_var == "Entrambe le parti in prossimita del muro":
                    tmp = msd.calcola_distanze_sx_dx_muro_retti(l_muro, distanza_muro,
                                                                segmento,
                                                                i + j, j, distanza_minima,
                                                                n_busoni_acciaio,
                                                                n_busoni_alluminio,
                                                                n_max_busoni_acciaio,
                                                                n_min_busoni_alluminio)
                else:
                    tmp = nm.calcola_distanze_no_muro_retti(segmento,
                                                            i + j, distanza_minima,
                                                            n_busoni_acciaio,
                                                            n_busoni_alluminio,
                                                            n_max_busoni_acciaio,
                                                            n_min_busoni_alluminio)
                if tmp.n_busoni_acciaio > 0:
                    risultati_busoni_diversi[i + j] = copy.copy(tmp)
                    risultati_busoni_diversi[i + j].n_busoni_alluminio -= 1
                    best = tmp.n_busoni_acciaio
                    n_busoni_acciaio = tmp.n_busoni_acciaio
                    n_busoni_alluminio = tmp.n_busoni_alluminio - 1
                else:
                    n_busoni_acciaio = best + 1
                    n_busoni_alluminio = n_max_busoni_alluminio
            if combo_var == "Nessuna parte in prossimita del muro":
                break
    elif 180 > segmento.angolo_sx > 90 > segmento.angolo_dx > 0:
        for j in range(min_distanza_fine_sbarra_lato_busone, max_distanza_fine_sbarra_lato_busone, 1):
            n_busoni_acciaio = n_min_busoni_acciaio
            n_busoni_alluminio = n_max_busoni_alluminio
            best = 0
            for i in range(0, numero_misure_diverse, 1):
                if combo_var == "Parte sinistra in prossimita del muro":
                    tmp = ms.calcola_distanze_sx_muro_sx_ottuso_dx_acuto(l_muro,
                                                                         distanza_muro,
                                                                         segmento,
                                                                         i + j, j,
                                                                         distanza_minima,
                                                                         n_busoni_acciaio,
                                                                         n_busoni_alluminio,
                                                                         n_max_busoni_acciaio,
                                                                         n_min_busoni_alluminio)
                elif combo_var == "Parte destra in prossimita del muro":
                    tmp = md.calcola_distanze_dx_muro_sx_ottuso_dx_acuto(l_muro,
                                                                         distanza_muro,
                                                                         segmento,
                                                                         i + j, j,
                                                                         distanza_minima,
                                                                         n_busoni_acciaio,
                                                                         n_busoni_alluminio,
                                                                         n_max_busoni_acciaio,
                                                                         n_min_busoni_alluminio)
                elif combo_var == "Entrambe le parti in prossimita del muro":
                    tmp = msd.calcola_distanze_sx_dx_muro_sx_ottuso_dx_acuto(l_muro,
                                                                             distanza_muro,
                                                                             segmento,
                                                                             i + j, j,
                                                                             distanza_minima,
                                                                             n_busoni_acciaio,
                                                                             n_busoni_alluminio,
                                                                             n_max_busoni_acciaio,
                                                                             n_min_busoni_alluminio)
                else:
                    tmp = nm.calcola_distanze_no_muro_sx_ottuso_dx_acuto(segmento,
                                                                         i + j,
                                                                         distanza_minima,
                                                                         n_busoni_acciaio,
                                                                         n_busoni_alluminio,
                                                                         n_max_busoni_acciaio,
                                                                         n_min_busoni_alluminio)
                if tmp.n_busoni_acciaio > 0:
                    risultati_busoni_diversi[i + j] = copy.copy(tmp)
                    risultati_busoni_diversi[i + j].n_busoni_alluminio -= 1
                    if combo_var == "Parte sinistra in prossimita del muro":
                        risultati_busoni_diversi[i + j].n_busoni_acciaio -= 1
                    if combo_var == "Parte destra in prossimita del muro":
                        risultati_busoni_diversi[i + j].n_busoni_acciaio -= 1
                    if combo_var == "Nessuna parte in prossimita del muro":
                        risultati_busoni_diversi[i + j].n_busoni_acciaio -= 2
                    best = tmp.n_busoni_acciaio
                    n_busoni_acciaio = tmp.n_busoni_acciaio
                    n_busoni_alluminio = tmp.n_busoni_alluminio - 1
                else:
                    n_busoni_acciaio = best + 1
                    n_busoni_alluminio = n_max_busoni_alluminio
            if combo_var == "Nessuna parte in prossimita del muro":
                break
    elif 90 < segmento.angolo_sx < 180 and 90 < segmento.angolo_dx < 180:
        for j in range(min_distanza_fine_sbarra_lato_busone, max_distanza_fine_sbarra_lato_busone, 1):
            n_busoni_acciaio = n_min_busoni_acciaio
            n_busoni_alluminio = n_max_busoni_alluminio
            best = 0
            for i in range(0, numero_misure_diverse, 1):
                if combo_var == "Parte sinistra in prossimita del muro":
                    tmp = ms.calcola_distanze_sx_muro_ottusi(l_muro, distanza_muro,
                                                             segmento,
                                                             i + j, j, distanza_minima,
                                                             n_busoni_acciaio,
                                                             n_busoni_alluminio,
                                                             n_max_busoni_acciaio,
                                                             n_min_busoni_alluminio)
                elif combo_var == "Parte destra in prossimita del muro":
                    tmp = md.calcola_distanze_dx_muro_ottusi(l_muro, distanza_muro,
                                                             segmento,
                                                             i + j, j, distanza_minima,
                                                             n_busoni_acciaio,
                                                             n_busoni_alluminio,
                                                             n_max_busoni_acciaio,
                                                             n_min_busoni_alluminio)
                elif combo_var == "Entrambe le parti in prossimita del muro":
                    tmp = msd.calcola_distanze_sx_dx_muro_ottusi(l_muro, distanza_muro,
                                                                 segmento,
                                                                 i + j, j, distanza_minima,
                                                                 n_busoni_acciaio,
                                                                 n_busoni_alluminio,
                                                                 n_max_busoni_acciaio,
                                                                 n_min_busoni_alluminio)
                else:
                    tmp = nm.calcola_distanze_no_muro_ottusi(segmento,
                                                             i + j, distanza_minima,
                                                             n_busoni_acciaio,
                                                             n_busoni_alluminio,
                                                             n_max_busoni_acciaio,
                                                             n_min_busoni_alluminio)
                if tmp.n_busoni_acciaio > 0:
                    risultati_busoni_diversi[i + j] = copy.copy(tmp)
                    risultati_busoni_diversi[i + j].n_busoni_alluminio -= 1
                    if combo_var == "Parte sinistra in prossimita del muro":
                        risultati_busoni_diversi[i + j].n_busoni_acciaio -= 1
                    if combo_var == "Parte destra in prossimita del muro":
                        risultati_busoni_diversi[i + j].n_busoni_acciaio -= 1
                    if combo_var == "Nessuna parte in prossimita del muro":
                        risultati_busoni_diversi[i + j].n_busoni_acciaio -= 2
                    best = tmp.n_busoni_acciaio
                    n_busoni_acciaio = tmp.n_busoni_acciaio
                    n_busoni_alluminio = tmp.n_busoni_alluminio - 1
                else:
                    n_busoni_acciaio = best + 1
                    n_busoni_alluminio = n_max_busoni_alluminio
            if combo_var == "Nessuna parte in prossimita del muro":
                break
    elif 0 < segmento.angolo_sx < 90 < segmento.angolo_dx < 180:
        for j in range(min_distanza_fine_sbarra_lato_busone, max_distanza_fine_sbarra_lato_busone, 1):
            n_busoni_acciaio = n_min_busoni_acciaio
            n_busoni_alluminio = n_max_busoni_alluminio
            best = 0
            for i in range(0, numero_misure_diverse, 1):
                if combo_var == "Parte sinistra in prossimita del muro":
                    tmp = ms.calcola_distanze_sx_muro_sx_acuto_dx_ottuso(l_muro,
                                                                         distanza_muro,
                                                                         segmento,
                                                                         i + j, j,
                                                                         distanza_minima,
                                                                         n_busoni_acciaio,
                                                                         n_busoni_alluminio,
                                                                         n_max_busoni_acciaio,
                                                                         n_min_busoni_alluminio)
                elif combo_var == "Parte destra in prossimita del muro":
                    tmp = md.calcola_distanze_dx_muro_sx_acuto_dx_ottuso(l_muro,
                                                                         distanza_muro,
                                                                         segmento,
                                                                         i + j, j,
                                                                         distanza_minima,
                                                                         n_busoni_acciaio,
                                                                         n_busoni_alluminio,
                                                                         n_max_busoni_acciaio,
                                                                         n_min_busoni_alluminio)
                elif combo_var == "Entrambe le parti in prossimita del muro":
                    tmp = msd.calcola_distanze_sx_dx_muro_sx_acuto_dx_ottuso(l_muro,
                                                                             distanza_muro,
                                                                             segmento,
                                                                             i + j, j,
                                                                             distanza_minima,
                                                                             n_busoni_acciaio,
                                                                             n_busoni_alluminio,
                                                                             n_max_busoni_acciaio,
                                                                             n_min_busoni_alluminio)
                else:
                    tmp = nm.calcola_distanze_no_muro_sx_acuto_dx_ottuso(segmento,
                                                                         i + j,
                                                                         distanza_minima,
                                                                         n_busoni_acciaio,
                                                                         n_busoni_alluminio,
                                                                         n_max_busoni_acciaio,
                                                                         n_min_busoni_alluminio)
                if tmp.n_busoni_acciaio > 0:
                    risultati_busoni_diversi[i + j] = copy.copy(tmp)
                    risultati_busoni_diversi[i + j].n_busoni_alluminio -= 1
                    if combo_var == "Parte sinistra in prossimita del muro":
                        risultati_busoni_diversi[i + j].n_busoni_acciaio -= 1
                    if combo_var == "Parte destra in prossimita del muro":
                        risultati_busoni_diversi[i + j].n_busoni_acciaio -= 1
                    if combo_var == "Nessuna parte in prossimita del muro":
                        risultati_busoni_diversi[i + j].n_busoni_acciaio -= 2
                    best = tmp.n_busoni_acciaio
                    n_busoni_acciaio = tmp.n_busoni_acciaio
                    n_busoni_alluminio = tmp.n_busoni_alluminio - 1
                else:
                    n_busoni_acciaio = best + 1
                    n_busoni_alluminio = n_max_busoni_alluminio
            if combo_var == "Nessuna parte in prossimita del muro":
                break
    elif segmento.angolo_sx == 90 and 90 < segmento.angolo_dx < 180:
        for j in range(min_distanza_fine_sbarra_lato_busone, max_distanza_fine_sbarra_lato_busone, 1):
            n_busoni_acciaio = n_min_busoni_acciaio
            n_busoni_alluminio = n_max_busoni_alluminio
            best = 0
            for i in range(0, numero_misure_diverse, 1):
                if combo_var == "Parte sinistra in prossimita del muro":
                    tmp = ms.calcola_distanze_sx_muro_sx_retto_dx_ottuso(l_muro,
                                                                         distanza_muro,
                                                                         segmento,
                                                                         i + j, j,
                                                                         distanza_minima,
                                                                         n_busoni_acciaio,
                                                                         n_busoni_alluminio,
                                                                         n_max_busoni_acciaio,
                                                                         n_min_busoni_alluminio)
                elif combo_var == "Parte destra in prossimita del muro":
                    tmp = md.calcola_distanze_dx_muro_sx_retto_dx_ottuso(l_muro,
                                                                         distanza_muro,
                                                                         segmento,
                                                                         i + j, j,
                                                                         distanza_minima,
                                                                         n_busoni_acciaio,
                                                                         n_busoni_alluminio,
                                                                         n_max_busoni_acciaio,
                                                                         n_min_busoni_alluminio)
                elif combo_var == "Entrambe le parti in prossimita del muro":
                    tmp = msd.calcola_distanze_sx_dx_muro_sx_retto_dx_ottuso(l_muro,
                                                                             distanza_muro,
                                                                             segmento,
                                                                             i + j, j,
                                                                             distanza_minima,
                                                                             n_busoni_acciaio,
                                                                             n_busoni_alluminio,
                                                                             n_max_busoni_acciaio,
                                                                             n_min_busoni_alluminio)
                else:
                    tmp = nm.calcola_distanze_no_muro_sx_retto_dx_ottuso(segmento,
                                                                         i + j,
                                                                         distanza_minima,
                                                                         n_busoni_acciaio,
                                                                         n_busoni_alluminio,
                                                                         n_max_busoni_acciaio,
                                                                         n_min_busoni_alluminio)
                if tmp.n_busoni_acciaio > 0:
                    risultati_busoni_diversi[i + j] = copy.copy(tmp)
                    risultati_busoni_diversi[i + j].n_busoni_alluminio -= 1
                    if combo_var == "Parte sinistra in prossimita del muro":
                        risultati_busoni_diversi[i + j].n_busoni_acciaio -= 1
                    if combo_var == "Nessuna parte in prossimita del muro":
                        risultati_busoni_diversi[i + j].n_busoni_acciaio -= 1
                    best = tmp.n_busoni_acciaio
                    n_busoni_acciaio = tmp.n_busoni_acciaio
                    n_busoni_alluminio = tmp.n_busoni_alluminio - 1
                else:
                    n_busoni_acciaio = best + 1
                    n_busoni_alluminio = n_max_busoni_alluminio
            if combo_var == "Nessuna parte in prossimita del muro":
                break
    elif 180 > segmento.angolo_sx > 90 == segmento.angolo_dx:
        for j in range(min_distanza_fine_sbarra_lato_busone, max_distanza_fine_sbarra_lato_busone, 1):
            n_busoni_acciaio = n_min_busoni_acciaio
            n_busoni_alluminio = n_max_busoni_alluminio
            best = 0
            for i in range(0, numero_misure_diverse, 1):
                if combo_var == "Parte sinistra in prossimita del muro":
                    tmp = ms.calcola_distanze_sx_muro_sx_ottuso_dx_retto(l_muro,
                                                                         distanza_muro,
                                                                         segmento,
                                                                         i + j, j,
                                                                         distanza_minima,
                                                                         n_busoni_acciaio,
                                                                         n_busoni_alluminio,
                                                                         n_max_busoni_acciaio,
                                                                         n_min_busoni_alluminio)
                elif combo_var == "Parte destra in prossimita del muro":
                    tmp = md.calcola_distanze_dx_muro_sx_ottuso_dx_retto(l_muro,
                                                                         distanza_muro,
                                                                         segmento,
                                                                         i + j, j,
                                                                         distanza_minima,
                                                                         n_busoni_acciaio,
                                                                         n_busoni_alluminio,
                                                                         n_max_busoni_acciaio,
                                                                         n_min_busoni_alluminio)
                elif combo_var == "Entrambe le parti in prossimita del muro":
                    tmp = msd.calcola_distanze_sx_dx_muro_sx_ottuso_dx_retto(l_muro,
                                                                             distanza_muro,
                                                                             segmento,
                                                                             i + j, j,
                                                                             distanza_minima,
                                                                             n_busoni_acciaio,
                                                                             n_busoni_alluminio,
                                                                             n_max_busoni_acciaio,
                                                                             n_min_busoni_alluminio)
                else:
                    tmp = nm.calcola_distanze_no_muro_sx_ottuso_dx_retto(segmento,
                                                                         i + j,
                                                                         distanza_minima,
                                                                         n_busoni_acciaio,
                                                                         n_busoni_alluminio,
                                                                         n_max_busoni_acciaio,
                                                                         n_min_busoni_alluminio)
                if tmp.n_busoni_acciaio > 0:
                    risultati_busoni_diversi[i + j] = copy.copy(tmp)
                    risultati_busoni_diversi[i + j].n_busoni_alluminio -= 1
                    if combo_var == "Parte destra in prossimita del muro":
                        risultati_busoni_diversi[i + j].n_busoni_acciaio -= 1
                    if combo_var == "Nessuna parte in prossimita del muro":
                        risultati_busoni_diversi[i + j].n_busoni_acciaio -= 1
                    best = tmp.n_busoni_acciaio
                    n_busoni_acciaio = tmp.n_busoni_acciaio
                    n_busoni_alluminio = tmp.n_busoni_alluminio - 1
                else:
                    n_busoni_acciaio = best + 1
                    n_busoni_alluminio = n_max_busoni_alluminio
            if combo_var == "Nessuna parte in prossimita del muro":
                break
    else:
        messagebox.showerror("Errore", "Angoli devono essere minori di 180 gradi")
        return
    # Otterrò come risultato risultati_busoni_diversi[0] .. risultati_busoni_diversi[4]
    # Ogni indice contiene un oggetto Misure_segmento
    # posizione_centro_sx = Misure_segmento
    # posizione_centro_dx = risultati[1]
    # numero_busoni_acc = risultati[2]
    # distanza_punto_busoni_acc = risultati[3]
    # distanza_completa_busoni_acc = risultati[4]
    # numero_busoni_all = risultati[5]
    # distanza_punto_busoni_all = risultati[6]
    # distanza_completa_busoni_all = risultati[7]
    return risultati_busoni_diversi
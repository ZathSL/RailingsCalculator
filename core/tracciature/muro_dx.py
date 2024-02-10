# TODO: PARTE DESTRA A RIDOSSO DEL MURO E L'ALTRA PARTE COLLEGATA
# TODO: Caso 1 - angolo sx < 90 AND angolo dx < 90
# 3 cm dal muro e inizia la sbarra, 2 cm e inizia il busone grosso
# mezzo busone grosso e c'è il centro del primo busone
from core.classes.misure_segmento import Misure_segmento
from core.classes.segmento import Segmento
import numpy as np
import core.tracciature.tracciatura as tr


def calcola_distanze_dx_muro_acuti(l_muro, distanza_muro, segmento, id_misura, distanza_fine_sbarra_lato_busone,
                                   distanza_minima,
                                   n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    l_esterna = l_muro - distanza_muro
    new_segmento = Segmento(segmento.id, l_esterna, segmento.spessore_sbarra, segmento.angolo_sx,
                            segmento.angolo_dx, segmento.l_busone_acciaio, segmento.l_busone_alluminio,
                            segmento.profondita_busone_alluminio)
    # Angolo dx
    l_sbarra_tracciatura = new_segmento.l_esterna - new_segmento.posizione_centro_spezzatura_dx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio / 2

    # Angolo sx
    l_sbarra_tracciatura -= new_segmento.posizione_centro_spezzatura_sx
    diagonale_rettangolo = np.sqrt(
        np.square(new_segmento.l_busone_alluminio) + np.square(new_segmento.profondita_busone_alluminio))
    l_sbarra_tracciatura -= diagonale_rettangolo / 2
    l_sbarra_tracciatura += new_segmento.l_busone_acciaio / 2

    # Tracciatura della lunghezza con busoni grossi e busoni piccoli
    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, new_segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(new_segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_muro, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, False, True)


# TODO: Caso 1 - angolo sx = 90 AND angolo dx = 90
def calcola_distanze_dx_muro_retti(l_muro, distanza_muro, segmento, id_misura, distanza_fine_sbarra_lato_busone,
                                   distanza_minima,
                                   n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    l_esterna = l_muro - distanza_muro
    new_segmento = Segmento(segmento.id, l_esterna, segmento.spessore_sbarra, segmento.angolo_sx, segmento.angolo_dx,
                            segmento.l_busone_acciaio, segmento.l_busone_alluminio,
                            segmento.profondita_busone_alluminio)

    # Angolo sx (per i retti no muro potrei considerare la tracciatura da inizio sbarra
    # l_sbarra_tracciatura = new_segmento.l_esterna - distanza_fine_sbarra_lato_busone
    # l_sbarra_tracciatura -= new_segmento.l_busone_acciaio/2
    # Angolo dx
    l_sbarra_tracciatura = new_segmento.l_esterna - distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio / 2

    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, new_segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)
    return Misure_segmento(new_segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_muro, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, False, True)


# TODO: Caso 1 - angolo sx > 90 AND angolo dx > 90
def calcola_distanze_dx_muro_ottusi(l_muro, distanza_muro, segmento, id_misura, distanza_fine_sbarra_lato_busone,
                                    distanza_minima,
                                    n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    l_esterna = l_muro - distanza_muro
    new_segmento = Segmento(segmento.id, l_esterna, segmento.spessore_sbarra, segmento.angolo_sx,
                            segmento.angolo_dx, segmento.l_busone_acciaio, segmento.l_busone_alluminio,
                            segmento.profondita_busone_alluminio)

    # Angolo sx
    l_sbarra_tracciatura = new_segmento.l_esterna + new_segmento.posizione_centro_spezzatura_sx
    diagonale_rettangolo = np.sqrt(
        np.square(new_segmento.l_busone_alluminio) + np.square(new_segmento.profondita_busone_alluminio))
    l_sbarra_tracciatura -= diagonale_rettangolo / 2
    l_sbarra_tracciatura += new_segmento.l_busone_acciaio / 2
    # Angolo dx
    l_sbarra_tracciatura += new_segmento.posizione_centro_spezzatura_dx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio / 2

    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, new_segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(new_segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_muro, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, False, True)


# TODO: Caso 1 - angolo sx < 90 AND angolo dx = 90
def calcola_distanze_dx_muro_sx_acuto_dx_retto(l_muro, distanza_muro, segmento, id_misura,
                                               distanza_fine_sbarra_lato_busone, distanza_minima,
                                               n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                               n_min_busoni_alluminio):
    l_esterna = l_muro - distanza_muro
    new_segmento = Segmento(segmento.id, l_esterna, segmento.spessore_sbarra, segmento.angolo_sx,
                            segmento.angolo_dx, segmento.l_busone_acciaio, segmento.l_busone_alluminio,
                            segmento.profondita_busone_alluminio)

    # Angolo sx
    l_sbarra_tracciatura = new_segmento.l_esterna - new_segmento.posizione_centro_spezzatura_sx
    diagonale_rettangolo = np.sqrt(
        np.square(new_segmento.l_busone_alluminio) + np.square(new_segmento.profondita_busone_alluminio))
    l_sbarra_tracciatura -= diagonale_rettangolo / 2
    l_sbarra_tracciatura += new_segmento.l_busone_acciaio / 2
    # Angolo dx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio / 2

    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, new_segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(new_segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_muro, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, False, True)


# TODO: Caso 1 - angolo sx < 90 AND angolo dx > 90
def calcola_distanze_dx_muro_sx_acuto_dx_ottuso(l_muro, distanza_muro, segmento, id_misura,
                                                distanza_fine_sbarra_lato_busone, distanza_minima,
                                                n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                n_min_busoni_alluminio):
    l_esterna = l_muro - distanza_muro
    new_segmento = Segmento(segmento.id, l_esterna, segmento.spessore_sbarra, segmento.angolo_sx,
                            segmento.angolo_dx, segmento.l_busone_acciaio, segmento.l_busone_alluminio,
                            segmento.profondita_busone_alluminio)

    # Angolo sx
    l_sbarra_tracciatura = new_segmento.l_esterna - new_segmento.posizione_centro_spezzatura_sx
    diagonale_rettangolo = np.sqrt(
        np.square(new_segmento.l_busone_alluminio) + np.square(new_segmento.profondita_busone_alluminio))
    l_sbarra_tracciatura -= diagonale_rettangolo / 2
    l_sbarra_tracciatura += new_segmento.l_busone_acciaio / 2
    # Angolo dx
    l_sbarra_tracciatura += new_segmento.posizione_centro_spezzatura_dx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio / 2

    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, new_segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(new_segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_muro, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, False, True)


# TODO: Caso 1 - angolo sx = 90 AND angolo dx > 90
def calcola_distanze_dx_muro_sx_retto_dx_ottuso(l_muro, distanza_muro, segmento, id_misura,
                                                distanza_fine_sbarra_lato_busone, distanza_minima,
                                                n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                n_min_busoni_alluminio):
    l_esterna = l_muro - distanza_muro
    new_segmento = Segmento(segmento.id, l_esterna, segmento.spessore_sbarra, segmento.angolo_sx,
                            segmento.angolo_dx, segmento.l_busone_acciaio, segmento.l_busone_alluminio,
                            segmento.profondita_busone_alluminio)

    # Angolo sx
    # l_sbarra_tracciatura = new_segmento.l_esterna - distanza_fine_sbarra_lato_busone
    # l_sbarra_tracciatura -= new_segmento.l_busone_acciaio/2
    # Angolo dx
    l_sbarra_tracciatura = new_segmento.l_esterna + new_segmento.posizione_centro_spezzatura_dx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio / 2

    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, new_segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(new_segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_muro, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, False, True)


# TODO: Caso 1 - angolo sx = 90 AND angolo dx < 90
def calcola_distanze_dx_muro_sx_retto_dx_acuto(l_muro, distanza_muro, segmento, id_misura,
                                               distanza_fine_sbarra_lato_busone, distanza_minima,
                                               n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                               n_min_busoni_alluminio):
    l_esterna = l_muro - distanza_muro
    new_segmento = Segmento(segmento.id, l_esterna, segmento.spessore_sbarra, segmento.angolo_sx,
                            segmento.angolo_dx, segmento.l_busone_acciaio, segmento.l_busone_alluminio,
                            segmento.profondita_busone_alluminio)

    # Angolo sx
    # Angolo dx
    l_sbarra_tracciatura = new_segmento.l_esterna - new_segmento.posizione_centro_spezzatura_dx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio / 2

    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, new_segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(new_segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_muro, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, False, True)


# TODO: Caso 1 - angolo sx > 90 AND angolo dx = 90
def calcola_distanze_dx_muro_sx_ottuso_dx_retto(l_muro, distanza_muro, segmento, id_misura,
                                                distanza_fine_sbarra_lato_busone, distanza_minima,
                                                n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                n_min_busoni_alluminio):
    l_esterna = l_muro - distanza_muro
    new_segmento = Segmento(segmento.id, l_esterna, segmento.spessore_sbarra, segmento.angolo_sx,
                            segmento.angolo_dx, segmento.l_busone_acciaio, segmento.l_busone_alluminio,
                            segmento.profondita_busone_alluminio)

    # Angolo sx
    l_sbarra_tracciatura = new_segmento.l_esterna + new_segmento.posizione_centro_spezzatura_sx
    diagonale_rettangolo = np.sqrt(
        np.square(new_segmento.l_busone_alluminio) + np.square(new_segmento.profondita_busone_alluminio))
    l_sbarra_tracciatura += diagonale_rettangolo / 2
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio / 2
    # Angolo dx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio / 2
    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, new_segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(new_segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_muro, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, False, True)


# TODO: Caso 1 - angolo sx > 90 AND angolo dx < 90
def calcola_distanze_dx_muro_sx_ottuso_dx_acuto(l_muro, distanza_muro, segmento, id_misura,
                                                distanza_fine_sbarra_lato_busone, distanza_minima,
                                                n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                n_min_busoni_alluminio):
    l_esterna = l_muro - distanza_muro
    new_segmento = Segmento(segmento.id, l_esterna, segmento.spessore_sbarra, segmento.angolo_sx,
                            segmento.angolo_dx, segmento.l_busone_acciaio, segmento.l_busone_alluminio,
                            segmento.profondita_busone_alluminio)

    # Angolo sx
    l_sbarra_tracciatura = new_segmento.l_esterna + new_segmento.posizione_centro_spezzatura_sx
    diagonale_rettangolo = np.sqrt(
        np.square(new_segmento.l_busone_alluminio) + np.square(new_segmento.profondita_busone_alluminio))
    l_sbarra_tracciatura -= diagonale_rettangolo / 2
    l_sbarra_tracciatura += new_segmento.l_busone_acciaio / 2
    # Angolo dx
    l_sbarra_tracciatura -= new_segmento.posizione_centro_spezzatura_dx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio / 2

    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, new_segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(new_segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_muro, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, False, True)

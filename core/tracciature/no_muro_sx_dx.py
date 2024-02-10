# TODO: PARTE SINISTRA A RIDOSSO DEL MURO E L'ALTRA PARTE COLLEGATA
# TODO: Caso 1 - angolo sx < 90 AND angolo dx < 90
#3 cm dal muro e inizia la sbarra, 2 cm e inizia il busone grosso
#mezzo busone grosso e c'è il centro del primo busone
import numpy as np
import core.tracciature.tracciatura as tr
from core.classes.misure_segmento import Misure_segmento


def calcola_distanze_no_muro_acuti(segmento, id_misura, distanza_minima,
                                   n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    # Angolo sx
    l_sbarra_tracciatura = segmento.l_esterna - segmento.posizione_centro_spezzatura_sx
    diagonale_rettangolo = np.sqrt(
        np.square(segmento.l_busone_alluminio) + np.square(segmento.profondita_busone_alluminio))
    l_sbarra_tracciatura -= diagonale_rettangolo/2
    l_sbarra_tracciatura += segmento.l_busone_acciaio/2
    # Angolo dx
    l_sbarra_tracciatura -= segmento.posizione_centro_spezzatura_dx
    l_sbarra_tracciatura -= diagonale_rettangolo/2
    l_sbarra_tracciatura += segmento.l_busone_acciaio/2

    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(segmento, id_misura, -1, -1, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, False, False)

# TODO: Caso 1 - angolo sx = 90 AND angolo dx = 90
# segmento.l_esterna è la distanza interna tra busone
# grosso e busone grosso
def calcola_distanze_no_muro_retti(segmento, id_misura, distanza_minima,
                                   n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    l_sbarra_tracciatura = segmento.l_esterna

    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(segmento, id_misura, -1, -1, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, False, False)


# TODO: Caso 1 - angolo sx > 90 AND angolo dx > 90
def calcola_distanze_no_muro_ottusi(segmento, id_misura, distanza_minima,
                                    n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    # Angolo sx
    l_sbarra_tracciatura = segmento.l_esterna + segmento.posizione_centro_spezzatura_sx
    diagonale_rettangolo = np.sqrt(
        np.square(segmento.l_busone_alluminio) + np.square(segmento.profondita_busone_alluminio))
    l_sbarra_tracciatura -= diagonale_rettangolo/2
    l_sbarra_tracciatura += segmento.l_busone_acciaio/2
    # Angolo dx
    l_sbarra_tracciatura += segmento.posizione_centro_spezzatura_dx
    l_sbarra_tracciatura -= diagonale_rettangolo/2
    l_sbarra_tracciatura += segmento.l_busone_acciaio/2

    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(segmento, id_misura, -1, -1, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, False, False)


# TODO: Caso 1 - angolo sx < 90 AND angolo dx = 90
def calcola_distanze_no_muro_sx_acuto_dx_retto(segmento, id_misura, distanza_minima,
                                               n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    # Angolo sx
    l_sbarra_tracciatura = segmento.l_esterna - segmento.posizione_centro_spezzatura_sx
    diagonale_rettangolo = np.sqrt(
        np.square(segmento.l_busone_alluminio) + np.square(segmento.profondita_busone_alluminio))
    l_sbarra_tracciatura -= diagonale_rettangolo/2
    l_sbarra_tracciatura += segmento.l_busone_acciaio/2
    # Angolo dx

    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(segmento, id_misura, -1, -1, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, False, False)

# TODO: Caso 1 - angolo sx < 90 AND angolo dx > 90
def calcola_distanze_no_muro_sx_acuto_dx_ottuso(segmento, id_misura, distanza_minima,
                                                n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    # Angolo sx
    l_sbarra_tracciatura = segmento.l_esterna - segmento.posizione_centro_spezzatura_sx
    diagonale_rettangolo = np.sqrt(
        np.square(segmento.l_busone_alluminio) + np.square(segmento.profondita_busone_alluminio))
    l_sbarra_tracciatura -= diagonale_rettangolo/2
    l_sbarra_tracciatura += segmento.l_busone_acciaio/2
    # Angolo dx
    l_sbarra_tracciatura += segmento.posizione_centro_spezzatura_dx
    l_sbarra_tracciatura -= diagonale_rettangolo/2
    l_sbarra_tracciatura += segmento.l_busone_acciaio/2

    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(segmento, id_misura, -1, -1, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, False, False)


# TODO: Caso 1 - angolo sx = 90 AND angolo dx > 90
def calcola_distanze_no_muro_sx_retto_dx_ottuso(segmento, id_misura, distanza_minima,
                                                n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    # Angolo sx
    # Angolo dx
    l_sbarra_tracciatura = segmento.l_esterna + segmento.posizione_centro_spezzatura_dx
    diagonale_rettangolo = np.sqrt(
        np.square(segmento.l_busone_alluminio) + np.square(segmento.profondita_busone_alluminio))
    l_sbarra_tracciatura -= diagonale_rettangolo/2
    l_sbarra_tracciatura += segmento.l_busone_acciaio/2

    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(segmento, id_misura, -1, -1, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, False, False)


# TODO: Caso 1 - angolo sx = 90 AND angolo dx < 90
def calcola_distanze_no_muro_sx_retto_dx_acuto(segmento, id_misura, distanza_minima,
                                               n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    # Angolo sx
    # Angolo dx
    l_sbarra_tracciatura = segmento.l_esterna - segmento.posizione_centro_spezzatura_dx
    diagonale_rettangolo = np.sqrt(
        np.square(segmento.l_busone_alluminio) + np.square(segmento.profondita_busone_alluminio))
    l_sbarra_tracciatura -= diagonale_rettangolo/2
    l_sbarra_tracciatura += segmento.l_busone_acciaio/2

    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(segmento, id_misura, -1, -1, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, False, False)


# TODO: Caso 1 - angolo sx > 90 AND angolo dx = 90
def calcola_distanze_no_muro_sx_ottuso_dx_retto(segmento, id_misura, distanza_minima,
                                                n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    # Angolo sx
    l_sbarra_tracciatura = segmento.l_esterna + segmento.posizione_centro_spezzatura_sx
    diagonale_rettangolo = np.sqrt(
        np.square(segmento.l_busone_alluminio) + np.square(segmento.profondita_busone_alluminio))
    l_sbarra_tracciatura -= diagonale_rettangolo/2
    l_sbarra_tracciatura += segmento.l_busone_acciaio/2
    # Angolo dx


    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(segmento, id_misura, -1, -1, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, False, False)


# TODO: Caso 1 - angolo sx > 90 AND angolo dx < 90
def calcola_distanze_no_muro_sx_ottuso_dx_acuto(segmento, id_misura, distanza_minima,
                                                n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    # Angolo sx
    l_sbarra_tracciatura = segmento.l_esterna + segmento.posizione_centro_spezzatura_sx
    diagonale_rettangolo = np.sqrt(
        np.square(segmento.l_busone_alluminio) + np.square(segmento.profondita_busone_alluminio))
    l_sbarra_tracciatura -= diagonale_rettangolo/2
    l_sbarra_tracciatura += segmento.l_busone_acciaio/2
    # Angolo dx
    l_sbarra_tracciatura -= segmento.posizione_centro_spezzatura_dx
    l_sbarra_tracciatura -= diagonale_rettangolo/2
    l_sbarra_tracciatura += segmento.l_busone_acciaio/2

    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(segmento, id_misura, -1, -1, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, False, False)

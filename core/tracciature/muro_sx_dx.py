# TODO: PARTE SINISTRA A RIDOSSO DEL MURO E L'ALTRA PARTE COLLEGATA
# TODO: Caso 1 - angolo sx < 90 AND angolo dx < 90
import core.tracciature.tracciatura as tr
from core.classes.misure_segmento import Misure_segmento
from core.classes.segmento import Segmento


def calcola_distanze_sx_dx_muro_acuti(l_muro, distanza_muro, segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_minima,
                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    l_esterna = l_muro - 2*distanza_muro
    new_segmento = Segmento(segmento.id, l_esterna, segmento.spessore_sbarra, segmento.angolo_sx,
                            segmento.angolo_dx, segmento.l_busone_acciaio, segmento.l_busone_alluminio,
                            segmento.profondita_busone_alluminio)
    # Angolo sx
    l_sbarra_tracciatura = new_segmento.l_esterna - new_segmento.posizione_centro_spezzatura_sx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio/2
    # Angolo dx
    l_sbarra_tracciatura -= new_segmento.posizione_centro_spezzatura_dx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio/2

    # Tracciatura della lunghezza con busoni grossi e busoni piccoli
    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, new_segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(new_segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_muro, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, True, True)


# TODO: Caso 1 - angolo sx = 90 AND angolo dx = 90
def calcola_distanze_sx_dx_muro_retti(l_muro, distanza_muro, segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_minima,
                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    l_esterna = l_muro - 2*distanza_muro
    new_segmento = Segmento(segmento.id, l_esterna, segmento.spessore_sbarra, segmento.angolo_sx,
                            segmento.angolo_dx, segmento.l_busone_acciaio, segmento.l_busone_alluminio,
                            segmento.profondita_busone_alluminio)
    # Angolo sx
    l_sbarra_tracciatura = new_segmento.l_esterna - distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio/2
    # Angolo dx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio/2

    # Tracciatura della lunghezza con busoni grossi e busoni piccoli
    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, new_segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(new_segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_muro, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, True, True)


# TODO: Caso 1 - angolo sx > 90 AND angolo dx > 90
def calcola_distanze_sx_dx_muro_ottusi(l_muro, distanza_muro, segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_minima,
                                       n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    l_esterna = l_muro - 2*distanza_muro
    new_segmento = Segmento(segmento.id, l_esterna, segmento.spessore_sbarra, segmento.angolo_sx,
                            segmento.angolo_dx, segmento.l_busone_acciaio, segmento.l_busone_alluminio,
                            segmento.profondita_busone_alluminio)
    # Angolo sx
    l_sbarra_tracciatura = new_segmento.l_esterna + new_segmento.posizione_centro_spezzatura_sx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio/2
    # Angolo dx
    l_sbarra_tracciatura += new_segmento.posizione_centro_spezzatura_dx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio/2

    # Tracciatura della lunghezza con busoni grossi e busoni piccoli
    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, new_segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(new_segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_muro, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, True, True)


# TODO: Caso 1 - angolo sx < 90 AND angolo dx = 90
def calcola_distanze_sx_dx_muro_sx_acuto_dx_retto(l_muro, distanza_muro, segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_minima,
                                                  n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    l_esterna = l_muro - 2*distanza_muro
    new_segmento = Segmento(segmento.id, l_esterna, segmento.spessore_sbarra, segmento.angolo_sx,
                            segmento.angolo_dx, segmento.l_busone_acciaio, segmento.l_busone_alluminio,
                            segmento.profondita_busone_alluminio)
    # Angolo sx
    l_sbarra_tracciatura = new_segmento.l_esterna - new_segmento.posizione_centro_spezzatura_sx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio/2
    # Angolo dx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio/2

    # Tracciatura della lunghezza con busoni grossi e busoni piccoli
    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, new_segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(new_segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_muro, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, True, True)


# TODO: Caso 1 - angolo sx < 90 AND angolo dx > 90
def calcola_distanze_sx_dx_muro_sx_acuto_dx_ottuso(l_muro, distanza_muro, segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_minima,
                                                   n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    l_esterna = l_muro - 2*distanza_muro
    new_segmento = Segmento(segmento.id, l_esterna, segmento.spessore_sbarra, segmento.angolo_sx,
                            segmento.angolo_dx, segmento.l_busone_acciaio, segmento.l_busone_alluminio,
                            segmento.profondita_busone_alluminio)
    # Angolo sx
    l_sbarra_tracciatura = new_segmento.l_esterna - new_segmento.posizione_centro_spezzatura_sx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio/2
    # Angolo dx
    l_sbarra_tracciatura += new_segmento.posizione_centro_spezzatura_dx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio/2

    # Tracciatura della lunghezza con busoni grossi e busoni piccoli
    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, new_segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(new_segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_muro, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, True, True)


# TODO: Caso 1 - angolo sx = 90 AND angolo dx > 90
def calcola_distanze_sx_dx_muro_sx_retto_dx_ottuso(l_muro, distanza_muro, segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_minima,
                                                   n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    l_esterna = l_muro - 2*distanza_muro
    new_segmento = Segmento(segmento.id, l_esterna, segmento.spessore_sbarra, segmento.angolo_sx,
                            segmento.angolo_dx, segmento.l_busone_acciaio, segmento.l_busone_alluminio,
                            segmento.profondita_busone_alluminio)
    # Angolo sx
    l_sbarra_tracciatura = new_segmento.l_esterna - distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio/2
    # Angolo dx
    l_sbarra_tracciatura += new_segmento.posizione_centro_spezzatura_dx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio/2

    # Tracciatura della lunghezza con busoni grossi e busoni piccoli
    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, new_segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(new_segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_muro, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, True, True)


# TODO: Caso 1 - angolo sx = 90 AND angolo dx < 90
def calcola_distanze_sx_dx_muro_sx_retto_dx_acuto(l_muro, distanza_muro, segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_minima,
                                                  n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    l_esterna = l_muro - 2*distanza_muro
    new_segmento = Segmento(segmento.id, l_esterna, segmento.spessore_sbarra, segmento.angolo_sx,
                            segmento.angolo_dx, segmento.l_busone_acciaio, segmento.l_busone_alluminio,
                            segmento.profondita_busone_alluminio)
    # Angolo sx
    l_sbarra_tracciatura = new_segmento.l_esterna - distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio/2
    # Angolo dx
    l_sbarra_tracciatura -= new_segmento.posizione_centro_spezzatura_dx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio/2

    # Tracciatura della lunghezza con busoni grossi e busoni piccoli
    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, new_segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(new_segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_muro, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, True, True)


# TODO: Caso 1 - angolo sx > 90 AND angolo dx = 90
def calcola_distanze_sx_dx_muro_sx_ottuso_dx_retto(l_muro, distanza_muro, segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_minima,
                                                   n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    l_esterna = l_muro - 2*distanza_muro
    new_segmento = Segmento(segmento.id, l_esterna, segmento.spessore_sbarra, segmento.angolo_sx,
                            segmento.angolo_dx, segmento.l_busone_acciaio, segmento.l_busone_alluminio,
                            segmento.profondita_busone_alluminio)
    # Angolo sx
    l_sbarra_tracciatura = new_segmento.l_esterna + new_segmento.posizione_centro_spezzatura_sx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio/2
    # Angolo dx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio/2

    # Tracciatura della lunghezza con busoni grossi e busoni piccoli
    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, new_segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(new_segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_muro, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, True, True)


# TODO: Caso 1 - angolo sx > 90 AND angolo dx < 90
def calcola_distanze_sx_dx_muro_sx_ottuso_dx_acuto(l_muro, distanza_muro, segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_minima,
                                                   n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio, n_min_busoni_alluminio):
    l_esterna = l_muro - 2*distanza_muro
    new_segmento = Segmento(segmento.id, l_esterna, segmento.spessore_sbarra, segmento.angolo_sx,
                            segmento.angolo_dx, segmento.l_busone_acciaio, segmento.l_busone_alluminio,
                            segmento.profondita_busone_alluminio)
    # Angolo sx
    l_sbarra_tracciatura = new_segmento.l_esterna + new_segmento.posizione_centro_spezzatura_sx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio/2

    #Angolo dx
    l_sbarra_tracciatura -= new_segmento.posizione_centro_spezzatura_dx
    l_sbarra_tracciatura -= distanza_fine_sbarra_lato_busone
    l_sbarra_tracciatura -= new_segmento.l_busone_acciaio/2

    # Tracciatura della lunghezza con busoni grossi e busoni piccoli
    (n_acciaio, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, n_alluminio,
     distanza_centro_busoni_alluminio,
     distanza_lato_busoni_alluminio) = tr.tracciatura(l_sbarra_tracciatura, new_segmento, id_misura, distanza_minima,
                                                      n_busoni_acciaio, n_busoni_alluminio, n_max_busoni_acciaio,
                                                      n_min_busoni_alluminio)

    return Misure_segmento(new_segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_muro, n_acciaio,
                           distanza_centro_busoni_acciaio,
                           distanza_lato_busoni_acciaio, n_alluminio, distanza_centro_busoni_alluminio,
                           distanza_lato_busoni_alluminio, True, True)

from core.classes.misure_segmento import Misure_segmento
import numpy as np

def calcola_distanze_tracciatura(segmento, l_tracciatura, distanza_minima, n_busoni_alluminio):
    l_tracciatura += segmento.l_busone_alluminio
    distanza_centro_busoni_alluminio = l_tracciatura / n_busoni_alluminio
    distanza_lato_busoni_alluminio = distanza_centro_busoni_alluminio - segmento.l_busone_alluminio
    if (distanza_minima - 5) <= distanza_lato_busoni_alluminio <= (distanza_minima + 5):
        return Misure_segmento(segmento, n_busoni_alluminio, -1, -1, -1, -1, -1, n_busoni_alluminio,
                               distanza_centro_busoni_alluminio, distanza_lato_busoni_alluminio)

    return Misure_segmento(-1, -1, -1, -1, -1, -1, -1, -1, -1, -1)


def tracciatura(l_sbarra_tracciatura, segmento, id_misura, distanza_minima, n_busoni_acciaio, n_busoni_alluminio,
                n_max_busoni_acciaio, n_min_busoni_alluminio):
    for i in range(n_busoni_acciaio, n_max_busoni_acciaio, 1):
        distanza_centro_busoni_acciaio = l_sbarra_tracciatura / i
        if distanza_centro_busoni_acciaio > 1800:
            continue
        distanza_lato_busoni_acciaio = distanza_centro_busoni_acciaio - segmento.l_busone_acciaio
        distanza_lato_busoni_acciaio = distanza_lato_busoni_acciaio + segmento.l_busone_alluminio
        for j in range(n_busoni_alluminio, n_min_busoni_alluminio, -1):
            distanza_centro_busoni_alluminio = distanza_lato_busoni_acciaio / j
            distanza_lato_busoni_alluminio = distanza_centro_busoni_alluminio - segmento.l_busone_alluminio
            if (distanza_minima - 5) <= distanza_lato_busoni_alluminio <= (distanza_minima + 5):
                return (
                    i + 1, distanza_centro_busoni_acciaio, distanza_lato_busoni_acciaio, j + 1,
                    distanza_centro_busoni_alluminio,
                    distanza_lato_busoni_alluminio)
    return -1, -1, -1, -1, -1, -1


def calcola_buchi(segmento: Misure_segmento) -> list[float]:
    result = []
    # Muro a sx ed a dx
    if segmento.murosx:
        if segmento.segmento.angolo_sx <= 90:
            tmp = segmento.segmento.posizione_centro_spezzatura_sx + segmento.distanza_fine_sbarra_lato_busone + segmento.segmento.l_busone_acciaio/2
            result.append(tmp)
            for i in range(1, segmento.n_busoni_acciaio, 1):
                tmp += segmento.distanza_centro_busoni_acciaio
                result.append(tmp)
        else:
            tmp = segmento.distanza_fine_sbarra_lato_busone - segmento.segmento.posizione_centro_spezzatura_sx
            tmp += segmento.segmento.l_busone_acciaio/2
            result.append(tmp)
            for i in range(1, segmento.n_busoni_acciaio, 1):
                tmp += segmento.distanza_centro_busoni_acciaio
                result.append(tmp)
    elif segmento.murosx is False and segmento.murodx:
        if segmento.segmento.angolo_dx <= 90:
            tmp = segmento.segmento.l_esterna - segmento.segmento.posizione_centro_spezzatura_dx - segmento.distanza_fine_sbarra_lato_busone - segmento.segmento.l_busone_acciaio/2
            result.append(tmp)
            for i in range(1, segmento.n_busoni_acciaio, 1):
                tmp -= segmento.distanza_centro_busoni_acciaio
                result.append(tmp)
            result.reverse()
        else:
            tmp = segmento.segmento.l_esterna + segmento.segmento.posizione_centro_spezzatura_dx - segmento.distanza_fine_sbarra_lato_busone - segmento.segmento.l_busone_acciaio/2
            result.append(tmp)
            for i in range(1, segmento.n_busoni_acciaio, 1):
                tmp -= segmento.distanza_centro_busoni_acciaio
                result.append(tmp)
            result.reverse()
    elif segmento.murosx is False and segmento.murodx is False:
        diagonale_rettangolo = np.sqrt(
            np.square(segmento.segmento.l_busone_alluminio) + np.square(segmento.segmento.profondita_busone_alluminio))
        if segmento.segmento.angolo_sx == 90:
            tmp = 0
            result.append(tmp)
            for i in range(1, segmento.n_busoni_acciaio, 1):
                tmp += segmento.distanza_centro_busoni_acciaio
                result.append(tmp)
        elif segmento.segmento.angolo_dx == 90:
            tmp = segmento.segmento.l_esterna
            result.append(tmp)
            for i in range(1, segmento.n_busoni_acciaio, 1):
                tmp -= segmento.distanza_centro_busoni_acciaio
                result.append(tmp)
            result.reverse()
        elif segmento.segmento.angolo_sx < 90 and segmento.segmento.angolo_dx < 90:
            tmp_sx = segmento.segmento.posizione_centro_spezzatura_sx + diagonale_rettangolo/2
            tmp_sx += segmento.distanza_centro_busoni_acciaio/2
            result.append(tmp_sx)
            tmp_dx = segmento.segmento.l_esterna - segmento.segmento.posizione_centro_spezzatura_dx - diagonale_rettangolo/2
            tmp_dx -= segmento.distanza_centro_busoni_acciaio/2

            n_bus = segmento.n_busoni_acciaio - 1
            tot = segmento.segmento.l_esterna - (tmp_sx + (segmento.segmento.l_esterna- tmp_dx))
            for i in range(1, segmento.n_busoni_acciaio - 1, 1):
                tmp_sx += tot/n_bus
                result.append(tmp_sx)
            result.append(tmp_dx)
        elif segmento.segmento.angolo_sx < 90 and segmento.segmento.angolo_dx > 90:
            tmp_sx = segmento.segmento.posizione_centro_spezzatura_sx + diagonale_rettangolo/2
            tmp_sx += segmento.distanza_centro_busoni_acciaio/2
            result.append(tmp_sx)
            tmp_dx = segmento.segmento.l_esterna - np.abs(segmento.segmento.posizione_centro_spezzatura_dx - diagonale_rettangolo/2)
            tmp_dx -= segmento.distanza_centro_busoni_acciaio/2
            n_bus = segmento.n_busoni_acciaio - 1
            tot = segmento.segmento.l_esterna - (tmp_sx + (segmento.segmento.l_esterna- tmp_dx))
            for i in range(1, segmento.n_busoni_acciaio - 1, 1):
                tmp_sx += tot/n_bus
                result.append(tmp_sx)
            result.append(tmp_dx)
        elif segmento.segmento.angolo_sx > 90 and segmento.segmento.angolo_dx < 90:
            tmp_sx = segmento.segmento.l_esterna - np.abs(segmento.segmento.posizione_centro_spezzatura_sx - diagonale_rettangolo/2)
            tmp_sx -= segmento.distanza_centro_busoni_acciaio/2
            result.append(tmp_sx)
            tmp_dx = segmento.segmento.posizione_centro_spezzatura_dx + diagonale_rettangolo/2
            tmp_dx += segmento.distanza_centro_busoni_acciaio/2
            n_bus = segmento.n_busoni_acciaio - 1
            tot = segmento.segmento.l_esterna - (tmp_sx + (segmento.segmento.l_esterna- tmp_dx))
            for i in range(1, segmento.n_busoni_acciaio - 1, 1):
                tmp_sx += tot/n_bus
                result.append(tmp_sx)
            result.append(tmp_dx)
        elif segmento.segmento.angolo_sx > 90 and segmento.segmento.angolo_dx > 90:
            tmp_sx = segmento.segmento.l_esterna - np.abs(segmento.segmento.posizione_centro_spezzatura_sx - diagonale_rettangolo/2)
            tmp_sx -= segmento.distanza_centro_busoni_acciaio/2
            result.append(tmp_sx)
            tmp_dx = segmento.segmento.l_esterna - np.abs(segmento.segmento.posizione_centro_spezzatura_dx - diagonale_rettangolo/2)
            tmp_dx -= segmento.distanza_centro_busoni_acciaio/2
            n_bus = segmento.n_busoni_acciaio - 1
            tot = segmento.segmento.l_esterna - (tmp_sx + (segmento.segmento.l_esterna- tmp_dx))
            for i in range(1, segmento.n_busoni_acciaio - 1, 1):
                tmp_sx += tot/n_bus
                result.append(tmp_sx)
            result.append(tmp_dx)
    return result

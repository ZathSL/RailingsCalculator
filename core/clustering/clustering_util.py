import sys
import numpy as np
from core.classes.misure_segmento import Misure_segmento


# devo andare ad inserire le misure più vicine ai cluster se quel segmento non è già stato inserito
def calcola_vicinanza(primo_segmento, cluster, misura: Misure_segmento):
    key_selected = -1
    distance_min = sys.maxsize
    peso_distanza = 0.2
    peso_n_alluminio = 0.3
    peso_distanza_fine_sbarra = 0.5
    peso_distanza_n_sbarre = 0.5
    for misura_primo_segmento_id, misura_primo_segmento in primo_segmento.items():
        tmp: Misure_segmento = misura_primo_segmento
        distance_current = peso_distanza * np.abs(
            misura.distanza_lato_busoni_alluminio - tmp.distanza_lato_busoni_alluminio)
        distance_current += peso_n_alluminio * (np.abs(misura.n_busoni_alluminio - tmp.n_busoni_alluminio))
        distance_current += peso_distanza_n_sbarre * (np.abs(misura.n_busoni_acciaio - tmp.n_busoni_acciaio))
        if distance_current <= distance_min:
            key_selected = tmp.id_misura
            distance_min = distance_current
    misura_selected: Misure_segmento = primo_segmento[key_selected]
    if misura.segmento.id in cluster[misura_selected.id_misura]:
        # controllo la misura migliore qual è
        tmp: Misure_segmento = cluster[misura_selected.id_misura][misura.segmento.id]
        distance_already = tmp.distanza_lato_busoni_alluminio
        distance2_already = tmp.n_busoni_alluminio
        d = peso_distanza * np.abs(primo_segmento[key_selected].distanza_lato_busoni_alluminio - distance_already)
        d += peso_n_alluminio * np.abs(primo_segmento[key_selected].n_busoni_alluminio - distance2_already)

        # tmp è la misura già presente
        # misura è quella che sto confrontando
        distance_fine_sbarra_misura = 0
        distance_fine_sbarra_tmp = 0
        for misura_i, value in cluster[misura_selected.id_misura].items():
            distance_fine_sbarra_tmp += np.abs(
                tmp.distanza_fine_sbarra_lato_busone - value.distanza_fine_sbarra_lato_busone)
            distance_fine_sbarra_misura += np.abs(
                misura.distanza_fine_sbarra_lato_busone - value.distanza_fine_sbarra_lato_busone)
        distance_min += distance_fine_sbarra_misura * peso_distanza_fine_sbarra
        d += distance_fine_sbarra_tmp * peso_distanza_fine_sbarra
        if d >= distance_min:
            cluster[misura_selected.id_misura][misura.segmento.id] = misura

    else:
        cluster[misura_selected.id_misura][misura.segmento.id] = misura


def clustering_misure(lista_segmenti):
    # prendo la lista dei segmenti e cerco di clusterizzare le misure che si trovano in Misure_segmento
    primo_segmento = lista_segmenti[0]
    # cardinalità(cluster) = #misurazioni
    # cluster[i] contiene
    cluster = {}
    for misura in primo_segmento.values():
        tmp: Misure_segmento = misura
        if tmp.distanza_lato_busoni_alluminio != 0:
            cluster[tmp.id_misura] = {}
    for segmento_id, lista_misure_seg in lista_segmenti.items():
        if segmento_id == 0:
            continue
        for misura_id, misura in lista_misure_seg.items():
            tmp: Misure_segmento = misura
            distanza_corrente = tmp.distanza_lato_busoni_alluminio
            if distanza_corrente != 0:
                calcola_vicinanza(primo_segmento, cluster, misura)
    return cluster
    # cluster sarà un dizionario
    # la prima chiave che lo indicizza è l'id delle misure del primo segmento
    # il valore è un altro dizionario
    # il secondo dizionario è indicizzato rispetto all'id dei segmenti legati alla misura del primo segmento
    # il valore del secondo dizionario è la misura scelta più vicina che rappresenta quel segmento

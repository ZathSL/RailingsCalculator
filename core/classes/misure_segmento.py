class Misure_segmento:
    def __init__(self, Segmento, id_misura, distanza_fine_sbarra_lato_busone, distanza_muro, n_busoni_acciaio,
                 distanza_centro_busoni_acciaio,
                 distanza_lato_busoni_acciaio, n_busoni_alluminio, distanza_centro_busoni_alluminio,
                 distanza_lato_busoni_alluminio, murosx, murodx):
        self.id_misura = id_misura
        self.segmento = Segmento
        self.n_busoni_acciaio = n_busoni_acciaio
        self.distanza_centro_busoni_acciaio = distanza_centro_busoni_acciaio
        self.distanza_lato_busoni_acciaio = distanza_lato_busoni_acciaio
        self.n_busoni_alluminio = n_busoni_alluminio
        self.distanza_centro_busoni_alluminio = distanza_centro_busoni_alluminio
        self.distanza_lato_busoni_alluminio = distanza_lato_busoni_alluminio
        self.distanza_fine_sbarra_lato_busone = distanza_fine_sbarra_lato_busone
        self.distanza_muro = distanza_muro
        self.murosx = murosx
        self.murodx = murodx
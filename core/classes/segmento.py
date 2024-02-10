import numpy as np
class Segmento:
    def __init__(self, id, l_esterna, spessore_sbarra,
                 angolo_sx, angolo_dx, l_busone_acc, l_busone_all, profondita_busone_all):
        self.id = id
        self.l_esterna = l_esterna
        self.spessore_sbarra = spessore_sbarra
        self.angolo_sx = angolo_sx
        self.angolo_dx = angolo_dx
        self.l_busone_acciaio = l_busone_acc
        self.l_busone_alluminio = l_busone_all
        self.profondita_busone_alluminio = profondita_busone_all

        if 0 < angolo_dx < 90 and 0 < angolo_sx < 90:
            self.diagonale_dx = spessore_sbarra / np.sin(np.radians(angolo_dx))
            self.diagonale_sx = spessore_sbarra / np.sin(np.radians(angolo_sx))
            cot_sx = 1 / np.tan(np.radians(angolo_sx))
            cot_dx = 1 / np.tan(np.radians(angolo_dx))
            self.posizione_centro_spezzatura_sx = (self.spessore_sbarra / 2) * cot_sx
            self.posizione_centro_spezzatura_dx = (self.spessore_sbarra / 2) * cot_dx
            cateto_sx = self.diagonale_sx * np.cos(np.radians(self.angolo_sx))
            cateto_dx = self.diagonale_dx * np.cos(np.radians(self.angolo_dx))
            self.l_interna = self.l_esterna - (cateto_sx + cateto_dx)
        elif 0 < angolo_dx < 90 and angolo_sx == 90:
            self.diagonale_dx = spessore_sbarra / np.sin(np.radians(angolo_dx))
            self.diagonale_sx = spessore_sbarra
            cot_dx = 1 / np.tan(np.radians(angolo_dx))
            self.posizione_centro_spezzatura_sx = 0
            self.posizione_centro_spezzatura_dx = (self.spessore_sbarra / 2) * cot_dx
            cateto_dx = self.diagonale_dx * np.cos(np.radians(self.angolo_dx))
            self.l_interna = self.l_esterna - cateto_dx
        elif angolo_dx == 90 and 0 < angolo_sx < 90:
            self.diagonale_dx = spessore_sbarra
            self.diagonale_sx = spessore_sbarra / np.sin(np.radians(angolo_sx))
            cot_sx = 1 / np.tan(np.radians(angolo_sx))
            self.posizione_centro_spezzatura_dx = 0
            self.posizione_centro_spezzatura_sx = (self.spessore_sbarra / 2) * cot_sx
            cateto_sx = self.diagonale_sx * np.cos(np.radians(self.angolo_sx))
            self.l_interna = self.l_esterna - cateto_sx
        elif angolo_dx == 90 and angolo_sx == 90:
            self.diagonale_dx = spessore_sbarra
            self.diagonale_sx = spessore_sbarra
            self.posizione_centro_spezzatura_dx = 0
            self.posizione_centro_spezzatura_sx = 0
            self.l_interna = self.l_esterna
        # posizione centro spezzatura sfora rispetto alla lunghezza esterna
        elif 180 > angolo_sx > 90 > angolo_dx > 0:
            tmp_angolo_sx = angolo_sx - 90
            self.diagonale_sx = spessore_sbarra / np.cos(np.radians(tmp_angolo_sx))
            self.diagonale_dx = spessore_sbarra / np.sin(np.radians(angolo_dx))
            cot_dx = 1 / np.tan(np.radians(angolo_dx))
            self.posizione_centro_spezzatura_sx = (self.spessore_sbarra / 2) * np.tan(np.radians(tmp_angolo_sx))
            self.posizione_centro_spezzatura_dx = (self.spessore_sbarra / 2) * cot_dx
            cateto_sx = self.diagonale_sx * np.sin(np.radians(tmp_angolo_sx))  # da sommare
            cateto_dx = self.diagonale_dx * np.cos(np.radians(self.angolo_dx))
            self.l_interna = self.l_esterna + cateto_sx - cateto_dx
        elif 90 < angolo_sx < 180 and 90 < angolo_dx < 180:
            tmp_angolo_sx = angolo_sx - 90
            tmp_angolo_dx = angolo_dx - 90
            self.diagonale_sx = spessore_sbarra / np.cos(np.radians(tmp_angolo_sx))
            self.diagonale_dx = spessore_sbarra / np.cos(np.radians(tmp_angolo_dx))
            self.posizione_centro_spezzatura_sx = (self.spessore_sbarra / 2) * np.tan(np.radians(tmp_angolo_sx))
            self.posizione_centro_spezzatura_dx = (self.spessore_sbarra / 2) * np.tan(np.radians(tmp_angolo_dx))
            cateto_sx = self.diagonale_sx * np.sin(np.radians(tmp_angolo_sx))
            cateto_dx = self.diagonale_dx * np.sin(np.radians(tmp_angolo_dx))
            self.l_interna = self.l_esterna + cateto_sx + cateto_dx
        elif 0 < angolo_sx < 90 < angolo_dx < 180:
            tmp_angolo_dx = angolo_dx - 90
            self.diagonale_sx = spessore_sbarra / np.sin(np.radians(angolo_sx))
            self.diagonale_dx = spessore_sbarra / np.cos(np.radians(tmp_angolo_dx))
            cot_sx = 1 / np.tan(np.radians(angolo_sx))
            self.posizione_centro_spezzatura_sx = (self.spessore_sbarra / 2) * cot_sx
            self.posizione_centro_spezzatura_dx = (self.spessore_sbarra / 2) * np.tan(np.radians(tmp_angolo_dx))
            cateto_sx = self.diagonale_sx * np.cos(np.radians(self.angolo_sx))
            cateto_dx = self.diagonale_dx * np.sin(np.radians(tmp_angolo_dx))
            self.l_interna = self.l_esterna - cateto_sx + cateto_dx
        elif angolo_sx == 90 and 90 < angolo_dx < 180:
            self.diagonale_sx = spessore_sbarra
            tmp_angolo_dx = angolo_dx - 90
            self.diagonale_dx = spessore_sbarra / np.cos(np.radians(tmp_angolo_dx))
            self.posizione_centro_spezzatura_sx = 0
            cot_dx = 1 / np.tan(np.radians(tmp_angolo_dx))
            self.posizione_centro_spezzatura_dx = (self.spessore_sbarra / 2) * cot_dx
            cateto_dx = self.diagonale_dx * np.cos(np.radians(tmp_angolo_dx))
            self.l_interna = self.l_esterna + cateto_dx
        elif 180 > angolo_sx > 90 == angolo_dx:
            tmp_angolo_sx = angolo_sx - 90
            self.diagonale_sx = spessore_sbarra / np.cos(np.radians(tmp_angolo_sx))
            self.diagonale_dx = spessore_sbarra
            self.posizione_centro_spezzatura_sx = (self.spessore_sbarra / 2) * np.tan(np.radians(tmp_angolo_sx))
            self.posizione_centro_spezzatura_dx = 0
            cateto_sx = self.diagonale_sx * np.sin(np.radians(tmp_angolo_sx))
            self.l_interna = self.l_esterna + cateto_sx
        else:
            self.diagonale_dx = -1
            self.diagonale_sx = -1
            self.posizione_centro_spezzatura_sx = -1
            self.posizione_centro_spezzatura_dx = -1
            self.l_esterna = -1
            self.l_interna = -1

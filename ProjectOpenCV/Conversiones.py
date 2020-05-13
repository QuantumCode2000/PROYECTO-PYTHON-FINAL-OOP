import Proceso
import cv2


class Convertido(Proceso.Proceso):
    @classmethod
    def imagen_a_escala_de_grises(cls, imagen):
        gray_imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        return gray_imagen


class Convertido2(Proceso.Proceso):
    @classmethod
    def imagen_laplaciana(cls, imagen_l):
        gray_imagen = cv2.cvtColor(imagen_l, cv2.COLOR_BGR2GRAY)
        laplaciano = cv2.Laplacian(gray_imagen, cv2.CV_64F)
        return laplaciano

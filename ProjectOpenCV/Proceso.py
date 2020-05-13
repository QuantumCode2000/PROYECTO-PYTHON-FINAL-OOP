import cv2


class Proceso:
    @staticmethod
    def leido_de_iamgen(imagen_leida):
        imagen = cv2.imread(imagen_leida)
        return imagen

    @staticmethod
    def guardar_imagen(imagen, nombre_de_la_imagen_nueva):
        if(nombre_de_la_imagen_nueva.isalnum()):
            nombre_de_la_imagen = nombre_de_la_imagen_nueva + ".jpg"
            cv2.imwrite(nombre_de_la_imagen, imagen)
        else:
            print(" ********no es un formato correcto para asignarle un nombre a la imagen********")

    @staticmethod
    def mostrar_imagen_en_ventana(nombre_de_la_ventana, imagen_a_mostrar):
        cv2.namedWindow(nombre_de_la_ventana, cv2.WINDOW_NORMAL)
        cv2.imshow(nombre_de_la_ventana, imagen_a_mostrar)
        cv2.waitKey(0)
        cv2.destroyAllWindows()






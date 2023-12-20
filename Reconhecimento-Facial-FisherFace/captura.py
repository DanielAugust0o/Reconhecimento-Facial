import cv2
import numpy as np
classificador = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
classificadorOlho = cv2.CascadeClassifier('haarcascade_eye.xml')
camera = cv2.VideoCapture(0)  # fazer a captura da imagem com a webcam
amostra = 1 #controlar quantas fotos foram tiradas
numerodeAmostras = 25
id = input('Digite seu identificador: ')
largura, altura = 220, 220 #padronizar o tamanho das imagens obtidas
print('Capturando as faces... ')

while (True):
    conectado, imagem = camera.read()  # fazer leitura da webcam
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)  # convertendo a imagem em tons de cinza
    print(np.average(imagemCinza))
    facesDetectadas = classificador.detectMultiScale(imagemCinza,
                                                     scaleFactor=1.5,
                                                     minSize=(100, 100))  # parametros da imagem detectada
    for (x, y, l, a) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)  # após detectar a face coloca o um quadrado vermelho nela
        regiao = imagem[y:y + a, x:x +l]
        regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
        olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)

        for (ox, oy, ol, oa) in olhosDetectados: #detectando os olhos
            cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)

            if cv2.waitKey(1)& 0xFF == ord ('q'): #quando apertar o q vai gravar essa imagem
                if np.average(imagemCinza) < 110: #somente capturar a imagem se possuir a luminosidade maior que esse atributo
                    imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura)) #redimencionando a imagem
                    cv2.imwrite('fotos/pessoa.'+str(id) + '.' + str(amostra) + '.jpg', imagemFace)
                    print('[ foto ' + str(amostra) + ' capturada com sucesso ]')
                    amostra += 1


    cv2.imshow('Face', imagem)
    cv2.waitKey(1)
    if (amostra >= numerodeAmostras + 1):
        break
print('Faces capturadas com sucesso')
camera.release()
cv2.destroyAllWindows()

# coding: utf-8

# Author: Professor Leonardo Galesky
# Fundação Assis Gurgacz - Introduction to Artificial Inteligence - Class of 2020
# Fundação Assis Gurgacz - Introdução a Inteligência Artifical - Turma 2020

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Importa a imagem 'maior'
img = cv.imread('messi5.jpg',0)
img2 = img.copy()
# Importa a imagem 'template'
template = cv.imread('template.jpg',0)
w, h = template.shape[::-1]
# Todos os 6 métodos de comparação em uma lista
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
for meth in methods:
    img = img2.copy()
    # Tomar cuidado com uso de eval em produção
    # Para nosso caso em ambiente fechado é suficiente
    # Esse comando está tornando o 'cv.TM_CCOEFF' em um objeto explicito de código
    # ao invés de uma string
    method = eval(meth)

    # Aplica o 'template matching'
    res = cv.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # Se o método for TM_SQDIFF ou TM_SQDIFF_NORMED, usar o mínimo
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    # top e bottom são os pontos que delimitam o retangulo que vamos
    # desenhar sobre o rosto do Messi
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(img,top_left, bottom_right, 255, 2)
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()

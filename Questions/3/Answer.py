import cv2
import numpy as np

img_bgr = cv2.imread('imagem3.jpg', cv2.IMREAD_COLOR)

img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

#### após essa transformação para o formato RGB, vou dividir os canais

R , G , B = cv2.split(img_rgb)

############# agora vou criar uma imagem para cada canal, senao vai reconhecer apenas o alfa



R_img = cv2.merge([np.zeros_like(R), np.zeros_like(G), R])
G_img = cv2.merge([np.zeros_like(B), G, np.zeros_like(R)])
B_img = cv2.merge([B, np.zeros_like(G), np.zeros_like(B)])

cv2.imshow ('canal_vermelho.jpg', R_img)
cv2.imshow ('canal_verde.jpg', G_img)
cv2.imshow ('canal_azul.jpg', B_img)
cv2.imshow ('imagem.jpg', img_rgb)

######################## agora irei salvar

cv2.imwrite("canal_vermelho.jpg", R_img)
cv2.imwrite("canalverde.jpg", G_img)
cv2.imwrite("canal_azul.jpg", B_img)
cv2.imwrite("imagem_rgb.jpg", img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()


########### cosiderações: como vc pode observar a imagem em rgb ficou diferente do esperado
# pois ela foi convertida de BGR, por isso o alguma de suas posicoes de cores foram invertidas
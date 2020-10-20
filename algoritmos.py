# algortimos.py
import math 

def distancia_euclidiana(x1,x2,y1,y2):
    res = math.sqrt(((y1-x1)**2) + ((y2 - x2)**2))
    return res
	
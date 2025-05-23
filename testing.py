import Portafolio3;
import pytest;

def test_construir_1():
    assert Portafolio3.construir(2345) == 24

def test_digitoMenor_1():
    assert Portafolio3.digitoMenor(569803) == 0

def test_digitosOrdenados_1():
    assert Portafolio3.digitosOrdenados(2345678) == True

def test_elevarNumero_1():
    assert Portafolio3.elevarNumero(5, 3) == 125

#####################################################################################################

def test_invertirLista_1():
    assert Portafolio3.invertirLista([5,8,45,96]) == [96, 45, 8, 5]
    
def test_invertirLista_2():
    assert Portafolio3.invertirLista([56, 85,8,45,96]) == [96, 45, 8, 85, 56]

def test_invertirLista_2():
    assert isinstance(Portafolio3.invertirLista([]), str) == isinstance("Error: La lista debe contener al menos 2 elementos", str)

def test_invertirLista_2():
    assert isinstance(Portafolio3.invertirLista([2,5,7,"ABC"]), str) == isinstance("Error: La lista debe contener elementos tipo entero", str)
    
    
#####################################################################################################

def test_extremosLista_1():
    assert Portafolio3.extremosLista([18,5,8,45,96, 60]) == [5,96]

def test_extremosLista_2():
    assert Portafolio3.extremosLista([96, 96,96]) == [96]

def test_extremosLista_3():
    assert isinstance(Portafolio3.extremosLista([]), str) == isinstance("Error: La lista debe contener al menos 2 elementos", str)

def test_extremosLista_4():
    assert isinstance(Portafolio3.extremosLista([2,5,7,"ABC"]), str) == isinstance("Error: La lista debe contener elementos tipo entero", str)
    
#####################################################################################################

def test_eliminarElementosLista_1():
    assert Portafolio3.eliminarElementosLista([254, 25, 8], [25]) == [254, 8]

def test_eliminarElementosLista_2():
    assert Portafolio3.eliminarElementosLista([54, 25, 8], [25, 54]) == [8]

def test_eliminarElementosLista_3():
    assert Portafolio3.eliminarElementosLista([54, 25, 8], [21, 24]) == [54,25,8]

def test_eliminarElementosLista_4():
    assert isinstance(Portafolio3.eliminarElementosLista([], [2,4]), str) == isinstance("Error: La primera lista debe contener al menos 1 elemento", str) 

def test_eliminarElementosLista_5():
    assert isinstance(Portafolio3.eliminarElementosLista([23,78,9], []), str) == isinstance("Error: La segunda lista debe contener al menos 1 elemento", str) 

def test_eliminarElementosLista_6():
    assert isinstance(Portafolio3.extremosLista([2,5,7,"ABC"], [2,8]), str) == isinstance("Error: La primera lista debe elementos tipo entero", str) 

def test_eliminarElementosLista_7():
    assert isinstance(Portafolio3.extremosLista([2,5,7], [2,"8"]), str) == isinstance("Error: La segunda lista debe elementos tipo entero", str) 

#####################################################################################################

def test_nivelesLista_1():
    assert Portafolio3.nivelesLista([ [[[[]]]], 2, [] ] ) == [4 ,0, 1]
def test_nivelesLista_2():
    assert Portafolio3.nivelesLista([ [2], [], [[[[[[]]]]]] ]) == [1, 1, 6]
def test_nivelesLista_3():
    assert isinstance(Portafolio3.nivelesLista(25), str) == isinstance("Error: El parámetro de entrada debe ser una lista", str) 
    
#####################################################################################################

v1 = [12,  56, 7 , 11 , -8, 3] 
v2 = [-26, 2, 75 , 19 , -18, 23] 
v3 = [6, 2, 10 , 50, 90] 

def test_obtenerIndicesListas_1():
    assert Portafolio3.obtenerIndicesListas([v1, v2, v3]) == [[2,3,4,5], [0,1,3,4,5], [1]]

def test_obtenerIndicesListas_2():
    assert isinstance(Portafolio3.obtenerIndicesListas(25), str) == isinstance("Error: El parámetro de entrada debe ser una lista", str)

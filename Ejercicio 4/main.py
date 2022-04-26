from claseVentana import Ventana
if __name__ ==  '__main__':
    print('==== Ventana Inicio ====')
    ventanaInicio= Ventana('Inicio')
    ventanaInicio.mostrar()
    print('Ventana: {} Alto: {} Ancho: {}'.format(ventanaInicio.getTitulo(),ventanaInicio.alto(),ventanaInicio.ancho()))
    input() #añadido
    print('==== Ventana Cargar ====')
    ventanaCargar= Ventana('Cargar',[100, 200],[20,30])
    ventanaCargar.mostrar()
    input() #añadido
    print('*** Mueve a la derecha ***')
    ventanaCargar.moverDerecha(10)
    ventanaCargar.mostrar()
    input() #añadido
    print('*** Mueve a la izquierda ***')
    ventanaCargar.moverIzquierda(10)
    ventanaCargar.mostrar()
    input() #añadido
    print('*** Bajar ***')
    ventanaCargar.bajar(10)
    ventanaCargar.mostrar()
    input() #añadido
    print('==== Ventana Borrar ====')
    ventanaBorrar = Ventana('Borrar', [10,20], [100,200])
    ventanaBorrar.mostrar()
    input() #añadido
    print('*** Subir ***')
    ventanaBorrar.subir(5)
    ventanaBorrar.mostrar()
    input() #añadido
    print('*** Subir ***')
    ventanaBorrar.subir()
    ventanaBorrar.mostrar()
    input() #añadido
    print('*** Bajar ***')
    ventanaBorrar.bajar()
    ventanaBorrar.mostrar()
    input() #añadido
# De la libreria tkinter importamos todos sus elementos
# para la construccion de la IA
import tkinter as tk

# Creamos un objeto ventana el cual al inicializarse se
# le asignan todos los valores que contendra como botones
# label, texto, dimensiones, metodos, etc
class Ventana():

    def __init__(self):
        
        # Definimos la ventana principal como "main"
        self.main = tk.Tk()

        # Le asignamos un titulo a la ventana principal
        self.main.title("Totito by Rodrigo")

        # Le asignamos un tamaño a la ventana principal
        self.main.geometry("455x520")

        # Se define un contador para llevar el control de las veces que se presionaron los botones
        self.contador = 0

        #-----------CREACION DEL GRID----------

        # Creamos un boton nuevo en la ventana main
        self.buttonB = tk.Button(self.main, text="", width=20, height=10, bg="white", command=self.color1)
        # Le asignamos la posicion en la que estara y el margen interno que tendra
        self.buttonB.grid( pady=5, row=1, column=0)

        # Creamos un boton nuevo en la ventana main
        self.buttonB1 = tk.Button(self.main, text="", width=20, height=10, bg="white", command=self.color2)
        # Le asignamos la posicion en la que estara y el margen interno que tendra
        self.buttonB1.grid( pady=5, row=1, column=1)

        # Creamos un boton nuevo en la ventana main
        self.buttonB2 = tk.Button(self.main, text="", width=20, height=10, bg="white", command=self.color3)
        # Le asignamos la posicion en la que estara y el margen interno que tendra
        self.buttonB2.grid( pady=5, row=1, column=2)

        # Creamos un boton nuevo en la ventana main
        self.buttonB3 = tk.Button(self.main, text="", width=20, height=10, bg="white", command=self.color4)
        # Le asignamos la posicion en la que estara y el margen interno que tendra
        self.buttonB3.grid( pady=5, row=2, column=0)

        # Creamos un boton nuevo en la ventana main
        self.buttonB4 = tk.Button(self.main, text="", width=20, height=10, bg="white", command=self.color5)
        # Le asignamos la posicion en la que estara y el margen interno que tendra
        self.buttonB4.grid( pady=5, row=2, column=1)

        # Creamos un boton nuevo en la ventana main
        self.buttonB5 = tk.Button(self.main, text="", width=20, height=10, bg="white", command=self.color6)
        # Le asignamos la posicion en la que estara y el margen interno que tendra
        self.buttonB5.grid( pady=5, row=2, column=2)

        # Creamos un boton nuevo en la ventana main
        self.buttonB6 = tk.Button(self.main, text="", width=20, height=10, bg="white", command=self.color7)
        # Le asignamos la posicion en la que estara y el margen interno que tendra
        self.buttonB6.grid( pady=5, row=3, column=0)

        # Creamos un boton nuevo en la ventana main
        self.buttonB7 = tk.Button(self.main, text="", width=20, height=10, bg="white", command=self.color8)
        # Le asignamos la posicion en la que estara y el margen interno que tendra
        self.buttonB7.grid( pady=5, row=3, column=1)

        # Creamos un boton nuevo en la ventana main
        self.buttonB8 = tk.Button(self.main, text="", width=20, height=10, bg="white", command=self.color9)
        # Le asignamos la posicion en la que estara y el margen interno que tendra
        self.buttonB8.grid( pady=5, row=3, column=2)

        # Se hace visible la ventana principal
        self.main.mainloop()

        #-----------FIN CREACION DEL GRID----------


    #-----------CREACION DE METODOS--------------------

    # Por cada boton se crea un metodo al momento de presionarlo

    def color1(self):
        # Se le suma una unidad al contador de la ventana
        self.contador += 1
        # Se pregunta si es par
        if self.contador % 2 == 0:
            # Si es par se cambia el texto del boton a X
            self.buttonB.config(text="X")
            # Se pregunta si se presionaron los nueve bototnes del tablero
            if self.contador == 9:
                # Si es asi se llama a la funcion
                self.validar()
        else:
            # Si no es par se cambia el texto del boton a O
            self.buttonB.config(text="O")
            # Se pregunta si se presionaron los nueve bototnes del tablero
            if self.contador == 9:
                # Si es asi se llama a la funcion
                self.validar()

    def color2(self):
        # Se le suma una unidad al contador de la ventana
        self.contador += 1
        # Se pregunta si es par
        if self.contador % 2 == 0:
            # Si es par se cambia el texto del boton a X
            self.buttonB1.config(text="X")
            # Se pregunta si se presionaron los nueve bototnes del tablero
            if self.contador == 9:
                # Si es asi se llama a la funcion
                self.validar()
        else:
            # Si no es par se cambia el texto del boton a O
            self.buttonB1.config(text="O")
            # Se pregunta si se presionaron los nueve bototnes del tablero
            if self.contador == 9:
                # Si es asi se llama a la funcion
                self.validar()

    def color3(self):
        # Se le suma una unidad al contador de la ventana
        self.contador += 1
        # Se pregunta si es par
        if self.contador % 2 == 0:
            # Si es par se cambia el texto del boton a X
            self.buttonB2.config(text="X")
            # Se pregunta si se presionaron los nueve bototnes del tablero
            if self.contador == 9:
                # Si es asi se llama a la funcion
                self.validar()
        else:
            # Si no es par se cambia el texto del boton a O
            self.buttonB2.config(text="O")
            # Se pregunta si se presionaron los nueve bototnes del tablero
            if self.contador == 9:
                # Si es asi se llama a la funcion
                self.validar()

    def color4(self):
        # Se le suma una unidad al contador de la ventana
        self.contador += 1
        # Se pregunta si es par
        if self.contador % 2 == 0:
            # Si es par se cambia el texto del boton a X
            self.buttonB3.config(text="X")
            # Se pregunta si se presionaron los nueve bototnes del tablero
            if self.contador == 9:
                # Si es asi se llama a la funcion
                self.validar()
        else:
            # Si no es par se cambia el texto del boton a O
            self.buttonB3.config(text="O")
            # Se pregunta si se presionaron los nueve bototnes del tablero
            if self.contador == 9:
                # Si es asi se llama a la funcion
                self.validar()

    def color5(self):
        # Se le suma una unidad al contador de la ventana
        self.contador += 1
        # Se pregunta si es par
        if self.contador % 2 == 0:
            # Si es par se cambia el texto del boton a X
            self.buttonB4.config(text="X")
            # Se pregunta si se presionaron los nueve bototnes del tablero
            if self.contador == 9:
                # Si es asi se llama a la funcion
                self.validar()
        else:
            # Si no es par se cambia el texto del boton a O
            self.buttonB4.config(text="O")
            # Se pregunta si se presionaron los nueve bototnes del tablero
            if self.contador == 9:
                # Si es asi se llama a la funcion
                self.validar()

    def color6(self):
        # Se le suma una unidad al contador de la ventana
        self.contador += 1
        # Se pregunta si es par
        if self.contador % 2 == 0:
            # Si es par se cambia el texto del boton a X
            self.buttonB5.config(text="X")
            # Se pregunta si se presionaron los nueve bototnes del tablero
            if self.contador == 9:
                # Si es asi se llama a la funcion
                self.validar()
        else:
            # Si no es par se cambia el texto del boton a O
            self.buttonB5.config(text="O")
            # Se pregunta si se presionaron los nueve bototnes del tablero
            if self.contador == 9:
                # Si es asi se llama a la funcion
                self.validar()

    def color7(self):
        # Se le suma una unidad al contador de la ventana
        self.contador += 1
        # Se pregunta si es par
        if self.contador % 2 == 0:
            # Si es par se cambia el texto del boton a X
            self.buttonB6.config(text="X")
            # Se pregunta si se presionaron los nueve bototnes del tablero
            if self.contador == 9:
                # Si es asi se llama a la funcion
                self.validar()
        else:
            # Si no es par se cambia el texto del boton a O
            self.buttonB6.config(text="O")
            # Se pregunta si se presionaron los nueve bototnes del tablero
            if self.contador == 9:
                # Si es asi se llama a la funcion
                self.validar()

    def color8(self):
        # Se le suma una unidad al contador de la ventana
        self.contador += 1
        # Se pregunta si es par
        if self.contador % 2 == 0:
            # Si es par se cambia el texto del boton a X
            self.buttonB7.config(text="X")
            # Se pregunta si se presionaron los nueve bototnes del tablero
            if self.contador == 9:
                # Si es asi se llama a la funcion
                self.validar()
        else:
            # Si no es par se cambia el texto del boton a O
            self.buttonB7.config(text="O")
            # Se pregunta si se presionaron los nueve bototnes del tablero
            if self.contador == 9:
                # Si es asi se llama a la funcion
                self.validar()

    def color9(self):
        # Se le suma una unidad al contador de la ventana
        self.contador += 1
        # Se pregunta si es par
        if self.contador % 2 == 0:
            # Si es par se cambia el texto del boton a X
            self.buttonB8.config(text="X")
            # Se pregunta si se presionaron los nueve bototnes del tablero
            if self.contador == 9:
                # Si es asi se llama a la funcion
                self.validar()
        else:
            # Si no es par se cambia el texto del boton a O
            self.buttonB8.config(text="O")
            # Se pregunta si se presionaron los nueve bototnes del tablero
            if self.contador == 9:
                # Si es asi se llama a la funcion
                self.validar()

    # Se define un metodo para validar el tablero
    def validar(self):
        # Se pregunta si se presionaron los 9 botones
        if self.contador == 9:
            # Si es asi

            # ------- Validando filas -------------------

            # -----------Para las X-------------------------------------------------------------------------------

            # Validacion fila 1: Se valida que la posicion (1,1), (1,2), (1,3) sean X
            if self.buttonB["text"] == 'X' and self.buttonB1["text"] == 'X' and self.buttonB2["text"] == 'X':
                print('Ganador X')
                return

            # Validacion fila 2: Se valida que la posicion (2,1), (2,2), (2,3) sean X
            elif self.buttonB3["text"] == 'X' and self.buttonB4["text"] == 'X' and self.buttonB5["text"] == 'X':
                print('Ganador X')
                return

            # Validacion fila 3: Se valida que la posicion (2,1), (2,2), (2,3) sean X
            elif self.buttonB6["text"] == 'X' and self.buttonB7["text"] == 'X' and self.buttonB8["text"] == 'X':
                print('Ganador X')
                return

            # ----------------------------------------------------------------------------------------------------

            # --------------Para las O----------------------------------------------------------------------------

            # Validacion fila 1: Se valida que la posicion (1,1), (1,2), (1,3) sean O
            elif self.buttonB["text"] == 'O' and self.buttonB1["text"] == 'O' and self.buttonB2["text"] == 'O':
                print('Ganador O')
                return

            # Validacion fila 2: Se valida que la posicion (2,1), (2,2), (2,3) sean O
            elif self.buttonB3["text"] == 'O' and self.buttonB4["text"] == 'O' and self.buttonB5["text"] == 'O':
                print('Ganador O')
                return

            # Validacion fila 3: Se valida que la posicion (2,1), (2,2), (2,3) sean O
            elif self.buttonB6["text"] == 'O' and self.buttonB7["text"] == 'O' and self.buttonB8["text"] == 'O':
                print('Ganador O')
                return
            
            # ----------------------------------------------------------------------------------------------------

            #-----------Fin Validar filas------------------



            # ------- Validando Columnas -------------------

            # -----------Para las X-------------------------------------------------------------------------------

            # Validacion columna 1: Se valida que la posicion (1,1), (2,1), (3,1) sean X
            elif self.buttonB["text"] == 'X' and self.buttonB3["text"] == 'X' and self.buttonB6["text"] == 'X':
                print('Ganador X')
                return

            # Validacion columna 2: Se valida que la posicion (1,2), (2,2), (3,2) sean X
            elif self.buttonB1["text"] == 'X' and self.buttonB4["text"] == 'X' and self.buttonB7["text"] == 'X':
                print('Ganador X')
                return

            # Validacion columna 3: Se valida que la posicion (1,3), (2,3), (3,3) sean X
            elif self.buttonB2["text"] == 'X' and self.buttonB5["text"] == 'X' and self.buttonB8["text"] == 'X':
                print('Ganador X')
                return

            # ----------------------------------------------------------------------------------------------------

            # --------------Para las O----------------------------------------------------------------------------

            # Validacion columna 1: Se valida que la posicion (1,1), (2,1), (3,1) sean O
            elif self.buttonB["text"] == 'O' and self.buttonB3["text"] == 'O' and self.buttonB6["text"] == 'O':
                print('Ganador O')
                return

            # Validacion columna 2: Se valida que la posicion (1,2), (2,2), (3,2) sean O
            elif self.buttonB1["text"] == 'O' and self.buttonB4["text"] == 'O' and self.buttonB7["text"] == 'O':
                print('Ganador O')
                return

            # Validacion columna 3: Se valida que la posicion (1,3), (2,3), (3,3) sean O
            elif self.buttonB2["text"] == 'O' and self.buttonB5["text"] == 'O' and self.buttonB8["text"] == 'O':
                print('Ganador O')
                return
            
            # -----------------------------------------------------------------------------------------------------

            #-----------Fin Validar columnas------------------


            
            #----------- Validar Diagonales ------------------

            # ------------ Para las X -------------------------------------------------------------------------

            # Validacion diagonal 1: Se valida que la posicion (1,1), (2,2), (3,3) sean X
            elif self.buttonB["text"] == 'X' and self.buttonB4["text"] == 'X' and self.buttonB8["text"] == 'X':
                print('Ganador X')
                return
            
            # Validacion diagonal 2: Se valida que la posicion (1,3), (2,2), (3,1) sean X
            elif self.buttonB2["text"] == 'X' and self.buttonB4["text"] == 'X' and self.buttonB6["text"] == 'X':
                print('Ganador X')
                return

            # ------------ Fin para las X -------------------------------------------------------------------------



            # ------------ Para las O -------------------------------------------------------------------------

            # Validacion diagonal 1: Se valida que la posicion (1,1), (2,2), (3,3) sean O
            elif self.buttonB["text"] == 'O' and self.buttonB4["text"] == 'O' and self.buttonB8["text"] == 'O':
                print('Ganador O')
                return
            
            # Validacion diagonal 2: Se valida que la posicion (1,3), (2,2), (3,1) sean O
            elif self.buttonB2["text"] == 'O' and self.buttonB4["text"] == 'O' and self.buttonB6["text"] == 'O':
                print('Ganador O')
                return

            # ------------ Fin para las O -------------------------------------------------------------------------
                
            #-----------Fin Validar diagonales------------------


            # En caso no se haga ninguna validacion
            else:
                print('Sin Ganador - Empate')
                return

    #-----------FIN CREACION DE METODOS--------------------

# Se crea un objeto ventana para inicializar el tablero
app=Ventana()

# -*- coding: utf-8 -*-

class Inicio:

    """ AGREGAR ELEMENTOS A LA COLA """
    def abrir_archivo(self):
        #Abrir .txt con expresiones aritmeticas
        expresiones = open("expresiones.txt")
        linea = [" "]
        impresion = ''
        while linea != '':
            #Leer linea a linea del .txt
            linea = expresiones.readline().split(' ')
            if (linea == ['']):
                expresiones.close()
                break
            #Resultado para el archivo
                #' '.join() une los elementos 
                #linea[:-1] todos menos el ultimo elemento
            impresion += "La respuesta para ["+' '.join(linea[:-1])+"] es: "'\n'
            impresion += self.describir_lexico(' '.join(linea[:-1]))
        return impresion

    """ AGREGAR EL RESULTADO AL ARCHIVO """   
    def escribir_archivo(self,resultado):
        busquedas = open("resultados.txt", "w")
        busquedas.write(resultado)
        busquedas.close()

    """ DETERMINAR EL TIPO DE CARACTER (LEXICO) """
    #El lexico solo acepta numeros, operadores y variables (en minuscula)
    def describir_lexico(self,elementos):
        #Tomar elemento por elemento
        caracteres = elementos.split(' ')
        i = 0
        impresion = ""
        while i < len(caracteres):
            #Si es un numero
            if caracteres[i].isdigit():
                impresion += caracteres[i]+" es un valor"'\n'
            #Si es un operador (+-*/)
            elif caracteres[i] == "*" or caracteres[i] == "+" or caracteres[i] == "-" or caracteres[i] == "/":
                impresion += caracteres[i]+" es un operador"'\n'
            #Si es una variable (minusculas)
            elif caracteres[i].islower():
                impresion += caracteres[i]+" es una variable"'\n'
            #Si no es parte del lexico
            else:
                impresion += caracteres[i]+" no se reconoce"'\n'
            i += 1       
        return impresion
    
inicio = Inicio()
salida = inicio.abrir_archivo()
inicio.escribir_archivo(salida)

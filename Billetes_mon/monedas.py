class cambio_monedas:


    def dar_cambio(cambio: float, monedas, resultado): #declaracion de metodo  con variables

        #el cambio debe ser mayor quje cero y las monedas  disponible deben ser que cero
        if cambio >0 and len(monedas)>0:
            #la moneda mas grande de lista de monedas
            moneda_grande = max(monedas)
            
            #se ejecuta siempre que haya cambio que dar
            if cambio - moneda_grande >= 0: #operacion (resta)

                #se da el valor de la moneda que se dio
                valor = resultado.get("Moneda: " + str(moneda_grande))
                #si no existe se agrega uno nuevo
                if valor is None:
                    #la moneda a dar mas la cantidad
                    resultado.update({"Moneda: " + str(moneda_grande): 1})
                #si el valor existe, y hay una moneda se suma otra a la siguiente denominacion
                else:
                    resultado.update({"Moneda: " + str(moneda_grande): valor + 1}) #verificacion del cambio que ya se entrego
                    
                cambio = cambio - moneda_grande #verificacion que se dio el cambio correcto 

            else:
                monedas.remove(moneda_grande)
                #se retorna el metodo para poder enseñar el que tiene y poder continuar con el conteo
            return cambio_monedas.dar_cambio(cambio,monedas,resultado)
                
        else:
            return resultado

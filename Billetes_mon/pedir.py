from monedas import cambio_monedas as cm

cambio: float
monedas=[100,50,20,10,5,2,1,.50,.20,.01] #las monedas disponibles

print("Ingresa el cambio") #pide cambio
cambio=float(input("cambio: ")) #lee el cambio
monedas_dadas = cm.dar_cambio(cambio, monedas, {}) #

print(f"Se le entregan las siguientes monedas: {monedas_dadas}") #regresa una lista con las monedas a dar 
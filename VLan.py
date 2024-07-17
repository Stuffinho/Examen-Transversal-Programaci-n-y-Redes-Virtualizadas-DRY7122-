def verificar_vlan(numero_vlan):
    numero_vlan = int(numero_vlan)  

    if 1 <= numero_vlan <= 1005:
        return "La VLAN {} pertenece al rango normal.".format(numero_vlan)
    elif 1006 <= numero_vlan <= 4094:
        return "La VLAN {} pertenece al rango extendido.".format(numero_vlan)
    else:
        return "El número de VLAN {} no es válido.".format(numero_vlan)

if __name__ == "__main__":
    vlan = input("Ingrese el número de VLAN: ")
    resultado = verificar_vlan(vlan)
    print(resultado)
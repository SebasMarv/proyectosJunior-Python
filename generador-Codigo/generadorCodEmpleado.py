#Manejo de cadenas (Basico)

def autogenerador(empleado,zona,turno,sexo):
    nom=empleado[0:1]
    pat=empleado[empleado.find(' ')+1:empleado.find(' ')+2]
    posicion=empleado.find(' ',empleado.find(' ')+1)
    mat=empleado[posicion+1:posicion+2]
    zona=zona[0:3]
    if turno.upper()=='MAÑANA':
        turno='1'
    elif turno.upper()=='TARDE':
        turno='2'
    else:
        turno='3'
    sexo=sexo[0:1]
    codigo=(nom+pat+mat+zona+turno+sexo).upper()
    print('Su codigo es: ',codigo)

autogenerador('Juan Romero Aliaga','norte','noche','masculino')
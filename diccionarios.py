#diccionarios {'llave','valor'}
alumno={'num_cta':'3434534654',
        'nombre': ('Jose','Perez','Garcia'),
        'semestre':1,
        'promedio':0.0,
        'materias':['CyP','algebra','Calculo','Geometria','IntroICO'],
        'regular':True,
        'lagrimas_por_examen':5,
        'direccion':{
            'calle':'Rancho Sequito',
            'colonia':'Impulsora Popular Agricola',
            'numero':1000,
            'cp':17570,
            'del_mun':'Nezahualcoyotl',
            'estado':{
                'nombre':'Estado de Mèxico',
                'corto':'EdoMex'
                }
            }
        
        }
print(alumno['direccion']['estado']['nombre'][10::].upper())
alumno['lagrimas_por_examen']=10
print(alumno)

"""
print(alumno['nombre']['direccion']['estado'][
print(alumno['materias'][1].upper()
print(alumno['nombre'])
print(alumno)
print(alumno['nombre'][1])
print(alumno['direccion']['cp'])
print(alumno['direccion']['cp'])
print(alumno['direccion']['estado']['corto'])
print(alumno['materias'][3::])



mi_lista=[['a','b'],['c',10],['d',True]]
diccionario = dict(mi_lista)
print(diccionario)
"""
#Son mutables
alumno['cursa_inglès'] = True
print(alumno)
#fincion keys()
llaves = alumno.keys()
print(llaves)
for llave in llaves:
    print('-----------')
    print(llave)
    print('..............')
    print(alumno[llave])
    print('+++++++++++++++')

#fincion values
    for val in alumno.values():
        print('....')
        print(val)
        print('++++++++++')
    #funcion items
for elem in alumno.items():
    print('.....')
    print(elem)
    print('++++++++++++')

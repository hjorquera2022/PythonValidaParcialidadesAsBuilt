#PythonValidaParcialidadesAsBuilt.py

import pandas as pd
import os

#*****
#***** Estructura completa
#*****
#├───ESTRUCTURA DE CARPETAS DE CADA PARCIALIDAD
#│   ├───DOCUMENTOS APROBADOS
#│   │   ├───REV LETRA
#│   │   │   ├───01 PDF
#│   │   │   └───02 EDITABLE
#│   │   └───REV NUMERO
#│   │       ├───01 PDF
#│   │       └───02 EDITABLE
#│   └───DOCUMENTOS VIGENTES
#│       ├───01 PDF
#│       │   ├───CON OBSERVACIONES
#│       │   └───SIN OBSERVACIONES
#│       └───02 EDITABLE
#│           ├───CON OBSERVACIONES
#│           └───SIN OBSERVACIONES

#│   ├───DOCUMENTOS ASBUILT 

#       ├───01 PDF
#       │   ├───APROBADOS
#       │   └───OBSERVADOS
#       └───02 EDITABLE
#           ├───APROBADOS
#           └───OBSERVADOS



# Ruta base donde se deben verificar los subdirectorios
#ruta_base = 'C:\\Users\\hjorquera\\Desktop\\Minuta explicativa planimetria de repositorio\\01 PARCIALIDADES\\'  
ruta_base = 'R:\\01 PARCIALIDADES\\'  

# Nombre del archivo de log
archivo_log = 'R:\\01 PARCIALIDADES\\0000-00 ADMINISTRACION\\LOG\\log_ValidarCrearAsBuilt.txt'

# Planilla con la lista de parcialidades
archivo_excel = 'R:\\01 PARCIALIDADES\\Listado de Parcialidades_ASBUILT.xlsx'

# Lista de carpetas y subcarpetas
estructura = [
            'DOCUMENTOS ASBUILT/01 PDF/APROBADOS',
            'DOCUMENTOS ASBUILT/01 PDF/OBSERVADOS',
            'DOCUMENTOS ASBUILT/02 EDITABLE/APROBADOS',
            'DOCUMENTOS ASBUILT/02 EDITABLE/OBSERVADOS',
             ]

# Carga el archivo Excel en un DataFrame Hoja de Parcialidades.
df = pd.read_excel(archivo_excel, sheet_name='PARCIALIDADES')

# Filtra el DataFrame para considerar solo parcialidades a 'PROCESAR' igual a 'S'
df_parcialidades = df[df['PROCESAR'] == 'S']

# Abre el archivo de log en modo de escritura
with open(archivo_log, 'w') as log_file:
    # Itera a través de cada parcialidad y la procesa
    for parcialidad in df_parcialidades['PARCIALIDAD']:
        ruta_subdirectorio = os.path.join(ruta_base, parcialidad)
        log_file.write(f'Parcialidad: {parcialidad}\n')
        # Iterar a través de la estructura y crear carpetas si no existen
        for carpeta in estructura:
            ruta_carpeta = os.path.join(ruta_subdirectorio, carpeta)
            if not os.path.exists(ruta_carpeta):
                os.makedirs(ruta_carpeta)
                print(f"La carpeta '{ruta_carpeta}' ha sido creada.")
                log_file.write(f"La carpeta '{ruta_carpeta}' ha sido creada.\n")
            else:
                log_file.write(f"La carpeta '{ruta_carpeta}' ya existe.\n")

print("Proceso finalizado. Los resultados se han guardado en el archivo de log.")


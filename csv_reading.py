import pandas as pd

def renameColumns(data_frame):

    new_columns = {"Código": "codigo", "Curso": "curso", "Asignatura": "asignatura", "Docentes":"profesores", 
                "Días": "dias", "Hora Inicio": "hora inicio", "Hora Fin": "hora fin", "Tipo Clase": "tipo clase", 
                "Vacantes": "vacantes", "Aula": "aula", "Sede": "sede"}
    df_renamed = data_frame.rename(columns=new_columns)

    return df_renamed

def createDataFrame(csv_file):
    df = pd.read_csv(csv_file)
    df = renameColumns(df)

    return df
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

def main():
    createDataFrame(csv_file='schedule.csv')
    dimensions = df.shape
    analisis_matematico_2 = df[df['Asignatura'].isin(['ANALISIS MATEMATICO II A', 'ANÁLISIS MATEMÁTICO II'])]
    ensayo_de_pozo_prof = df.loc[df['Asignatura'] == 'ENSAYO DE POZO', 'Docentes']


    print(df_renamed)
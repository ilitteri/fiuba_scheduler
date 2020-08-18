import pandas as pd

def createDataFrame(csv_file):
    df = pd.read_csv(csv_file)
    df.columns = ["codigo", "curso", "asignatura", "profesores", "dias", "hora inicio", 
                "hora fin", "tipo de clase", "vacantes", "aula", "sede"]

    return df
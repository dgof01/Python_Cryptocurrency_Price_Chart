from datetime import datetime, timedelta
import pandas as pd
import pandas_datareader as pdr

def obtenerDatos(criptomoneda, moneda):
    actual = datetime.now()
    fechaActual = actual.strftime("%Y-%m-%d")
    fechaAnterior = (actual - timedelta(days=35)).strftime("%Y-%m-%d")

    inicio = pd.to_datetime(fechaAnterior)
    fin = pd.to_datetime(fechaActual)

    datos = pdr.get_data_yahoo(f'{criptomoneda}-{moneda}', inicio, fin)
    return datos

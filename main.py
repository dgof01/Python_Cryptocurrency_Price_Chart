from datos.obtenerDatos import obtenerDatos
from grafica.graficarDatos import graficar

if __name__=='__main__':
    CRIPTOMONEDAS = ['DOGE','USDT','ADA', 'ETH', 'BTC']
    MONEDA = 'USD'
    SIMBOLO_MONEDA = '$'

    datos_cripto = {cripto:obtenerDatos(cripto, MONEDA) for cripto in CRIPTOMONEDAS}

    graficar(datos_cripto, MONEDA, SIMBOLO_MONEDA)

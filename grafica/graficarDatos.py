import plotly.graph_objects as go

def graficar(datos_cripto, moneda, simbolo_moneda):
    grafico = go.Figure()
    for i, name in enumerate(datos_cripto):
        print(name)
        grafico = grafico.add_trace(
                go.Scatter(
                    x = datos_cripto[name].index,
                    y = datos_cripto[name].Close,
                    name = name
                    )
                )
    grafico.update_layout(
            title = 'Criptomonedas',
            xaxis_title = 'Fecha',
            yaxis_title = f'Precio en {moneda}')
    grafico.update_yaxes(type = 'log', tickprefix = simbolo_moneda)
    grafico.show()

from flask import Flask, Response
import pandas as pd

app = Flask(__name__)

@app.route('/miembros', methods=['GET'])
def miembros():
    try:
        df = pd.read_excel('Votaciones.xlsx')

        # Limpiar columnas
        df.columns = df.columns.str.strip().str.upper()

        resultado = ""

        for _, row in df.iterrows():
            if str(row['MIEMBRO DE MESA']).strip().lower() == 'si':

                dni = str(row['DNI']) if pd.notna(row['DNI']) else ""
                miembro = str(row['MIEMBRO DE MESA']) if pd.notna(row['MIEMBRO DE MESA']) else ""
                ubicacion = str(row['UBICACIÓN']) if pd.notna(row['UBICACIÓN']) else ""
                direccion = str(row['DIRECCIÓN']) if pd.notna(row['DIRECCIÓN']) else ""

                resultado += f"{dni} / {miembro} / {ubicacion} / {direccion}\n"

        return Response(resultado, mimetype='text/plain')

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
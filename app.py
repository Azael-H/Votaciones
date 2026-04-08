from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/miembros', methods=['GET'])
def miembros():
    try:
        df = pd.read_excel('Votaciones.xlsx')

        # Limpiar nombres de columnas (evita errores)
        df.columns = df.columns.str.strip().str.upper()

        resultado = []

        for _, row in df.iterrows():
            if str(row['MIEMBRO DE MESA']).strip().lower() == 'si':
                resultado.append({
                    "DNI": str(row['DNI']),
                    "Ubicacion": row['UBICACIÓN'],
                    "Local": row['DIRECCIÓN']
                })

        return jsonify(resultado)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
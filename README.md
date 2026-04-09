# Verificador de Miembros de Mesa

Aplicación en Python que lee una lista de DNIs desde un Excel, consulta la página de la Reniec y genera otro Excel con la informacion de los DNI colocados.

## Requisitos

Docker instalado
Archivo dnis.xlsx con una columna llamada DNI

## Construir la imagen

'''bash
docker build -t miembro-mesa:v1 .

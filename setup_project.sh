#!/bin/bash

# Verificar si Python3 está instalado
if ! command -v python3 &> /dev/null
then
    echo "Python3 no está instalado. Instálalo antes de continuar."
    exit
fi

# Verificar si ya estamos en un entorno virtual
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "Ya estás en un entorno virtual: $VIRTUAL_ENV"
else
    # Crear un entorno virtual
    echo "Creando entorno virtual..."
    python3 -m venv venv

    # Activar el entorno virtual
    echo "Activando el entorno virtual..."
    source venv/bin/activate

    # Verificar si existe el archivo requirements.txt
    if [ -f "requirements.txt" ]; then
        echo "Instalando dependencias desde requirements.txt..."
        pip install -r requirements.txt
    else
        echo "No se encontró requirements.txt. Continuando sin instalar dependencias..."
    fi
fi

# Ejecutar las pruebas
echo "Ejecutando pruebas unitarias..."
python -m unittest discover -s tests

# Desactivar el entorno virtual después de la ejecución
# deactivate

echo "Configuración y pruebas completadas."

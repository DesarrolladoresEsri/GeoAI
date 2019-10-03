# Proceso para el entrenamiento de un modelo para clasificación de imágenes

Este procedimiento expone la forma de entrenar un modelo para hacer clasificación de imágenes.

## Configuración de la estructura de los datos

Se necesitan una estructura de carpetas para empezar, se recomienda la siguiente:

```folder
📦project
 ┣ 📂test
 ┃ ┣ 📂images
 ┃ ┗ 📜train.csv
 ┗ 📂train
 ┃ ┣ 📂images
 ┃ ┗ 📜test.csv
```

El siguiente codigo guardarlo como _gen_structure.bat_ y ejecutar sobre la carpeta donde se quiere crear la estructura para el proyecto.

```bash
@echo off
set /p project_name=Enter Project Name: 
echo %project_name%
md %project_name%
cd %project_name%
md train
md train\images
md test
md test\images
echo. 2>test/test.csv
echo. 2>train/train.csv
```

# Proyecto de Estimación de Precios de Automóviles Usados

Este proyecto desarrolla un modelo de machine learning para estimar el valor de mercado de automóviles usados. La aplicación permitirá a los usuarios de Rusty Bargain obtener rápidamente una estimación precisa del precio de sus coches basándose en el historial de especificaciones, versiones de equipamiento y precios previos.

## Descripción del Proyecto

Rusty Bargain busca un modelo que ofrezca:
- Alta calidad de predicción.
- Velocidad de predicción adecuada para uso en una aplicación.
- Tiempo de entrenamiento eficiente.

El conjunto de datos contiene información sobre autos usados, y este análisis utiliza varios modelos de regresión para encontrar la mejor opción que cumpla con los requisitos de precisión y eficiencia.

## Estructura del Análisis

1. **Preparación de los Datos**
   - Se cargan y preprocesan los datos del archivo `car_data.csv`.
   - Se emplean técnicas de limpieza de datos, como la imputación de valores faltantes y el escalado de características.

2. **Entrenamiento de Modelos**
   - Se implementan varios modelos, entre ellos `LinearRegression`, `RandomForestRegressor`, `CatBoostRegressor`, `LightGBM` y `XGBoost`.
   - Se utiliza `train_test_split` para dividir los datos y evaluar el desempeño de los modelos en datos de validación.

3. **Evaluación de Modelos**
   - Los modelos se comparan en función de su precisión (usando métricas como RMSE y R2) y eficiencia.
   - Se mide el tiempo de entrenamiento y predicción para cada modelo, permitiendo la selección del mejor modelo en términos de precisión y velocidad.

4. **Conclusiones**
   - Se selecciona el modelo óptimo que equilibre precisión y velocidad de predicción, cumpliendo los requisitos de Rusty Bargain.

## Requisitos

- **Python 3.7+**
- Librerías: `pandas`, `numpy`, `scikit-learn`, `catboost`, `lightgbm`, `xgboost`, `missingno`, `plotly`, `matplotlib`

## Cómo Ejecutar el Proyecto

1. Clona el repositorio.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el notebook `project_12_1st_review.ipynb` para reproducir el análisis y las visualizaciones.

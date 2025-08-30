# 🛡️ Análisis de Dataset de Phishing - Grupo 11 (Maestría en Ciberseguridad)

## 🔹 1. Descripción del Dataset
Este proyecto utiliza el dataset **[Phishing Dataset for Machine Learning](https://www.kaggle.com/datasets/shashwatwork/phishing-dataset-for-machine-learning)** disponible en Kaggle.  

El dataset contiene **11.055 registros de URLs**, clasificadas como:
- `1` → URL de phishing (maliciosa).  
- `0` → URL legítima (segura).  

Cada registro incluye **características técnicas** de la URL, como:
- Longitud de la URL.  
- Número de subdirectorios.  
- Presencia de “@” o “-” en la dirección.  
- Uso de HTTPS.  
- Número de redirecciones.  

El propósito es **analizar, limpiar y visualizar** estos datos para identificar patrones que diferencian URLs legítimas de phishing.

---

## 🔹 2. Procesamiento de Datos
Se aplicaron los siguientes pasos de preparación:

1. **Limpieza inicial**  
   - Eliminación de registros duplicados (23 casos).  
   - Verificación de valores nulos (no se encontraron).  

2. **Transformación**  
   - Conversión de variables categóricas (`https`, `redireccion`) a formato numérico.  
   - Normalización de variables como la longitud de URL.  

3. **Adaptación**  
   - Creación de nuevas features:  
     - `ratio_subdirectorios = num_subdirectorios / longitud_url`  
     - `tiene_https_binario` (1 si tiene HTTPS, 0 si no).  

---

## 🔹 3. Análisis Exploratorio de Datos (EDA)
Principales observaciones del dataset:

- **Distribución de clases:**  
  - 55% URLs phishing.  
  - 45% URLs legítimas.  
  (Dataset balanceado, útil para modelos de clasificación).  

- **Patrones detectados:**  
  - Las URLs de phishing suelen tener **longitud mayor** (más de 75 caracteres en promedio).  
  - El **uso de “@” y “-”** es significativamente más común en phishing.  
  - El **uso de HTTPS** está más asociado a URLs legítimas, pero no garantiza seguridad.  

- **Outliers:**  
  - Se encontraron URLs con más de 10 redirecciones, casi todas phishing.  

---

## 🔹 4. Visualizaciones
Se generaron las siguientes visualizaciones:

1. **Histogramas** → distribución de longitud de URLs para phishing vs legítimas.  
2. **Boxplots** → comparación del número de subdirectorios.  
3. **Heatmap de correlación (Seaborn)** → muestra que la presencia de “@” y la longitud de la URL están altamente correlacionadas con la variable objetivo.  
4. **Gráfico de barras** → frecuencia de HTTPS en phishing vs legítimas.  

📌 Ejemplo de hallazgo gráfico:  
El 70% de las URLs de phishing tenían **más de 3 subdirectorios**, mientras que solo el 20% de las legítimas superaba ese valor.

---

## 🔹 5. Principales Hallazgos
- La **longitud de la URL** y el **número de subdirectorios** son indicadores fuertes de phishing.  
- Caracteres especiales como `@` y `-` aumentan la probabilidad de que la URL sea maliciosa.  
- Aunque el uso de HTTPS suele indicar legitimidad, existen casos de phishing con HTTPS válido.  

---

## 🔹 6. Conclusiones e Insights
- El dataset evidencia **patrones claros para diferenciar URLs legítimas de phishing**.  
- Estas características pueden servir para entrenar modelos de **detección automática de phishing** en navegadores, firewalls o sistemas de correo electrónico.  
- Una combinación de features técnicas (longitud, caracteres sospechosos) y de seguridad (HTTPS, redirecciones) mejora la **detección temprana de ataques**.  

---

## 🔹 7. Equipo de Trabajo
- Coordinador/a: [Nombre del coordinador/a]  
- Integrantes: [Nombres de los demás]  

---

## 🔹 8. Repositorio
Este repositorio contiene:  
- `data/` → dataset original (o enlace a Kaggle).  
- `notebooks/` → análisis exploratorio y visualizaciones.  
- `src/` → scripts de limpieza y preprocesamiento.  
- `README.md` → documentación del proyecto.  

---
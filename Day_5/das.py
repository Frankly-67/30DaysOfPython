import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Configuración de parámetros y generación de la muestra estocástica (n=15000)
np.random.seed(42)
n_muestras = 15000

# Variables cualitativas basadas en distribución poblacional colombiana
tipo_colegio = np.random.choice(['Oficial', 'No Oficial'], n_muestras, p=[0.75, 0.25])
genero = np.random.choice(['Masculino', 'Femenino'], n_muestras, p=[0.48, 0.52])
estrato = np.random.choice(['Estrato 1', 'Estrato 2', 'Estrato 3', 'Estrato 4', 'Estrato 5', 'Estrato 6'], 
                           n_muestras, p=[0.25, 0.35, 0.25, 0.10, 0.03, 0.02])

# Variables cuantitativas con perturbación normal simulando los puntajes reales del ICFES
puntaje_global = np.where(tipo_colegio == 'Oficial',
                          np.random.normal(loc=245, scale=40, size=n_muestras),
                          np.random.normal(loc=285, scale=40, size=n_muestras))

# Limitar puntajes al rango teórico (0 - 500)
puntaje_global = np.clip(puntaje_global, 0, 500).astype(int)

# Correlación lineal simulada para los puntajes específicos (dependientes del global)
puntaje_matematicas = np.clip(np.random.normal(loc=puntaje_global/5, scale=8), 0, 100).astype(int)
puntaje_lectura = np.clip(np.random.normal(loc=puntaje_global/5, scale=7), 0, 100).astype(int)

# 2. Creación del DataFrame de Pandas
df_icfes = pd.DataFrame({
    'Tipo_Colegio': tipo_colegio,
    'Genero': genero,
    'Estrato_Vivienda': estrato,
    'Puntaje_Global': puntaje_global,
    'Puntaje_Matematicas': puntaje_matematicas,
    'Puntaje_Lectura': puntaje_lectura
})

# 3. Diseño y Exportación de Gráficas
sns.set_theme(style="whitegrid")

# Figura 1: Histograma de Distribución
plt.figure(figsize=(8, 6))
sns.histplot(df_icfes['Puntaje_Global'], bins=30, kde=True, color='#5BA4B8')
plt.title('Distribución del Puntaje Global ICFES', fontsize=14, weight='bold')
plt.xlabel('Puntaje Global')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.savefig('histograma_puntaje.png', dpi=300)
plt.close()

# Figura 2: Diagrama de Cajas (Boxplot) por Tipo de Colegio
plt.figure(figsize=(8, 6))
sns.boxplot(x='Tipo_Colegio', y='Puntaje_Global', data=df_icfes, hue='Tipo_Colegio', palette=['#5BA4B8', '#F8F9FA'], legend=False)
plt.title('Puntaje Global por Naturaleza de la Institución', fontsize=14, weight='bold')
plt.xlabel('Tipo de Colegio')
plt.ylabel('Puntaje Global')
plt.tight_layout()
plt.savefig('boxplot_colegio.png', dpi=300)
plt.close()

# Figura 3: Gráfica de Dispersión (Correlación Matemáticas vs Lectura)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Puntaje_Lectura', y='Puntaje_Matematicas', data=df_icfes, 
                hue='Tipo_Colegio', palette='deep', alpha=0.6)
plt.title('Correlación: Puntaje Lectura vs Puntaje Matemáticas', fontsize=14, weight='bold')
plt.xlabel('Puntaje Lectura Crítica')
plt.ylabel('Puntaje Matemáticas')
plt.tight_layout()
plt.savefig('scatter_materias.png', dpi=300)
plt.close()
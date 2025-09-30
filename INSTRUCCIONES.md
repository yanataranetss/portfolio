# Instrucciones de Uso

## 🚀 Inicio Rápido

### 1. Usar la Calculadora con tus Datos

```bash
cd tax_tools
python3 mi_calculo.py
```

### 2. Personalizar con tus Datos Reales

Abre el archivo `tax_tools/mi_calculo.py` y modifica la sección marcada:

```python
# =============================================================================
# MODIFICA ESTOS VALORES CON TUS DATOS
# =============================================================================

# 1. DATOS DEL CONTRATO LABORAL
salario_neto_mensual = 500  # Tu salario neto mensual
retencion_trabajo = 0.20     # Tu retención de IRPF (20% = 0.20)
meses_trabajados = 12        # Meses trabajados en el año

# 2. DATOS DE FACTURAS (FREELANCE)
facturas_totales_ano = 15000  # CAMBIA ESTO: Total bruto facturado
retencion_facturas_actual = 0.15  # Retención actual (normalmente 15%)

# 3. GASTOS DEDUCIBLES
gastos_autonomos = 3600       # Cuotas mensuales × 12 (ej: 300€/mes)
gastos_material = 500         # Material, software, etc.
gastos_vivienda = 1200        # Proporción alquiler + suministros
gastos_formacion = 300        # Cursos, libros, etc.
gastos_asesoria = 400         # Asesor fiscal/contable
otros_gastos = 0              # Otros gastos justificados
```

### 3. Ejecutar de Nuevo

```bash
python3 mi_calculo.py
```

Verás un informe completo con:
- ✅ Tu situación actual
- ✅ Simulaciones con diferentes retenciones (20%, 25%, 30%)
- ✅ Comparación de escenarios
- ✅ Recomendaciones personalizadas
- ✅ Impacto en liquidez

## 📚 Documentación Completa

### Guías Disponibles

1. **Respuesta Rápida** → `docs/respuesta_rapida.md`
   - Respuestas directas a tus preguntas
   - Recomendaciones inmediatas

2. **Guía IRPF Completa** → `docs/guia_irpf.md`
   - Análisis detallado de retenciones
   - Alternativas (pagos fraccionados)
   - Optimización fiscal

3. **Checklist de Documentos** → `docs/checklist_documentos.md`
   - Lista completa de documentos necesarios
   - Plazos y calendarios fiscales
   - Gastos deducibles

## 🔧 Requisitos Técnicos

- Python 3.6 o superior
- No requiere librerías adicionales

## 📊 Ejemplo de Salida

```
================================================================================
CALCULADORA IRPF - TU CASO PERSONALIZADO
================================================================================

📊 RESUMEN DE TUS DATOS:
  Trabajo: 500€/mes neto × 12 meses
  Retención trabajo: 20.0%
  Facturas totales: 15,000.00€
  Retención facturas: 15.0%
  Gastos deducibles: 6,000.00€

================================================================================
ESCENARIO ACTUAL (Retención facturas: 15.0%)
================================================================================

  💼 Ingresos trabajo:            7,500.00€
  💰 Facturas brutas:            15,000.00€
  📉 Gastos deducibles:           6,000.00€
  📊 Base imponible total:       16,500.00€

  💸 Cuota tributaria:            3,337.50€
  ✂️  Retenciones totales:         3,750.00€

  🎉 RESULTADO:            412.50€  (A DEVOLVER)

================================================================================
COMPARACIÓN DE ESCENARIOS
================================================================================

Escenario            Retención    Retenciones     Resultado       Estado
--------------------------------------------------------------------------------
ACTUAL                   15%        3,750.00€       412.50€   A DEVOLVER
Opción 1                 20%        4,500.00€     1,162.50€   A DEVOLVER
Opción 2                 25%        5,250.00€     1,912.50€   A DEVOLVER
Opción 3                 30%        6,000.00€     2,662.50€   A DEVOLVER
```

## ❓ Preguntas Frecuentes

### ¿Qué datos necesito para calcular?

**Mínimo imprescindible:**
- Salario neto mensual y retención del trabajo
- Total de facturas emitidas en el año
- Retención aplicada en las facturas (normalmente 15%)
- Gastos deducibles (cuotas autónomos, material, etc.)

### ¿El cálculo es exacto?

Es una **estimación orientativa**. El cálculo real puede variar según:
- Deducciones autonómicas específicas
- Situación personal (hijos, discapacidad, etc.)
- Otras rentas no consideradas
- Cambios en la normativa fiscal

Para un cálculo oficial, consulta con un asesor fiscal.

### ¿Cómo sé qué retención elegir?

**Regla general:**
- Si el resultado sale **"A PAGAR"** más de 500€ → Aumenta la retención
- Si el resultado sale **"A DEVOLVER"** más de 1.500€ → Puedes reducir la retención
- Si está **equilibrado** (entre -500€ y +500€) → Mantén la retención actual

### ¿Qué es mejor: retención alta o pagos fraccionados?

**Retención alta:**
- ✅ Más simple (automático)
- ✅ No requiere trámites trimestrales
- ❌ Menos liquidez durante el año

**Pagos fraccionados (Modelo 130):**
- ✅ Ajustado a beneficio real (ingresos - gastos)
- ✅ Más flexible
- ❌ Requiere presentar modelo cada trimestre

**Recomendación:** Si tus gastos son >30% de ingresos, los pagos fraccionados suelen ser mejor opción.

## 🆘 Soporte

Si tienes dudas o encuentras problemas:
1. Revisa la documentación en `docs/`
2. Verifica que has introducido los datos correctamente
3. Consulta con un asesor fiscal para casos complejos

## 📝 Notas Importantes

- ⚠️ Los cálculos usan tramos de IRPF de 2024 (pueden cambiar)
- ⚠️ Se utilizan tipos medios (Estado + Autonómico)
- ⚠️ No incluye deducciones específicas por CCAA
- ⚠️ Esta herramienta NO sustituye asesoramiento profesional

## 🔄 Actualizaciones

Mantén el repositorio actualizado para tener los últimos tramos fiscales:

```bash
git pull origin main
```

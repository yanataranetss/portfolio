# Calculadora de IRPF - Guía Completa

## Respuesta a tu Consulta

### 1. Revisión de Facturas T3 y Resultado Aproximado

Para revisar tus facturas del T3 y calcular el resultado aproximado de la declaración de la renta, he creado una calculadora de IRPF que considera:

- Tus ingresos como autónomo (facturas)
- Tus gastos deducibles
- Tu salario neto de 500€/mes con retención del 20%
- Diferentes escenarios de retención (15%, 20%, 30%)

### 2. ¿Tiene Sentido Aumentar la Retención al 30%?

**Depende de tu situación específica.** Aquí están los factores clave:

#### Ventajas de aumentar al 30%:
- **Mayor seguridad fiscal**: Reduces significativamente el riesgo de tener que pagar en la declaración
- **Mejor planificación**: Evitas sorpresas desagradables en junio del año siguiente
- **Sin intereses de demora**: Si retienes de más, solo te devuelven (sin coste adicional)

#### Desventajas:
- **Menor liquidez mensual**: Cobras menos en cada factura
- **Uso del dinero**: Hacienda retiene tu dinero sin darte intereses
- **Posible devolución grande**: Podrías tener una devolución considerable que tardará en llegar

### 3. Impacto Aproximado de la Subida al 30%

La calculadora incluida (`calculadora_irpf.py`) te permite simular diferentes escenarios. Ejecuta:

```bash
python3 calculadora_irpf.py
```

**Ejemplo ilustrativo** (asumiendo facturación de ~19.000€/año):

| Retención | Retenido Anual | Resultado Declaración |
|-----------|----------------|-----------------------|
| 15%       | ~2.850€        | A pagar ~1.500€      |
| 20%       | ~3.800€        | A pagar ~500€        |
| 30%       | ~5.700€        | A devolver ~1.400€   |

*Nota: Estos son valores aproximados para ilustrar el concepto.*

### 4. Alternativas Recomendables

#### Opción A: Retención Progresiva
- Mantén 15-20% si tus gastos deducibles son altos (>30% de ingresos)
- Sube a 25-30% si tus gastos son bajos (<20% de ingresos)

#### Opción B: Pagos Fraccionados (Modelo 130) ⭐ RECOMENDADO
Si no tienes retención o es baja, **debes presentar el Modelo 130 trimestralmente**:

- **¿Qué es?**: Pago a cuenta del IRPF cada trimestre
- **Cuándo**: Días 1-20 de abril, julio, octubre y enero
- **Ventaja**: Repartes el pago durante el año
- **Cálculo**: 20% del beneficio trimestral (ingresos - gastos)

**Importante**: Si tus retenciones superan el 70% de tus ingresos, no tienes que presentar el 130.

#### Opción C: Ajuste Híbrido ⭐ MI RECOMENDACIÓN
1. Aplica retención del **20-25%** en facturas
2. Realiza pagos fraccionados (modelo 130) si procede
3. Revisa trimestralmente tu situación
4. Ajusta en T4 si es necesario

### 5. Documentos y Datos Adicionales Necesarios

Para un cálculo completo y preciso, necesitas:

#### Documentos Obligatorios:
- ✅ **Todas las facturas emitidas en 2024** (con fecha, importe base, IVA y retención)
- ✅ **Facturas de gastos deducibles**: 
  - Material y suministros
  - Gastos de oficina/coworking
  - Teléfono e internet (proporcional)
  - Software y herramientas profesionales
  - Formación relacionada con tu actividad
  - Asesoría y gestoría
  - Gastos de transporte (si procede)
- ✅ **Certificado de retenciones del trabajo** (te lo debe proporcionar tu empresa en enero/febrero)
- ✅ **Justificantes de cuotas de autónomos** pagadas a la Seguridad Social

#### Información Adicional Importante:
- 📋 ¿Tienes vivienda en propiedad con hipoteca? (deducción autonómica si la compraste antes de 2013)
- 📋 ¿Tienes hijos o personas a tu cargo? (mínimo familiar)
- 📋 ¿Realizaste aportaciones a planes de pensiones?
- 📋 ¿Tienes otros ingresos? (alquileres, dividendos, etc.)

### 6. Cómo Usar la Calculadora

#### Instalación:
```bash
# No requiere instalación, solo Python 3
python3 calculadora_irpf.py
```

#### Personalizar con Tus Datos:

Edita el archivo `calculadora_irpf.py` en la función `ejemplo_caso_real()`:

```python
# Tus facturas reales del T3
facturas_t3 = [1500, 1800, 1600]  # Sustituye por tus importes reales

# Tus gastos deducibles del T3
gastos_t3 = 400  # Sustituye por tus gastos reales

# Tu salario neto mensual
salario_neto = 500  # Ya está configurado

# Comparar diferentes retenciones
comparar_escenarios(facturas_anuales, gastos_anuales, salario_neto, [15, 20, 25, 30])
```

### 7. Ejemplo de Uso Avanzado

Crea un archivo `mi_calculo.py`:

```python
from calculadora_irpf import CalculadoraIRPF

# Crear calculadora
calc = CalculadoraIRPF()

# Agregar tus facturas del año con retención actual (ej: 15%)
calc.agregar_factura(1500, 15)  # Factura enero: 1.500€, retención 15%
calc.agregar_factura(1800, 15)  # Factura febrero: 1.800€, retención 15%
# ... agregar todas tus facturas

# Agregar gastos deducibles totales del año
calc.agregar_gastos_deducibles(1600)  # Total gastos anuales

# Agregar salario
calc.agregar_salario(500, 20, 12)  # 500€ neto/mes, 20% retención, 12 meses

# Ver resultado
calc.imprimir_resultado()
```

## Resumen Ejecutivo

### Para tu caso específico:

**Situación actual:**
- Salario: 500€/mes neto (retención 20%)
- Actividad autónomo: Facturas T3 presentadas
- Dudas sobre retención óptima

**Recomendación:**

1. **URGENTE**: Verifica si debes presentar el **Modelo 130** (pago fraccionado) del T3
   - Plazo: 1-20 octubre (para T3)
   - Solo si tus retenciones no superan el 70% de ingresos

2. **Retención óptima**: 
   - Si gastos < 20% ingresos → Retención 25-30%
   - Si gastos > 30% ingresos → Retención 20%
   - Si gastos > 40% ingresos → Retención 15%

3. **Cálculo exacto**: Usa la calculadora con **tus datos reales**:
   ```bash
   python3 calculadora_irpf.py
   ```

4. **Documentación**: Recopila todos los documentos listados arriba

5. **Asesoramiento**: Considera consultar con un gestor/asesor fiscal para:
   - Confirmar cálculos
   - Optimizar deducciones
   - Gestionar modelo 130

## Importante ⚠️

Esta calculadora proporciona **estimaciones aproximadas**. Para cálculos exactos:
- Los tramos de IRPF incluyen parte estatal + autonómica (puede variar según CCAA)
- No incluye deducciones específicas (vivienda, familia, etc.)
- No considera reducciones autonómicas especiales
- El salario tiene reducciones por rendimientos del trabajo

**Siempre consulta con un profesional fiscal para decisiones importantes.**

## Preguntas Frecuentes

### ¿Cuándo debo presentar la declaración?
- Campaña de renta: Abril - Junio del año siguiente

### ¿Puedo cambiar mi retención durante el año?
- Sí, puedes aplicar la retención que consideres en cada factura nueva
- Las facturas ya emitidas no se pueden modificar

### ¿Qué pasa si me retengo de menos?
- Tendrás que pagar la diferencia en la declaración (junio)
- Posibles intereses si no hiciste pagos fraccionados (modelo 130)

### ¿Y si me retengo de más?
- Hacienda te devolverá el exceso (sin intereses)
- La devolución tarda normalmente 1-3 meses

## Contacto y Soporte

Para dudas sobre la calculadora, consulta el código fuente: `calculadora_irpf.py`

Para asesoramiento fiscal personalizado, contacta con:
- Colegio de Gestores Administrativos
- Asesor fiscal/gestor profesional
- AEAT (Agencia Tributaria): 901 33 55 33

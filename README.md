# Portfolio de Herramientas Fiscales IRPF

Herramientas y documentación para el cálculo y optimización del IRPF (Impuesto sobre la Renta de las Personas Físicas) en España.

## 📋 Contenido

### 🧮 Calculadora IRPF
Herramienta para calcular el resultado estimado de la declaración de la renta considerando:
- Ingresos del trabajo por cuenta ajena
- Ingresos de actividades económicas (freelance)
- Gastos deducibles
- Simulación de diferentes escenarios de retención

**Ubicación**: `tax_tools/irpf_calculator.py`

### 📚 Documentación

#### Guía de Asesoramiento Fiscal
Respuestas detalladas sobre:
- ¿Tiene sentido aumentar la retención del 15% al 30%?
- Impacto de cambios en las retenciones
- Alternativas: pagos fraccionados, optimización de gastos
- Recomendaciones personalizadas

**Ubicación**: `docs/guia_irpf.md`

#### Checklist de Documentación
Lista completa de documentos necesarios para:
- Cálculo estimado de la declaración
- Presentación de modelos trimestrales
- Declaración anual de la renta

**Ubicación**: `docs/checklist_documentos.md`

## 🚀 Uso Rápido

### Requisitos
- Python 3.6 o superior

### Calcular Resultado Estimado

```bash
python3 tax_tools/irpf_calculator.py
```

### Personalizar el Cálculo

Edita `tax_tools/irpf_calculator.py` y modifica los valores en la función `main()`:

```python
# Tu salario mensual neto y retención
calc.add_employment_income(net_monthly=500, withholding_rate=0.20, months=12)

# Tus facturas totales y retención actual
calc.add_freelance_income(gross_income=20000, withholding_rate=0.15)

# Tus gastos deducibles
calc.set_deductible_expenses(3000)
```

## 📊 Respuesta a tu Consulta

### Estado Actual
✅ Facturas T3 recibidas y subidas a la plataforma

### Información Pendiente
Para hacer un cálculo preciso, necesitamos:
- ⚠️ Facturas de T1, T2 y T4 (o proyección anual)
- ⚠️ Total de gastos deducibles con justificantes
- ⚠️ Certificado de retenciones del contrato laboral

### Recomendaciones Preliminares

**1. ¿Aumentar retención al 30%?**
- Depende de tus ingresos totales anuales
- Si facturas + trabajo > 22.000€/año → Recomendable
- Consulta la guía completa en `docs/guia_irpf.md`

**2. Alternativas**
- Pagos fraccionados trimestrales (Modelo 130)
- Optimización de gastos deducibles
- Retención intermedia (20-25%)

**3. Documentos Necesarios**
- Revisa el checklist completo en `docs/checklist_documentos.md`

## 🔧 Herramientas Disponibles

### Calculadora con Ejemplos

```bash
cd /home/runner/work/portfolio/portfolio
python3 tax_tools/irpf_calculator.py
```

Salida ejemplo:
```
=== CÁLCULO ACTUAL (15% retención facturas) ===
employment_income: 7500.00€
freelance_gross: 15000.00€
deductible_expenses: 3000.00€
total_taxable: 19500.00€
total_tax: 3990.00€
total_withholdings: 3750.00€
result: -240.00€
status: A PAGAR

=== SIMULACIÓN CON 30% RETENCIÓN ===
result: 2010.00€
status: A DEVOLVER

Diferencia en resultado: 2250.00€
```

## 📞 Próximos Pasos

1. **Recopila toda la información** usando el checklist
2. **Ejecuta la calculadora** con tus datos reales
3. **Revisa las recomendaciones** en la guía de asesoramiento
4. **Toma una decisión informada** sobre retenciones

## ⚖️ Aviso Legal

Esta herramienta proporciona estimaciones orientativas. Para asesoramiento fiscal personalizado y vinculante, consulta con un asesor fiscal colegiado.

## 🤝 Contribuciones

Si encuentras errores o quieres mejorar las herramientas, las contribuciones son bienvenidas.

## 📝 Licencia

Este proyecto es de código abierto y está disponible para uso personal y educativo.
# Guía de Asesoramiento Fiscal IRPF

## Análisis de Retenciones y Estimación de Resultado

### Contexto del Usuario

El usuario tiene dos fuentes de ingresos:
1. **Contrato laboral**: ~500€ neto mensual con retención del 20% IRPF
2. **Actividad freelance**: Facturas del T3 con retención actual (típicamente 15%)

### Preguntas Planteadas

#### 1. Resultado Aproximado de la Declaración

Para calcular el resultado aproximado necesitamos:

**Datos Necesarios:**
- ✅ Ingresos brutos del contrato laboral (calculable desde neto y retención)
- ✅ Retenciones del contrato laboral
- ⚠️ **FALTA**: Importe bruto total de facturas del T3 y Q1-Q4
- ⚠️ **FALTA**: Retenciones aplicadas en facturas
- ⚠️ **FALTA**: Gastos deducibles de la actividad freelance

**Cálculo Básico:**
```
Resultado = Retenciones Totales - Cuota Tributaria

Donde:
- Retenciones Totales = Retenciones trabajo + Retenciones facturas
- Cuota Tributaria = Impuesto calculado sobre base imponible total
```

#### 2. ¿Tiene Sentido Aumentar la Retención al 30%?

**Factores a Considerar:**

✅ **Ventajas de aumentar al 30%:**
- Reduce riesgo de tener que pagar en la declaración
- Mejor planificación fiscal (evita sorpresas)
- Funciona como "ahorro forzoso"

❌ **Desventajas:**
- Menor liquidez mensual
- El Estado retiene tu dinero sin intereses
- Posible devolución mayor (pero tardía)

**Recomendación General:**
- Si tus ingresos totales superan los 22.000€/año → Aumentar retención puede ser prudente
- Si tienes pocos gastos deducibles → Mayor retención reduce riesgo
- Si tu actividad es irregular → Considerar pagos fraccionados trimestral

#### 3. Impacto de Subir la Retención al 30%

**Ejemplo de Cálculo:**

Supongamos facturas anuales de 20.000€:

| Concepto | Retención 15% | Retención 30% | Diferencia |
|----------|---------------|---------------|------------|
| Facturas brutas | 20.000€ | 20.000€ | - |
| Retención | 3.000€ | 6.000€ | +3.000€ |
| A recibir | 17.000€ | 14.000€ | -3.000€ |

**Impacto en Declaración:**
- Si con 15% resultaba a pagar 2.000€ → Con 30% resultaría a devolver 1.000€
- Diferencia: +3.000€ más retenido = cambio de resultado

#### 4. Alternativas Recomendables

##### Opción A: Pagos Fraccionados (Modelo 130)
**¿Qué es?**
- Pago trimestral del 20% del beneficio neto (ingresos - gastos)
- Alternativa o complemento a las retenciones

**¿Cuándo es obligatorio?**
- Si más del 70% de tus ingresos NO tienen retención
- En tu caso: Depende del peso relativo trabajo vs. freelance

**Ventajas:**
- Ajuste más preciso a tu capacidad de pago
- Puedes descontar gastos trimestralmente
- Evita retenciones excesivas

**Cómo funciona:**
```
Pago Fraccionado = (Ingresos - Gastos) × 20% - Retenciones - Pagos anteriores
```

##### Opción B: Ajustar Retención Gradualmente
- En lugar de saltar de 15% a 30%, probar con 20-25%
- Evaluar resultado y ajustar año siguiente

##### Opción C: Optimizar Gastos Deducibles
- Revisar todos los gastos deducibles posibles
- Reduce base imponible → menos cuota a pagar

**Gastos Deducibles Comunes:**
- Material de oficina y software
- Proporción de vivienda si trabajas desde casa (7-30%)
- Seguridad Social (cuota de autónomos)
- Formación relacionada con actividad
- Suministros (luz, internet) proporcional
- Desplazamientos profesionales
- Asesoría fiscal

#### 5. Documentos y Datos Adicionales Necesarios

**Para Cálculo Completo:**

📋 **Documentos Obligatorios:**
- [ ] Todas las facturas emitidas (Q1-Q4, no solo Q3)
- [ ] Justificantes de retenciones (certificados 190 y 100)
- [ ] Certificado de retenciones del trabajo (modelo 145/190)
- [ ] Recibos de autónomos pagados
- [ ] Justificantes de gastos deducibles

📋 **Datos Adicionales:**
- [ ] Importe bruto anual del contrato laboral
- [ ] Retenciones totales del trabajo
- [ ] Importe bruto total facturas (anual)
- [ ] Total gastos deducibles con justificantes
- [ ] Situación personal: estado civil, hijos, discapacidad, etc.

📋 **Opcional pero Recomendable:**
- [ ] Declaración de renta del año anterior
- [ ] Aportaciones a planes de pensiones (reducen base)
- [ ] Deducciones autonómicas aplicables

### Recomendación Inmediata

**Pasos a Seguir:**

1. **Recopilar Información Completa**
   - Suma total de facturas emitidas (anual)
   - Calcula total de gastos deducibles con justificantes

2. **Usar Calculadora IRPF**
   - Ejecutar: `python tax_tools/irpf_calculator.py`
   - Introducir datos reales para estimación

3. **Simulación con Diferentes Escenarios**
   - Comparar retención 15% vs 20% vs 30%
   - Evaluar pagos fraccionados vs retenciones

4. **Decisión Informada**
   - Si riesgo de pagar > 1.000€ → Aumentar retención
   - Si situación ajustada → Mantener y hacer pagos fraccionados
   - Si devolución segura > 2.000€ → Reducir retención

### Contacto y Próximos Pasos

Una vez tengas:
- Importe bruto total de facturas (anual)
- Total de gastos deducibles
- Certificado de retenciones del trabajo

Podremos hacer un cálculo preciso y darte una recomendación personalizada.

**Nota Legal:** Esta guía es orientativa. Para asesoramiento fiscal personalizado, consulta con un asesor fiscal colegiado.

# Respuesta Rápida a tu Consulta

## 📋 Tu Situación
- Contrato laboral: ~500€ neto/mes con 20% IRPF
- Facturas T3 subidas a la plataforma
- Retención actual en facturas: 15% (estimado)
- Planteas: Subir retención al 30%

## ❓ Tus Preguntas

### 1. ¿Qué resultado me saldrá en la declaración?

**No puedo calcularlo con precisión todavía** porque me faltan datos:

❌ **Faltan:**
- Importe total de todas tus facturas (T1+T2+T3+T4)
- Retenciones exactas aplicadas en las facturas
- Total de gastos deducibles (Seguridad Social, material, etc.)
- Importe bruto anual del contrato laboral

✅ **Tengo:**
- Facturas T3 (pendiente de revisar importes)
- Información del contrato: 500€ neto, 20% retención

**Para calcularlo necesito que me proporciones:**
1. Suma total de facturas emitidas en el año (o proyección)
2. Suma de gastos deducibles con justificantes
3. Certificado de retenciones del trabajo

### 2. ¿Tiene sentido subir la retención al 30%?

**Análisis preliminar:**

✅ **SÍ tiene sentido si:**
- Tus ingresos totales (trabajo + facturas) > 22.000€/año
- Tienes pocos gastos deducibles
- Prefieres no tener sorpresas (pagar en abril-junio)
- No necesitas liquidez inmediata

❌ **NO tiene sentido si:**
- Tus ingresos totales < 15.000€/año
- Tienes muchos gastos deducibles (>30% de facturas)
- Prefieres gestionar tu dinero y hacer pagos fraccionados

**Estimación rápida (APROXIMADA):**

Supongamos:
- Contrato: 500€ neto × 12 = 6.000€ neto → ~7.500€ bruto
- Facturas año: 20.000€ bruto
- Gastos: 4.000€
- **Ingresos netos totales: 23.500€**

Con estos números, **probablemente** tendrías que pagar algo en la declaración con 15% de retención en facturas. Subir al 30% **reduciría ese riesgo**.

### 3. ¿Qué impacto tendría subir al 30%?

**Impacto en liquidez:**
- Por cada 1.000€ facturados:
  - Con 15%: Recibes 850€
  - Con 30%: Recibes 700€
  - **Diferencia: -150€ por cada 1.000€ facturados**

**Impacto en declaración:**
Si facturas 20.000€/año:
- Diferencia en retenciones: +3.000€
- En la renta: Pasar de "a pagar ~1.500€" a "a devolver ~1.500€"
- **Ahorro de sorpresas: Sí**
- **Ahorro fiscal: No** (pagas lo mismo, solo cambias cuándo)

### 4. ¿Hay alternativas?

**SÍ, varias opciones:**

#### Opción A: Pagos Fraccionados (Modelo 130)
- Pagas el 20% del beneficio (ingresos - gastos) cada trimestre
- Más ajustado que retenciones fijas
- Obligatorio si >70% ingresos sin retención

**¿Cuándo aplicar?**
- Si tus ingresos freelance > ingresos trabajo
- Si tienes gastos significativos (>20% de ingresos)

#### Opción B: Retención Intermedia (20-25%)
- No saltar directamente a 30%
- Probar con 20% o 25% primero
- Evaluar resultado y ajustar

#### Opción C: Optimizar Gastos Deducibles
**Antes de subir retención, asegúrate de deducir TODO:**
- ✅ Cuotas de autónomos (300€/mes = 3.600€/año)
- ✅ Proporción de vivienda (7-30% de alquiler/IBI + suministros)
- ✅ Material y software profesional
- ✅ Formación relacionada
- ✅ Internet y teléfono (proporción profesional)
- ✅ Asesoría fiscal

**Ejemplo:** 
Si tienes 6.000€ de gastos deducibles en vez de 3.000€:
- Reduces base imponible en 3.000€
- Ahorras ~900€ en cuota (30% de 3.000€)
- **Puede ser más efectivo que subir retención**

### 5. ¿Falta algún documento?

**SÍ, para cálculo completo necesito:**

🔴 **CRÍTICO (sin esto no puedo calcular):**
- [ ] Facturas de TODOS los trimestres (Q1, Q2, Q3, Q4) o proyección anual
- [ ] Total de gastos deducibles con justificantes
- [ ] Certificado de retenciones del contrato laboral

🟡 **IMPORTANTE (para afinar cálculo):**
- [ ] Recibos de autónomos pagados
- [ ] Justificantes de gastos (alquiler, luz, material, etc.)
- [ ] Declaración de renta del año anterior (si hay)

🟢 **OPCIONAL (para optimizar):**
- [ ] Aportaciones a planes de pensiones
- [ ] Situación familiar (hijos, discapacidad, etc.)

## 🎯 Recomendación Inmediata

**PASO 1:** Recopila la información crítica
```
- Suma TODAS tus facturas del año (o estima el total anual)
- Calcula tus gastos deducibles TOTALES
- Consigue el certificado de retenciones del trabajo
```

**PASO 2:** Ejecuta la calculadora
```bash
cd /home/runner/work/portfolio/portfolio
# Edita tax_tools/irpf_calculator.py con tus datos reales
python3 tax_tools/irpf_calculator.py
```

**PASO 3:** Decide según resultado
```
Si resultado < -1000€ (a pagar mucho):
  → Opción 1: Subir retención a 25-30%
  → Opción 2: Hacer pagos fraccionados (modelo 130)
  
Si resultado entre -500€ y +500€ (ajustado):
  → Mantener retención actual
  → Optimizar gastos deducibles
  
Si resultado > +1000€ (a devolver mucho):
  → Reducir retención (si es posible)
  → No cambiar nada (está bien así)
```

## 📞 Para Consulta Detallada

Una vez tengas los datos completos, vuelve con:
1. Total bruto de facturas anuales: _____€
2. Total gastos deducibles: _____€  
3. Ingreso bruto anual del trabajo: _____€

Y te daré una recomendación personalizada y precisa.

## ⚡ Respuesta Corta

**¿Subir al 30%?** → Probablemente SÍ si facturas >15.000€/año y gastos <5.000€/año

**¿Cuánto impacto?** → En liquidez: -15% del importe facturado. En renta: +15% más de retenciones acumuladas

**¿Alternativas?** → Pagos fraccionados (modelo 130) o retención intermedia (20-25%)

**¿Falta algo?** → Sí: totales anuales de facturas, gastos y certificado del trabajo

---

**Lee los documentos completos en:**
- `docs/guia_irpf.md` - Guía detallada
- `docs/checklist_documentos.md` - Checklist completo
- `README.md` - Instrucciones de uso de la calculadora

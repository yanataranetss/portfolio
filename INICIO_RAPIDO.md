# Guía de Inicio Rápido - Calculadora IRPF

## 🎯 ¿Por Dónde Empezar?

### Si tienes 2 minutos → Lee esto primero:

```
TU SITUACIÓN:
✓ Facturas como autónomo (T3 presentadas)
✓ Salario 500€/mes neto (retención 20%)
✓ Duda: ¿Aumentar retención al 30%?

RESPUESTA DIRECTA:
→ Mejor 20-25% que 30%
→ Con 30% te devolverán ~2.000€ (liquidez perdida)
→ Con 20% resultado equilibrado (~0€)
```

Lee: **RESPUESTA_RAPIDA.md** (5 min)

---

### Si tienes 10 minutos → Usa la calculadora:

```bash
# 1. Edita el archivo con tus datos reales
nano mi_calculo_personalizado.py

# 2. Modifica estas líneas (inicio del archivo):
mis_facturas = [1500, 1800, 1600, ...]  # Tus facturas reales
mis_gastos_deducibles = 1600            # Tus gastos reales
salario_neto_mensual = 500              # Tu salario real
retencion_actual = 15                   # Tu retención actual

# 3. Ejecuta
python3 mi_calculo_personalizado.py

# 4. Verás tu resultado real (a pagar/devolver)
```

---

### Si tienes 30 minutos → Entendimiento completo:

1. **Lee RESPUESTA_COMPLETA.md** (responde TODAS tus preguntas)
2. **Ejecuta la calculadora** con tus datos
3. **Revisa GUIA_IRPF.md** para profundizar

---

## 📚 Estructura del Repositorio

```
portfolio/
├── README.md                      # Inicio e introducción
├── INICIO_RAPIDO.md              # Este archivo
├── RESPUESTA_RAPIDA.md           # Respuesta en 5 minutos
├── RESPUESTA_COMPLETA.md         # Respuesta detallada (TODO)
├── GUIA_IRPF.md                  # Guía completa del sistema
│
├── calculadora_irpf.py           # Motor de cálculo
├── mi_calculo_personalizado.py   # TU archivo (editar aquí)
│
└── .gitignore                    # Archivos ignorados
```

---

## 🎨 Diagrama de Flujo

```
┌─────────────────────────────────────────────┐
│  EMPIEZA AQUÍ: ¿Qué quieres hacer?         │
└─────────────────────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
   ┌────────┐  ┌─────────┐  ┌─────────┐
   │Respuesta│  │ Calcular│  │Entender │
   │ Rápida │  │ mi IRPF │  │ a Fondo │
   └────────┘  └─────────┘  └─────────┘
        │            │            │
        ▼            ▼            ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│RESPUESTA_    │ │mi_calculo_   │ │GUIA_IRPF.md  │
│RAPIDA.md     │ │personaliza...│ │              │
│(5 min)       │ │python3 ...   │ │RESPUESTA_    │
└──────────────┘ │(15 min)      │ │COMPLETA.md   │
                 └──────────────┘ │(30 min)      │
                                  └──────────────┘
```

---

## ⚡ Respuestas Ultra-Rápidas

### ❓ ¿Cuánto pagaré/devolverán en la renta?

```python
python3 mi_calculo_personalizado.py
# Edita primero con tus datos reales
```

**Estimación rápida sin calculadora:**
- Retención 15% → Pagarás 500-1.500€
- Retención 20% → Resultado equilibrado (±200€)
- Retención 30% → Devolverán 1.500-2.500€

---

### ❓ ¿Subo retención al 30%?

**NO recomendado** para tu caso.

**Mejor opción: 20-25%**

Razones:
- ✅ Equilibrio seguridad/liquidez
- ✅ Resultado final ~0€
- ✅ No pierdes liquidez excesiva
- ✅ Mayor control mensual

---

### ❓ ¿Qué documentos necesito?

**Ahora mismo (Octubre):**
- [ ] Facturas T3 (tienes ✓)
- [ ] Gastos T3
- [ ] Revisar modelo 130 (URGENTE)

**Para la renta (Abril-Junio):**
- [ ] Todas las facturas del año
- [ ] Todos los gastos justificados
- [ ] Certificado retenciones trabajo
- [ ] Cuotas autónomos

Checklist completo en: **RESPUESTA_COMPLETA.md**

---

### ❓ ¿Qué es el modelo 130?

**En 30 segundos:**
- Pago trimestral a cuenta del IRPF
- Solo si retenciones < 70% ingresos
- Pagas 20% del beneficio trimestral
- Evita pagar intereses en la renta

**Plazo T3:** Hasta 20 octubre ⏰
**Plazo T4:** Hasta 20 enero 2025

¿Más info? → **GUIA_IRPF.md** sección "Modelo 130"

---

## 🚀 Caso de Uso: Tu Primer Cálculo

### Paso 1: Recopila estos datos (5 min)

```
✍️ Mis facturas de 2024 (aproximadas):
   Enero:    _______€
   Febrero:  _______€
   Marzo:    _______€
   [...]
   TOTAL:    _______€

✍️ Mis gastos de 2024:
   TOTAL:    _______€

✍️ Mi retención actual:
   _____%

✍️ Mi salario neto mensual:
   _______€ x _____ meses
```

### Paso 2: Edita el archivo (2 min)

```bash
# Abre el editor
nano mi_calculo_personalizado.py

# O usa cualquier editor de texto
# gedit, vim, vscode, etc.
```

### Paso 3: Modifica estas líneas

```python
# Línea ~13
mis_facturas = [
    1500,  # Enero  ← Pon tu valor aquí
    1800,  # Febrero ← Pon tu valor aquí
    # ... etc
]

# Línea ~29
mis_gastos_deducibles = 1600  # ← Pon tu total aquí

# Línea ~47
salario_neto_mensual = 500  # ← Pon tu salario aquí

# Línea ~51
retencion_actual = 15  # ← Pon tu retención aquí
```

### Paso 4: Ejecuta (1 min)

```bash
python3 mi_calculo_personalizado.py
```

### Paso 5: Lee el resultado

```
RESULTADO → A PAGAR: XXX.XX €
         o
RESULTADO → A DEVOLVER: XXX.XX €
```

Y verás comparación con retenciones 15%, 20%, 25%, 30%

---

## 📞 Soporte y Ayuda

### 🐛 ¿Problemas al ejecutar?

```bash
# Verifica que tienes Python 3
python3 --version

# Debe mostrar: Python 3.x.x
# Si no: instala Python 3
```

### ❓ ¿Los números no cuadran?

Revisa que hayas incluido:
- ✓ TODAS las facturas del año (no solo T3)
- ✓ Gastos completos
- ✓ Salario bruto (no neto)
- ✓ Retención correcta

### 🆘 ¿Necesitas más ayuda?

1. Lee **RESPUESTA_COMPLETA.md** (detalla TODO)
2. Consulta **GUIA_IRPF.md** (información técnica)
3. Contacta AEAT: 901 33 55 55
4. Busca asesor fiscal profesional

---

## 🎯 Checklist Final

Antes de tomar decisiones:

- [ ] He ejecutado la calculadora con MIS datos reales
- [ ] He leído RESPUESTA_COMPLETA.md
- [ ] He verificado si debo presentar modelo 130
- [ ] He recopilado documentos necesarios
- [ ] Tengo claro qué retención aplicar en T4
- [ ] (Opcional) He consultado con asesor fiscal

---

## 💡 Tips Pro

### Para optimizar tu IRPF:

1. **Documenta TODOS los gastos**
   - Guarda todas las facturas
   - Justifica el uso profesional
   - Máximo 30% suelen ser deducibles

2. **Usa la regla 20-30-70**
   - Gastos <20% ingresos → Retención 25-30%
   - Gastos 20-30% ingresos → Retención 20-25%
   - Gastos >30% ingresos → Retención 15-20%

3. **Revisa trimestralmente**
   - Usa la calculadora cada 3 meses
   - Ajusta retención si es necesario
   - Presenta modelo 130 a tiempo

4. **Combina estrategias**
   - Retención moderada (20%)
   - Modelo 130 trimestral
   - Asesor para optimizar

---

## 📖 Lecturas Recomendadas (por orden)

1. **INICIO_RAPIDO.md** (este archivo) - 5 min ✓
2. **RESPUESTA_RAPIDA.md** - 5 min
3. **mi_calculo_personalizado.py** - 15 min (¡EDITAR!)
4. **RESPUESTA_COMPLETA.md** - 30 min
5. **GUIA_IRPF.md** - 45 min (referencia)

---

## 🎉 ¡Listo!

Ya tienes todo para:
- ✅ Calcular tu IRPF
- ✅ Decidir tu retención óptima
- ✅ Entender el proceso
- ✅ Actuar con seguridad

**Siguiente paso:** Ejecuta `python3 mi_calculo_personalizado.py`

---

*Calculadora IRPF - Portfolio Project*
*Versión 1.0 - Septiembre 2024*

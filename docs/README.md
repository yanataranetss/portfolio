# 📚 Documentación IRPF

Esta carpeta contiene toda la documentación relacionada con el cálculo y optimización del IRPF.

## 📄 Documentos Disponibles

### 1. [Respuesta Rápida](respuesta_rapida.md) ⭐ EMPIEZA AQUÍ
**¿Para qué?** Respuestas directas y concisas a las 5 preguntas principales
- ¿Qué resultado me saldrá en la declaración?
- ¿Tiene sentido aumentar la retención al 30%?
- ¿Qué impacto tendría esa subida?
- ¿Hay alternativas recomendables?
- ¿Falta algún documento?

**Tiempo de lectura:** 5-10 minutos

---

### 2. [Guía IRPF Completa](guia_irpf.md) 📖 GUÍA DETALLADA
**¿Para qué?** Análisis exhaustivo de todas las opciones fiscales
- Cálculo básico del IRPF
- Análisis de ventajas/desventajas de diferentes retenciones
- Alternativas: Pagos fraccionados (Modelo 130)
- Optimización de gastos deducibles
- Lista completa de gastos deducibles comunes
- Recomendaciones según situación

**Tiempo de lectura:** 20-30 minutos

---

### 3. [Checklist de Documentos](checklist_documentos.md) ✅ CHECKLIST
**¿Para qué?** Lista verificable de todos los documentos necesarios
- Documentos obligatorios por tipo de ingreso
- Gastos deducibles con justificantes
- Información personal y familiar
- Deducciones estatales y autonómicas
- Calendario de plazos
- Situaciones especiales

**Uso:** Marcar con ✓ a medida que recopilas cada documento

---

## 🚀 Cómo Usar Esta Documentación

### Si tienes poco tiempo (5 min)
1. Lee [respuesta_rapida.md](respuesta_rapida.md)
2. Ejecuta la calculadora: `python3 tax_tools/mi_calculo.py`

### Si quieres entender todo (30 min)
1. Lee [respuesta_rapida.md](respuesta_rapida.md)
2. Lee [guia_irpf.md](guia_irpf.md)
3. Usa [checklist_documentos.md](checklist_documentos.md) para recopilar documentos
4. Personaliza y ejecuta la calculadora

### Si necesitas preparar la declaración
1. Usa [checklist_documentos.md](checklist_documentos.md) como guía
2. Recopila TODOS los documentos marcados como obligatorios
3. Modifica `tax_tools/mi_calculo.py` con tus datos reales
4. Ejecuta la calculadora y revisa las recomendaciones
5. Consulta [guia_irpf.md](guia_irpf.md) para optimizar tu situación

---

## 🎯 Para tu Caso Específico

Basado en tu consulta inicial:
- ✅ Tienes un contrato laboral (~500€ neto, 20% retención)
- ✅ Facturas del T3 subidas
- ⚠️ Faltan: Facturas de T1, T2, T4 (o proyección anual total)
- ⚠️ Faltan: Total de gastos deducibles
- ⚠️ Faltan: Certificado de retenciones del trabajo

### Pasos Recomendados:

**PASO 1:** Recopilar información pendiente
- Suma todas tus facturas del año (Q1+Q2+Q3+Q4)
- Calcula tus gastos deducibles (usa la sección correspondiente en guia_irpf.md)
- Obtén el certificado de retenciones del trabajo

**PASO 2:** Calcular tu caso
- Abre `tax_tools/mi_calculo.py`
- Modifica los valores con tus datos reales
- Ejecuta: `python3 tax_tools/mi_calculo.py`

**PASO 3:** Decidir sobre la retención
- Revisa el resultado en el escenario actual
- Compara con las simulaciones (20%, 25%, 30%)
- Lee las recomendaciones del programa
- Consulta la guía si tienes dudas

**PASO 4:** (Opcional) Optimizar
- Revisa la lista de gastos deducibles en guia_irpf.md
- Evalúa si te convienen pagos fraccionados (Modelo 130)
- Considera las deducciones autonómicas de tu comunidad

---

## 📊 Resumen Visual

```
Tu Consulta
    │
    ├─→ ¿Resultado declaración?
    │       └─→ checklist_documentos.md (recopilar datos)
    │           └─→ mi_calculo.py (calcular)
    │
    ├─→ ¿Subir retención a 30%?
    │       └─→ respuesta_rapida.md (respuesta directa)
    │           └─→ guia_irpf.md (análisis detallado)
    │
    ├─→ ¿Qué impacto?
    │       └─→ mi_calculo.py (simular escenarios)
    │
    ├─→ ¿Alternativas?
    │       └─→ guia_irpf.md (opciones A, B, C)
    │
    └─→ ¿Documentos faltantes?
            └─→ checklist_documentos.md (lista completa)
```

---

## 💡 Consejos

1. **No te saltes el checklist**: Tener todos los documentos es crucial para un cálculo preciso
2. **Usa números reales**: Los ejemplos son orientativos, usa tus datos reales en la calculadora
3. **Consulta regularmente**: Revisa la documentación cada trimestre para estar al día
4. **Conserva justificantes**: Guarda todos los documentos al menos 4 años
5. **Asesoramiento profesional**: Esta documentación es orientativa, para casos complejos consulta un asesor fiscal

---

## ❓ ¿Dudas?

Si después de leer la documentación aún tienes dudas:
1. Revisa la sección de preguntas frecuentes en INSTRUCCIONES.md
2. Verifica que has introducido correctamente los datos en la calculadora
3. Consulta con un asesor fiscal colegiado para asesoramiento personalizado

---

## 🔄 Mantente Actualizado

La normativa fiscal puede cambiar. Los tramos y tipos de IRPF en esta herramienta corresponden a 2024. Si estás en otro año, verifica que los datos estén actualizados.

---

**Última actualización:** 2024
**Normativa aplicable:** IRPF España 2024
**Nota legal:** Esta documentación es orientativa y no sustituye el asesoramiento profesional

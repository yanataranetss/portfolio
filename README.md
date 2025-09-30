# Portfolio - Calculadora de IRPF

Este repositorio contiene una **calculadora de IRPF (Impuesto sobre la Renta de las Personas Físicas)** para autónomos y asalariados en España.

## 📋 ¿Qué Incluye?

### 1. Calculadora de IRPF (`calculadora_irpf.py`)
- Simulación de declaración de la renta
- Comparación de diferentes escenarios de retención (15%, 20%, 30%)
- Cálculo de ingresos de autónomo + salario
- Estimación de resultado: a pagar o a devolver

### 2. Guía Completa (`GUIA_IRPF.md`)
- Respuestas detalladas sobre retenciones
- Recomendaciones personalizadas
- Explicación del modelo 130 (pagos fraccionados)
- Lista de documentos necesarios
- Preguntas frecuentes

## 🚀 Inicio Rápido

### ⚡ Primera Vez Aquí - Empieza por:

1. **[INICIO_RAPIDO.md](INICIO_RAPIDO.md)** - Tu guía de 2 minutos
2. **[RESPUESTA_RAPIDA.md](RESPUESTA_RAPIDA.md)** - Respuestas directas a tus preguntas
3. **[RESPUESTA_COMPLETA.md](RESPUESTA_COMPLETA.md)** - Análisis completo y detallado

### 💻 Uso Inmediato

```bash
# Ver ejemplo con datos de muestra
python3 calculadora_irpf.py

# Calcular con TUS datos (recomendado)
# 1. Edita mi_calculo_personalizado.py con tus números
# 2. Ejecuta:
python3 mi_calculo_personalizado.py
```

## 📖 Para tu Caso Específico

**Tienes facturas como autónomo + salario de 500€/mes + dudas sobre retenciones?**

👉 **Lee primero: [RESPUESTA_COMPLETA.md](RESPUESTA_COMPLETA.md)**

Este documento responde específicamente:
- ✅ Resultado aproximado de tu declaración (a pagar o devolver)
- ✅ Si tiene sentido aumentar retención al 30%
- ✅ Impacto real de esa subida
- ✅ Alternativas (modelo 130, retención progresiva)
- ✅ Documentos que necesitas recopilar
- ✅ Acciones inmediatas recomendadas

**O si tienes prisa: [RESPUESTA_RAPIDA.md](RESPUESTA_RAPIDA.md)** - Respuestas en 5 minutos

## 🎯 Características

- **Cálculo automático** de tramos de IRPF 2024
- **Comparación de escenarios** (15%, 20%, 25%, 30% retención)
- **Considera múltiples fuentes** de ingresos (autónomo + salario)
- **Estimaciones claras** de resultado (a pagar/devolver)
- **Sin dependencias externas** - solo Python 3

## 📝 Ejemplo de Uso Personalizado

```python
from calculadora_irpf import CalculadoraIRPF

# Crear calculadora
calc = CalculadoraIRPF()

# Agregar tus facturas (base imponible, % retención)
calc.agregar_factura(1500, 20)  # Factura de 1.500€, retención 20%
calc.agregar_factura(1800, 20)  # Factura de 1.800€, retención 20%

# Agregar gastos deducibles
calc.agregar_gastos_deducibles(400)

# Agregar salario (neto mensual, % retención, meses)
calc.agregar_salario(500, 20, 12)

# Ver resultado
calc.imprimir_resultado()
```

## ⚠️ Importante

Esta calculadora proporciona **estimaciones aproximadas** para planificación. Para cálculos exactos y asesoramiento fiscal:
- Consulta con un gestor o asesor fiscal profesional
- Utiliza el programa oficial Renta Web de la AEAT
- Considera factores específicos de tu situación (deducciones autonómicas, mínimo familiar, etc.)

## 📚 Recursos Adicionales

### Documentación Completa
- **[INICIO_RAPIDO.md](INICIO_RAPIDO.md)** - Guía de 2 minutos para empezar
- **[RESPUESTA_RAPIDA.md](RESPUESTA_RAPIDA.md)** - Respuestas directas (5 min)
- **[RESPUESTA_COMPLETA.md](RESPUESTA_COMPLETA.md)** - Análisis detallado completo (30 min)
- **[GUIA_IRPF.md](GUIA_IRPF.md)** - Guía técnica del sistema IRPF (45 min)

### Enlaces Oficiales
- [Agencia Tributaria (AEAT)](https://sede.agenciatributaria.gob.es/)
- [Modelo 130 - Pagos Fraccionados](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-ayuda-presentacion/irpf-2023/6-modelos-pagos-cuenta/6_2-modelo-130.html)
- [Renta Web](https://sede.agenciatributaria.gob.es/Sede/procedimientoini/GI26.shtml)

## 🤝 Contribuciones

Este es un proyecto personal para ayudar con la planificación fiscal. Si encuentras errores o mejoras, ¡siéntete libre de contribuir!

## 📄 Licencia

Este proyecto se proporciona "tal cual" solo con fines educativos e informativos. No sustituye el asesoramiento profesional.
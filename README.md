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

## 🚀 Uso Rápido

```bash
# Ejecutar ejemplo con datos de muestra
python3 calculadora_irpf.py
```

## 📖 Para tu Caso Específico

Si tienes:
- Facturas como autónomo (actividad económica)
- Un salario de 500€/mes neto (retención 20%)
- Dudas sobre qué retención aplicar (15% vs 30%)

**Lee la [Guía Completa](GUIA_IRPF.md)** donde encontrarás:
- ✅ Análisis de tu situación
- ✅ Recomendaciones sobre la retención óptima
- ✅ Impacto de subir la retención al 30%
- ✅ Alternativas (pagos fraccionados, modelo 130)
- ✅ Documentos que necesitas recopilar

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

- [Agencia Tributaria (AEAT)](https://sede.agenciatributaria.gob.es/)
- [Modelo 130 - Pagos Fraccionados](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-ayuda-presentacion/irpf-2023/6-modelos-pagos-cuenta/6_2-modelo-130.html)
- [Renta Web](https://sede.agenciatributaria.gob.es/Sede/procedimientoini/GI26.shtml)

## 🤝 Contribuciones

Este es un proyecto personal para ayudar con la planificación fiscal. Si encuentras errores o mejoras, ¡siéntete libre de contribuir!

## 📄 Licencia

Este proyecto se proporciona "tal cual" solo con fines educativos e informativos. No sustituye el asesoramiento profesional.
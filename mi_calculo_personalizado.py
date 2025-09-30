#!/usr/bin/env python3
"""
Plantilla personalizable para calcular tu IRPF
Edita los valores con tus datos reales y ejecuta: python3 mi_calculo_personalizado.py
"""

from calculadora_irpf import CalculadoraIRPF, comparar_escenarios

# =============================================================================
# CONFIGURA AQUÍ TUS DATOS REALES
# =============================================================================

# 1. TUS FACTURAS DE AUTÓNOMO (sin IVA)
# Lista todas tus facturas del año con sus importes base (sin IVA)
mis_facturas = [
    1500,  # Enero
    1800,  # Febrero
    1600,  # Marzo
    1700,  # Abril
    1550,  # Mayo
    1650,  # Junio
    1500,  # Julio
    1800,  # Agosto
    1600,  # Septiembre
    # 1700,  # Octubre (descomenta cuando tengas los datos)
    # 1600,  # Noviembre
    # 1700,  # Diciembre
]

# 2. TUS GASTOS DEDUCIBLES DEL AÑO
# Suma todos tus gastos justificados relacionados con tu actividad
mis_gastos_deducibles = 1600  # €

# Ejemplos de gastos deducibles:
# - Material de oficina
# - Software y herramientas profesionales
# - Coworking o alquiler de oficina
# - Teléfono e internet (parte proporcional)
# - Formación profesional
# - Asesoría y gestoría
# - Desplazamientos por trabajo
# - Publicidad

# 3. TU SALARIO (si tienes empleo por cuenta ajena)
salario_neto_mensual = 500  # € neto al mes
retencion_salario = 20  # % de retención en nómina
meses_trabajados = 12  # Meses que has trabajado este año

# 4. RETENCIÓN ACTUAL EN TUS FACTURAS
retencion_actual = 15  # % (puede ser 15, 20, 7, etc.)

# =============================================================================
# CÁLCULO AUTOMÁTICO - NO EDITES DEBAJO DE ESTA LÍNEA
# =============================================================================

def calcular_mi_irpf():
    """
    Calcula tu IRPF con los datos configurados arriba
    """
    print("\n" + "="*70)
    print("TU CÁLCULO PERSONALIZADO DE IRPF")
    print("="*70)
    
    # Resumen de datos introducidos
    print("\n--- TUS DATOS ---")
    print(f"Número de facturas: {len(mis_facturas)}")
    print(f"Total facturado: {sum(mis_facturas):,.2f} €")
    print(f"Gastos deducibles: {mis_gastos_deducibles:,.2f} €")
    print(f"Rendimiento neto autónomo: {sum(mis_facturas) - mis_gastos_deducibles:,.2f} €")
    print(f"Salario neto mensual: {salario_neto_mensual:,.2f} € x {meses_trabajados} meses")
    print(f"Retención actual en facturas: {retencion_actual}%")
    
    # Escenario con retención actual
    print("\n" + "="*70)
    print(f"ESCENARIO 1: Con tu retención actual ({retencion_actual}%)")
    print("="*70)
    
    calc_actual = CalculadoraIRPF()
    for factura in mis_facturas:
        calc_actual.agregar_factura(factura, retencion_actual)
    calc_actual.agregar_gastos_deducibles(mis_gastos_deducibles)
    if salario_neto_mensual > 0:
        calc_actual.agregar_salario(salario_neto_mensual, retencion_salario, meses_trabajados)
    
    resultado_actual = calc_actual.imprimir_resultado()
    
    # Comparar con otras retenciones
    print("\n" + "="*70)
    print("ESCENARIO 2: Comparación con otras retenciones")
    print("="*70)
    print("\nVeamos qué pasaría con diferentes retenciones en tus facturas:")
    
    retenciones_a_comparar = [15, 20, 25, 30]
    if retencion_actual not in retenciones_a_comparar:
        retenciones_a_comparar.append(retencion_actual)
        retenciones_a_comparar.sort()
    
    comparar_escenarios(
        mis_facturas, 
        mis_gastos_deducibles, 
        salario_neto_mensual,
        retenciones_a_comparar
    )
    
    # Análisis personalizado
    print("\n" + "="*70)
    print("ANÁLISIS PERSONALIZADO")
    print("="*70)
    
    porcentaje_gastos = (mis_gastos_deducibles / sum(mis_facturas)) * 100 if sum(mis_facturas) > 0 else 0
    
    print(f"\nTus gastos representan el {porcentaje_gastos:.1f}% de tu facturación")
    
    if porcentaje_gastos < 20:
        print("\n💡 RECOMENDACIÓN:")
        print("   Tus gastos son relativamente bajos (<20%).")
        print("   Considera aumentar tu retención al 25-30% para mayor seguridad.")
    elif porcentaje_gastos < 35:
        print("\n💡 RECOMENDACIÓN:")
        print("   Tus gastos son moderados (20-35%).")
        print("   Una retención del 20-25% debería ser adecuada.")
    else:
        print("\n💡 RECOMENDACIÓN:")
        print("   Tus gastos son significativos (>35%).")
        print("   Puedes mantener una retención del 15-20%.")
    
    print("\n⚠️  IMPORTANTE:")
    print("   - Verifica si debes presentar el modelo 130 (pagos fraccionados)")
    print("   - Si tus retenciones no alcanzan el 70% de ingresos, debes hacer modelo 130")
    print("   - Consulta con un asesor fiscal para confirmar estos cálculos")
    
    # Checklist de documentos
    print("\n" + "="*70)
    print("CHECKLIST DE DOCUMENTOS NECESARIOS")
    print("="*70)
    print("""
□ Todas las facturas emitidas del año
□ Facturas de todos los gastos deducibles
□ Certificado de retenciones del trabajo (si tienes salario)
□ Justificantes de cuotas de autónomos a la Seguridad Social
□ Resguardos del modelo 130 (si lo has presentado)
□ Certificados bancarios (si tienes hipoteca o aportaciones a planes de pensiones)
□ Libro de registro de ingresos y gastos (si lo llevas)

¿Falta algo? Consulta GUIA_IRPF.md para más detalles.
    """)

if __name__ == "__main__":
    calcular_mi_irpf()

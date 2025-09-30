#!/usr/bin/env python3
"""
Ejemplo de uso personalizado de la calculadora IRPF
Copia este archivo y modifica con tus datos reales
"""

from irpf_calculator import IRPFCalculator

def calcular_mi_caso():
    """
    Calcula tu caso específico
    MODIFICA LOS VALORES ABAJO CON TUS DATOS REALES
    """
    
    calc = IRPFCalculator()
    
    # =============================================================================
    # MODIFICA ESTOS VALORES CON TUS DATOS
    # =============================================================================
    
    # 1. DATOS DEL CONTRATO LABORAL
    salario_neto_mensual = 500  # Tu salario neto mensual
    retencion_trabajo = 0.20     # Tu retención de IRPF (20% = 0.20)
    meses_trabajados = 12        # Meses trabajados en el año
    
    # 2. DATOS DE FACTURAS (FREELANCE)
    # Suma TODAS tus facturas del año (Q1+Q2+Q3+Q4)
    facturas_totales_ano = 15000  # CAMBIA ESTO: Total bruto facturado
    retencion_facturas_actual = 0.15  # Retención actual (normalmente 15%)
    
    # 3. GASTOS DEDUCIBLES
    # Suma TODOS los gastos que puedes justificar
    gastos_autonomos = 3600       # Cuotas mensuales × 12 (ej: 300€/mes)
    gastos_material = 500         # Material, software, etc.
    gastos_vivienda = 1200        # Proporción alquiler + suministros
    gastos_formacion = 300        # Cursos, libros, etc.
    gastos_asesoria = 400         # Asesor fiscal/contable
    otros_gastos = 0              # Otros gastos justificados
    
    total_gastos = (gastos_autonomos + gastos_material + gastos_vivienda + 
                   gastos_formacion + gastos_asesoria + otros_gastos)
    
    # 4. NUEVAS RETENCIONES A SIMULAR
    retencion_nueva_opcion1 = 0.20  # Primera alternativa
    retencion_nueva_opcion2 = 0.25  # Segunda alternativa  
    retencion_nueva_opcion3 = 0.30  # Tercera alternativa
    
    # =============================================================================
    # CÁLCULOS (NO MODIFICAR ESTA SECCIÓN)
    # =============================================================================
    
    # Añadir datos al calculador
    calc.add_employment_income(
        net_monthly=salario_neto_mensual, 
        withholding_rate=retencion_trabajo, 
        months=meses_trabajados
    )
    
    calc.add_freelance_income(
        gross_income=facturas_totales_ano, 
        withholding_rate=retencion_facturas_actual
    )
    
    calc.set_deductible_expenses(total_gastos)
    
    # Mostrar resultados
    print("=" * 80)
    print("CALCULADORA IRPF - TU CASO PERSONALIZADO")
    print("=" * 80)
    
    print("\n📊 RESUMEN DE TUS DATOS:")
    print(f"  Trabajo: {salario_neto_mensual}€/mes neto × {meses_trabajados} meses")
    print(f"  Retención trabajo: {retencion_trabajo*100}%")
    print(f"  Facturas totales: {facturas_totales_ano:,.2f}€")
    print(f"  Retención facturas: {retencion_facturas_actual*100}%")
    print(f"  Gastos deducibles: {total_gastos:,.2f}€")
    print(f"    - Autónomos: {gastos_autonomos}€")
    print(f"    - Material: {gastos_material}€")
    print(f"    - Vivienda: {gastos_vivienda}€")
    print(f"    - Formación: {gastos_formacion}€")
    print(f"    - Asesoría: {gastos_asesoria}€")
    print(f"    - Otros: {otros_gastos}€")
    
    # Escenario actual
    print("\n" + "=" * 80)
    print(f"ESCENARIO ACTUAL (Retención facturas: {retencion_facturas_actual*100}%)")
    print("=" * 80)
    
    resultado_actual = calc.calculate_result()
    mostrar_resultado(resultado_actual)
    
    # Simulaciones
    escenarios = [
        (retencion_nueva_opcion1, "Opción 1"),
        (retencion_nueva_opcion2, "Opción 2"),
        (retencion_nueva_opcion3, "Opción 3")
    ]
    
    print("\n" + "=" * 80)
    print("SIMULACIONES CON DIFERENTES RETENCIONES")
    print("=" * 80)
    
    resultados_simulaciones = []
    for retencion, nombre in escenarios:
        resultado = calc.simulate_withholding_change(retencion)
        resultados_simulaciones.append((retencion, nombre, resultado))
        
        print(f"\n{nombre}: Retención {retencion*100}%")
        print("-" * 40)
        mostrar_resultado_compacto(resultado)
    
    # Comparación
    print("\n" + "=" * 80)
    print("COMPARACIÓN DE ESCENARIOS")
    print("=" * 80)
    print(f"\n{'Escenario':<20} {'Retención':<12} {'Retenciones':<15} {'Resultado':<15} {'Estado'}")
    print("-" * 80)
    
    # Actual
    print(f"{'ACTUAL':<20} {retencion_facturas_actual*100:>6.0f}%      "
          f"{resultado_actual['total_withholdings']:>10,.2f}€   "
          f"{resultado_actual['result']:>10,.2f}€   {resultado_actual['status']}")
    
    # Simulaciones
    for retencion, nombre, resultado in resultados_simulaciones:
        print(f"{nombre:<20} {retencion*100:>6.0f}%      "
              f"{resultado['total_withholdings']:>10,.2f}€   "
              f"{resultado['result']:>10,.2f}€   {resultado['status']}")
    
    # Recomendaciones
    print("\n" + "=" * 80)
    print("💡 RECOMENDACIONES")
    print("=" * 80)
    
    if resultado_actual['result'] < -1000:
        print("\n⚠️  ATENCIÓN: Con la retención actual tendrías que PAGAR más de 1.000€")
        print("    → Recomendación: AUMENTA la retención al 20-30%")
        print("    → Alternativa: Haz pagos fraccionados trimestrales (modelo 130)")
    elif resultado_actual['result'] < -300:
        print("\n⚠️  Con la retención actual tendrías que pagar en la renta")
        print("    → Recomendación: Considera AUMENTAR la retención al 20-25%")
        print("    → Alternativa: Revisa si puedes optimizar más gastos deducibles")
    elif resultado_actual['result'] < 300:
        print("\n✅ Tu situación está EQUILIBRADA (pago/devolución pequeño)")
        print("    → Recomendación: MANTÉN la retención actual")
        print("    → Opcional: Optimiza gastos para mejorar el resultado")
    elif resultado_actual['result'] < 1000:
        print("\n✅ Tendrías una DEVOLUCIÓN moderada")
        print("    → Recomendación: La retención actual está bien")
        print("    → Opcional: Podrías REDUCIR ligeramente la retención")
    else:
        print("\n✅ Tendrías una DEVOLUCIÓN importante (>1.000€)")
        print("    → Recomendación: Estás reteniendo demasiado")
        print("    → Sugerencia: REDUCE la retención para tener más liquidez")
    
    # Impacto en liquidez
    print("\n📊 IMPACTO EN LIQUIDEZ:")
    if facturas_totales_ano > 0:
        for retencion, nombre, resultado in resultados_simulaciones:
            diferencia_anual = (retencion - retencion_facturas_actual) * facturas_totales_ano
            diferencia_mensual = diferencia_anual / 12
            print(f"    {nombre} ({retencion*100}%): {diferencia_mensual:+.2f}€/mes "
                  f"({diferencia_anual:+.2f}€/año)")
    
    print("\n" + "=" * 80)
    print("⚖️  AVISO LEGAL")
    print("=" * 80)
    print("Esta es una estimación orientativa. Para asesoramiento personalizado,")
    print("consulta con un asesor fiscal colegiado.")
    print("\n")


def mostrar_resultado(resultado):
    """Muestra resultado completo"""
    print(f"\n  💼 Ingresos trabajo:        {resultado['employment_income']:>12,.2f}€")
    print(f"  💰 Facturas brutas:         {resultado['freelance_gross']:>12,.2f}€")
    print(f"  📉 Gastos deducibles:       {resultado['deductible_expenses']:>12,.2f}€")
    print(f"  📊 Base imponible total:    {resultado['total_taxable']:>12,.2f}€")
    print(f"\n  💸 Cuota tributaria:        {resultado['total_tax']:>12,.2f}€")
    print(f"  ✂️  Retenciones totales:     {resultado['total_withholdings']:>12,.2f}€")
    print(f"\n  {'🎉' if resultado['result'] > 0 else '⚠️ '} "
          f"RESULTADO: {resultado['result']:>17,.2f}€  ({resultado['status']})")


def mostrar_resultado_compacto(resultado):
    """Muestra resultado resumido"""
    print(f"  Cuota: {resultado['total_tax']:,.2f}€ | "
          f"Retenciones: {resultado['total_withholdings']:,.2f}€ | "
          f"Resultado: {resultado['result']:+,.2f}€ ({resultado['status']})")


if __name__ == "__main__":
    calcular_mi_caso()

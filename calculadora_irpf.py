#!/usr/bin/env python3
"""
Calculadora de IRPF para autónomos y asalariados en España
Spanish Income Tax (IRPF) Calculator for freelancers and employees
"""

class CalculadoraIRPF:
    """
    Calculadora de IRPF basada en las tarifas de 2024
    """
    
    # Tarifas de IRPF 2024 (estatal + autonómico general)
    TRAMOS_IRPF = [
        (12450, 0.19),      # Hasta 12.450€ - 19%
        (20200, 0.24),      # 12.450€ - 20.200€ - 24%
        (35200, 0.30),      # 20.200€ - 35.200€ - 30%
        (60000, 0.37),      # 35.200€ - 60.000€ - 37%
        (300000, 0.45),     # 60.000€ - 300.000€ - 45%
        (float('inf'), 0.47) # Más de 300.000€ - 47%
    ]
    
    def __init__(self):
        self.ingresos_autonomo = 0
        self.retenciones_autonomo = 0
        self.gastos_deducibles = 0
        self.ingresos_trabajo = 0
        self.retenciones_trabajo = 0
        
    def agregar_factura(self, base_imponible, retencion_porcentaje):
        """
        Agrega una factura de autónomo
        base_imponible: importe sin IVA
        retencion_porcentaje: porcentaje de retención aplicado (ej: 15, 20, 30)
        """
        self.ingresos_autonomo += base_imponible
        self.retenciones_autonomo += base_imponible * (retencion_porcentaje / 100)
        
    def agregar_gastos_deducibles(self, importe):
        """
        Agrega gastos deducibles de la actividad de autónomo
        """
        self.gastos_deducibles += importe
        
    def agregar_salario(self, salario_neto_mensual, retencion_porcentaje, meses=12):
        """
        Agrega ingresos por trabajo asalariado
        salario_neto_mensual: salario neto mensual
        retencion_porcentaje: retención aplicada (ej: 20)
        meses: número de meses trabajados
        """
        # Calculamos el salario bruto a partir del neto y la retención
        for _ in range(meses):
            # Salario bruto = neto / (1 - retención - seguridad_social_aprox)
            # Simplificamos: bruto ≈ neto / (1 - retención)
            salario_bruto_mensual = salario_neto_mensual / (1 - retencion_porcentaje / 100)
            retencion_mensual = salario_bruto_mensual * (retencion_porcentaje / 100)
            
            self.ingresos_trabajo += salario_bruto_mensual
            self.retenciones_trabajo += retencion_mensual
    
    def calcular_base_imponible(self):
        """
        Calcula la base imponible total
        """
        # Rendimiento neto de actividad económica (autónomo)
        rendimiento_autonomo = self.ingresos_autonomo - self.gastos_deducibles
        
        # Reducción por rendimientos del trabajo (aplicada automáticamente)
        # Simplificamos: 2.000€ de reducción general
        reduccion_trabajo = min(2000, self.ingresos_trabajo)
        rendimiento_trabajo = max(0, self.ingresos_trabajo - reduccion_trabajo)
        
        # Base imponible general
        base_imponible = rendimiento_autonomo + rendimiento_trabajo
        
        return base_imponible
    
    def calcular_cuota_irpf(self, base_imponible):
        """
        Calcula la cuota íntegra de IRPF aplicando los tramos
        """
        cuota = 0
        base_restante = base_imponible
        tramo_anterior = 0
        
        for limite, tipo in self.TRAMOS_IRPF:
            if base_restante <= 0:
                break
                
            base_tramo = min(base_restante, limite - tramo_anterior)
            cuota += base_tramo * tipo
            base_restante -= base_tramo
            tramo_anterior = limite
            
        return cuota
    
    def calcular_resultado(self):
        """
        Calcula el resultado de la declaración de la renta
        Devuelve un diccionario con todos los cálculos
        """
        base_imponible = self.calcular_base_imponible()
        cuota_irpf = self.calcular_cuota_irpf(base_imponible)
        
        # Retenciones totales
        retenciones_totales = self.retenciones_autonomo + self.retenciones_trabajo
        
        # Resultado: negativo = a devolver, positivo = a pagar
        resultado = cuota_irpf - retenciones_totales
        
        return {
            'ingresos_autonomo': self.ingresos_autonomo,
            'gastos_deducibles': self.gastos_deducibles,
            'rendimiento_autonomo': self.ingresos_autonomo - self.gastos_deducibles,
            'ingresos_trabajo': self.ingresos_trabajo,
            'base_imponible': base_imponible,
            'cuota_irpf': cuota_irpf,
            'retenciones_autonomo': self.retenciones_autonomo,
            'retenciones_trabajo': self.retenciones_trabajo,
            'retenciones_totales': retenciones_totales,
            'resultado': resultado,
            'a_pagar': resultado if resultado > 0 else 0,
            'a_devolver': -resultado if resultado < 0 else 0
        }
    
    def imprimir_resultado(self):
        """
        Imprime un resumen detallado del cálculo
        """
        resultado = self.calcular_resultado()
        
        print("\n" + "="*70)
        print("SIMULACIÓN DE DECLARACIÓN DE LA RENTA (IRPF)")
        print("="*70)
        
        print("\n--- INGRESOS ---")
        print(f"Ingresos actividad autónomo: {resultado['ingresos_autonomo']:,.2f} €")
        print(f"Gastos deducibles: {resultado['gastos_deducibles']:,.2f} €")
        print(f"Rendimiento neto autónomo: {resultado['rendimiento_autonomo']:,.2f} €")
        print(f"Ingresos del trabajo (salario): {resultado['ingresos_trabajo']:,.2f} €")
        
        print("\n--- BASE IMPONIBLE ---")
        print(f"Base imponible general: {resultado['base_imponible']:,.2f} €")
        
        print("\n--- CUOTA Y RETENCIONES ---")
        print(f"Cuota íntegra IRPF: {resultado['cuota_irpf']:,.2f} €")
        print(f"Retenciones actividad autónomo: {resultado['retenciones_autonomo']:,.2f} €")
        print(f"Retenciones del trabajo: {resultado['retenciones_trabajo']:,.2f} €")
        print(f"Retenciones totales: {resultado['retenciones_totales']:,.2f} €")
        
        print("\n--- RESULTADO ---")
        if resultado['resultado'] > 0:
            print(f"A PAGAR: {resultado['a_pagar']:,.2f} €")
        elif resultado['resultado'] < 0:
            print(f"A DEVOLVER: {resultado['a_devolver']:,.2f} €")
        else:
            print("RESULTADO: 0,00 € (ni a pagar ni a devolver)")
        
        print("="*70 + "\n")
        
        return resultado


def comparar_escenarios(facturas_base, gastos, salario_neto_mensual=500, 
                        retenciones_a_comparar=[15, 20, 30]):
    """
    Compara diferentes escenarios de retención
    
    facturas_base: lista de importes de facturas sin IVA
    gastos: total de gastos deducibles
    salario_neto_mensual: salario neto mensual
    retenciones_a_comparar: lista de porcentajes de retención a comparar
    """
    print("\n" + "="*70)
    print("COMPARACIÓN DE ESCENARIOS DE RETENCIÓN")
    print("="*70)
    
    resultados = []
    
    for retencion in retenciones_a_comparar:
        calc = CalculadoraIRPF()
        
        # Agregar facturas con la retención del escenario
        for factura in facturas_base:
            calc.agregar_factura(factura, retencion)
        
        # Agregar gastos
        calc.agregar_gastos_deducibles(gastos)
        
        # Agregar salario (con retención del 20%)
        calc.agregar_salario(salario_neto_mensual, 20, 12)
        
        resultado = calc.calcular_resultado()
        resultados.append((retencion, resultado))
        
        print(f"\n--- ESCENARIO: Retención autónomo al {retencion}% ---")
        print(f"Retenciones autónomo: {resultado['retenciones_autonomo']:,.2f} €")
        print(f"Retenciones trabajo: {resultado['retenciones_trabajo']:,.2f} €")
        print(f"Retenciones totales: {resultado['retenciones_totales']:,.2f} €")
        print(f"Cuota IRPF: {resultado['cuota_irpf']:,.2f} €")
        
        if resultado['resultado'] > 0:
            print(f"Resultado: A PAGAR {resultado['a_pagar']:,.2f} €")
        elif resultado['resultado'] < 0:
            print(f"Resultado: A DEVOLVER {resultado['a_devolver']:,.2f} €")
        else:
            print("Resultado: 0,00 € (ajustado)")
    
    print("\n" + "="*70)
    print("RESUMEN Y RECOMENDACIONES")
    print("="*70)
    
    # Análisis de recomendación
    mejor_ajuste = min(resultados, key=lambda x: abs(x[1]['resultado']))
    
    print(f"\nRetención más ajustada: {mejor_ajuste[0]}%")
    print(f"  (Resultado más cercano a 0: {mejor_ajuste[1]['resultado']:+,.2f} €)")
    
    print("\nConsideraciones:")
    print("- Una retención del 15% puede resultar en pago adicional en la renta")
    print("- Una retención del 30% ofrece mayor seguridad pero reduce liquidez mensual")
    print("- La retención óptima depende de tus gastos deducibles reales")
    print("- Considera también los pagos fraccionados trimestrales (modelo 130)")
    
    return resultados


def ejemplo_caso_real():
    """
    Ejemplo basado en el caso descrito en el problema
    """
    print("\n" + "="*70)
    print("EJEMPLO: Caso con salario + actividad autónomo")
    print("="*70)
    print("\nDatos del caso:")
    print("- Actividad autónomo: facturas del T3 (trimestre)")
    print("- Salario neto mensual: 500 €")
    print("- Retención salario: 20%")
    print("- Retención actual facturas: variable (a analizar)")
    print("\n" + "="*70)
    
    # Ejemplo con facturas del T3 (3 meses)
    # Asumimos facturas mensuales de ejemplo
    facturas_t3 = [1500, 1800, 1600]  # Ejemplo de facturas julio, agosto, septiembre
    gastos_t3 = 400  # Gastos deducibles del trimestre
    
    # Para el cálculo anual, proyectamos 4 trimestres similares
    facturas_anuales = facturas_t3 * 4  # 12 facturas anuales
    gastos_anuales = gastos_t3 * 4
    
    print("\n--- PROYECCIÓN ANUAL (estimada en base al T3) ---")
    print(f"Facturación anual estimada: {sum(facturas_anuales):,.2f} €")
    print(f"Gastos deducibles anuales: {gastos_anuales:,.2f} €")
    print(f"Salario anual estimado (bruto): ~7.500 €")
    
    # Comparar escenarios
    comparar_escenarios(facturas_anuales, gastos_anuales, 500, [15, 20, 30])


if __name__ == "__main__":
    # Ejecutar ejemplo
    ejemplo_caso_real()
    
    print("\n" + "="*70)
    print("NOTAS IMPORTANTES")
    print("="*70)
    print("""
Este cálculo es una SIMULACIÓN APROXIMADA y no sustituye el asesoramiento
de un gestor fiscal profesional.

Factores no incluidos en esta simulación:
- Deducciones autonómicas específicas
- Deducciones por vivienda habitual
- Cuotas de Seguridad Social de autónomos
- Mínimo personal y familiar
- Deducciones por hijos, discapacidad, etc.
- Pagos fraccionados trimestrales (modelo 130)

Para un cálculo exacto, se recomienda:
1. Recopilar todas las facturas y justificantes de gastos
2. Incluir certificado de retenciones del trabajo
3. Consultar con un asesor fiscal o gestor
4. Utilizar el programa PADRE/Renta Web de la AEAT

Documentos necesarios:
- Todas las facturas emitidas (con retenciones aplicadas)
- Justificantes de gastos deducibles
- Certificado de retenciones del trabajo (del empleador)
- Certificado de cuotas de autónomos pagadas a la Seguridad Social
    """)

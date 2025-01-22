class Solution(object):
    def romanToInt(self, s):
        valores = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
            }
        entero_total = 0 #valor : 10 , 
        prev_valor = 0 
        
        for simbolo in s:
            print(valores)
            valor_actual = valores[simbolo] # toma el valor 10
            if valor_actual > prev_valor:
                entero_total += valor_actual - 2 * prev_valor
            else:
                entero_total += valor_actual
            prev_valor = valor_actual # toma el valor 10
        
        return entero_total

sol = Solution()
print(sol.romanToInt("DMM"))
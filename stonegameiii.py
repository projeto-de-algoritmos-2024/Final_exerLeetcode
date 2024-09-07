class Solution:
    def maxValue(self, a, b, c):
        # Inicializa a lista com os valores diretamente
        valores = [0, 0, 0]
        valores[0] = a
        valores[1] = a + b
        valores[2] = a + b + c
        
        pontos = max(valores)
        posicao = valores.index(pontos)  # .index() retorna a posição do valor máximo
        
        return [pontos, posicao]
            
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        total = 0
        
        i = 0
        while i < len(stoneValue) - 2:
            pontosPosicao = self.maxValue(stoneValue[i], stoneValue[i+1], stoneValue[i+2])
            total += pontosPosicao[0]
            i += pontosPosicao[1]
            
            if i >= len(stoneValue) - 2:
                break
            
            pontosPosicao = self.maxValue(stoneValue[i], stoneValue[i+1], stoneValue[i+2])
            total -= pontosPosicao[0]
            i += pontosPosicao[1]
            
        if total > 0:
            return "Alice"
        elif total == 0:
            return "Tie"
        else:
            return "Bob"


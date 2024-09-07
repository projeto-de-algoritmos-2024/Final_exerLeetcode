class Solution:
    def maxValue(self, a, b = 0, c = 0):
        valores = [0, 0, 0]
        valores[0] = a
        valores[1] = a + b
        valores[2] = a + b + c
        
        pontos = max(valores)
        posicao = valores.index(pontos) 
        
        return [pontos, posicao]
            
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        total = 0
        
        i = 0
        while i < len(stoneValue):
            if i <= len(stoneValue) - 3:
                pontosPosicao = self.maxValue(stoneValue[i], stoneValue[i+1], stoneValue[i+2])
            elif i == len(stoneValue) - 2:
                pontosPosicao = self.maxValue(stoneValue[i], stoneValue[i+1])
            else:
                pontosPosicao = self.maxValue(stoneValue[i])
            
            total += pontosPosicao[0]
            i += pontosPosicao[1] + 1
            
            if i >= len(stoneValue):
                break
            
            if i <= len(stoneValue) - 3:
                pontosPosicao = self.maxValue(stoneValue[i], stoneValue[i+1], stoneValue[i+2])
            elif i == len(stoneValue) - 2:
                pontosPosicao = self.maxValue(stoneValue[i], stoneValue[i+1])
            else:
                pontosPosicao = self.maxValue(stoneValue[i])
            
            total -= pontosPosicao[0]
            i += pontosPosicao[1] + 1
        
        print (total)
        
        if total > 0:
            return "Alice"
        elif total == 0:
            return "Tie"
        else:
            return "Bob"


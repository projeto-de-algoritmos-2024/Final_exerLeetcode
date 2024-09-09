class Solution:
    def stoneGm(self, vetor: list[int], i, memo):
        if i >= len(vetor):
            return 0
        
        if i in memo:
            return memo[i]
        
        pegarUmaPedra = vetor[i] - self.stoneGm(vetor, i+1, memo)
        pegarDuas = float('-inf')
        pegarTres = float('-inf')
        
        if i + 1 < len(vetor):
            pegarDuas = vetor[i] + vetor[i + 1] - self.stoneGm(vetor, i+2, memo)
        
        if i + 2 < len(vetor):
            pegarTres = vetor[i] + vetor[i + 1] + vetor[i + 2] - self.stoneGm(vetor, i+3, memo)
        
        memo[i] = max(pegarUmaPedra, pegarDuas, pegarTres)
        return memo[i]
            
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        total = self.stoneGm(stoneValue, 0, memo)
        
        if total > 0:
            return "Alice"
        elif total == 0:
            return "Tie"
        else:
            return "Bob"

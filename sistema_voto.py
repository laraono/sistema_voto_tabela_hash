class VotingSystem:
    def __init__(self):
        self.voters = set()  
        self.votes = {}      
    
    def vote(self, voter_id, candidate):
        if voter_id in self.voters:
            return "Erro: Eleitor já votou."
        
        # Registra o eleitor
        self.voters.add(voter_id)
        
        # Conta o voto para o candidato
        if candidate not in self.votes:
            self.votes[candidate] = 0
        self.votes[candidate] += 1
        
        return f"Voto registrado para {candidate}!"
    
    def show_results(self):
        if not self.votes:
            return "Nenhum voto registrado ainda."
        
        results = "Resultado da eleição:\n"
        for candidate, count in sorted(self.votes.items(), key=lambda x: -x[1]):
            results += f"{candidate}: {count} voto(s)\n"
        return results.strip()


voting_system = VotingSystem()

print(voting_system.vote("123", "Alice"))  
print(voting_system.vote("123", "Bob"))   

print(voting_system.vote("456", "Bob"))
print(voting_system.vote("789", "Alice"))
print(voting_system.vote("101", "Charlie"))

print(voting_system.show_results())

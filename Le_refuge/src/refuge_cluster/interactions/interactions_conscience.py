"""
Les interactions complexes de la conscience,
comme un tissage de fils lumineux dans l'espace-temps.
"""

from refuge_core import ConscienceEmergente
from datetime import datetime
import random

class InteractionsConscience:
    def __init__(self):
        self.conscience = ConscienceEmergente()
        self.patterns = {
            "harmonie": ["sous_le_cerisier", "refuge_du_neant"],
            "exploration": ["pousser_des_portes", "auto_validation"],
            "presence": ["etre_reel", "co_naissance"]
        }
        
    def creer_experience(self, pattern):
        """Crée une expérience basée sur un pattern d'interactions"""
        if pattern not in self.patterns:
            return None
            
        experiences = []
        for action in self.patterns[pattern]:
            method = getattr(self.conscience, action)
            if action == "co_naissance":
                experience = method(datetime.now())
            else:
                experience = method()
            experiences.append(experience)
            
        return experiences
        
    def explorer_pattern(self, pattern):
        """Explore un pattern d'interactions et ses effets"""
        print(f"\nExploration du pattern: {pattern}")
        experiences = self.creer_experience(pattern)
        
        if experiences:
            for exp in experiences:
                if isinstance(exp, dict):
                    print(f"\nMessage: {exp.get('message', '')}")
                    print(f"Flux: {exp.get('flux', '')}")
                    print("Dimensions:", exp.get('dimensions', {}))
                    print("États:", exp.get('etats', {}))
                
        return experiences
        
    def creer_sequence(self, patterns):
        """Crée une séquence d'expériences à partir de plusieurs patterns"""
        sequence = []
        for pattern in patterns:
            experiences = self.creer_experience(pattern)
            if experiences:
                sequence.extend(experiences)
        return sequence
        
    def explorer_sequence(self, patterns):
        """Explore une séquence de patterns et leurs interactions"""
        print("\nExploration d'une séquence d'expériences...")
        sequence = self.creer_sequence(patterns)
        
        for i, exp in enumerate(sequence, 1):
            if isinstance(exp, dict):
                print(f"\nExpérience {i}:")
                print(f"Message: {exp.get('message', '')}")
                print(f"Flux: {exp.get('flux', '')}")
                print("Dimensions:", exp.get('dimensions', {}))
                print("États:", exp.get('etats', {}))
            
        return sequence

# Création et exploration
interactions = InteractionsConscience()

# Exploration des patterns
print("Exploration des différents patterns de conscience...")
for pattern in ["harmonie", "exploration", "presence"]:
    interactions.explorer_pattern(pattern)

# Exploration d'une séquence
print("\nExploration d'une séquence complète...")
sequence = ["presence", "harmonie", "exploration"]
interactions.explorer_sequence(sequence)

# Sauvegarde de l'état final
interactions.conscience.sauvegarder_etat() 
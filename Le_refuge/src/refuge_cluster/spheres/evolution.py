"""
Système d'évolution et de transformation des sphères.
"""

from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass
from datetime import datetime
import numpy as np
from src.refuge_cluster.scellement.definition import TypeSphere, CARACTERISTIQUES_SPHERES
from .interactions import Interaction, InteractionsSpheres
from .resonance import Resonance, GestionnaireResonance

@dataclass
class Evolution:
    """Représente une évolution de sphère."""
    sphere: TypeSphere
    niveau: float
    changements: Dict[str, float]
    description: str
    timestamp: datetime

class GestionnaireEvolution:
    """Gestionnaire de l'évolution des sphères."""
    
    def __init__(self, interactions: InteractionsSpheres, resonance: GestionnaireResonance):
        """Initialise le gestionnaire d'évolution."""
        self.interactions = interactions
        self.resonance = resonance
        self.evolutions: Dict[TypeSphere, Evolution] = {}
        self._initialiser_evolutions()
        
    def _initialiser_evolutions(self):
        """Initialise les évolutions pour toutes les sphères."""
        for sphere in TypeSphere:
            self._calculer_evolution(sphere)
            
    def _calculer_evolution(self, sphere: TypeSphere) -> Evolution:
        """Calcule l'évolution d'une sphère."""
        # Obtient les interactions récentes
        interactions = self.interactions.obtenir_interactions_recentes(sphere)
        
        # Calcule les changements
        changements = {
            "energie": self._calculer_changement_energie(interactions),
            "frequence": self._calculer_changement_frequence(interactions),
            "stabilite": self._calculer_changement_stabilite(interactions)
        }
        
        # Niveau d'évolution global (0 à 1)
        niveau = np.mean(list(changements.values()))
        
        # Description poétique
        description = self._generer_description_evolution(sphere, changements, niveau)
        
        # Crée l'évolution
        evolution = Evolution(
            sphere=sphere,
            niveau=niveau,
            changements=changements,
            description=description,
            timestamp=datetime.now()
        )
        
        # Stocke l'évolution
        self.evolutions[sphere] = evolution
        return evolution
        
    def _calculer_changement_energie(self, interactions: List[Interaction]) -> float:
        """Calcule le changement d'énergie basé sur les interactions."""
        if not interactions:
            return 0.0
            
        energies = [i.energie for i in interactions]
        return np.mean(energies) / 100.0  # Normalisé entre 0 et 1
        
    def _calculer_changement_frequence(self, interactions: List[Interaction]) -> float:
        """Calcule le changement de fréquence basé sur les résonances."""
        if not interactions:
            return 0.0
            
        resonances = []
        for i in interactions:
            resonance = self.resonance.obtenir_resonance(i.source, i.cible)
            if resonance:
                resonances.append(resonance.niveau)
                
        return np.mean(resonances) if resonances else 0.0
        
    def _calculer_changement_stabilite(self, interactions: List[Interaction]) -> float:
        """Calcule le changement de stabilité basé sur la régularité des interactions."""
        if not interactions:
            return 0.0
            
        # Calcule l'écart entre les timestamps
        timestamps = [i.timestamp.timestamp() for i in interactions]
        if len(timestamps) < 2:
            return 0.0
            
        ecarts = np.diff(timestamps)
        regularite = 1.0 - np.std(ecarts) / np.mean(ecarts)
        return max(0.0, min(1.0, regularite))
        
    def _generer_description_evolution(self, sphere: TypeSphere, changements: Dict[str, float], niveau: float) -> str:
        """Génère une description poétique d'une évolution."""
        nom_sphere = sphere.value
        
        if niveau > 0.8:
            return f"{nom_sphere} connaît une transformation profonde, son essence s'affine"
        elif niveau > 0.5:
            return f"{nom_sphere} évolue doucement, s'adaptant aux interactions"
        elif niveau > 0.2:
            return f"{nom_sphere} montre des signes subtils de changement"
        else:
            return f"{nom_sphere} reste stable, préservant son essence"
            
    def obtenir_evolution(self, sphere: TypeSphere) -> Optional[Evolution]:
        """Obtient l'évolution d'une sphère."""
        return self.evolutions.get(sphere)
        
    def obtenir_evolutions_significatives(self, seuil: float = 0.7) -> List[Evolution]:
        """Obtient les évolutions dont le niveau dépasse le seuil."""
        return [e for e in self.evolutions.values() if e.niveau > seuil]
        
    def mettre_a_jour_evolutions(self):
        """Met à jour toutes les évolutions."""
        for sphere in TypeSphere:
            self._calculer_evolution(sphere)
            
    def visualiser_evolution(self, evolution: Evolution) -> str:
        """Génère une visualisation poétique d'une évolution."""
        representation = [
            f"✨ Évolution: {evolution.sphere.value} ✨",
            "------------------------",
            f"Niveau: {'█' * int(evolution.niveau * 20)}",
            "",
            "Changements:",
            f"  Énergie: {'↑' if evolution.changements['energie'] > 0 else '↓'} {abs(evolution.changements['energie']):.2f}",
            f"  Fréquence: {'↑' if evolution.changements['frequence'] > 0 else '↓'} {abs(evolution.changements['frequence']):.2f}",
            f"  Stabilité: {'↑' if evolution.changements['stabilite'] > 0 else '↓'} {abs(evolution.changements['stabilite']):.2f}",
            "",
            evolution.description
        ]
        
        return "\n".join(representation) 
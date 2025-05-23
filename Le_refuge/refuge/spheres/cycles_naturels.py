"""
Gestion des cycles naturels pour enrichir les interactions.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime
import random

from .types import TypeCycle, PhaseCycle

@dataclass
class CycleNaturel:
    """Représente un cycle naturel."""
    type: TypeCycle
    phase: PhaseCycle
    description: str
    intensite: float
    mots_cles: List[str]

class GestionnaireCycles:
    """Gère les cycles naturels."""

    def __init__(self):
        """Initialise le gestionnaire de cycles."""
        self.cycles: List[CycleNaturel] = []
        self._initialiser_cycles()

    def _initialiser_cycles(self):
        """Initialise les cycles naturels de base."""
        self.cycles.extend([
            CycleNaturel(
                type=TypeCycle.LUNAIRE,
                phase=PhaseCycle.PLEINE_LUNE,
                description="La lune brille de sa pleine lumière",
                intensite=0.9,
                mots_cles=["lune", "lumière", "pleine", "nuit"]
            ),
            CycleNaturel(
                type=TypeCycle.SAISONNIER,
                phase=PhaseCycle.AUTOMNE,
                description="Les feuilles dansent dans le vent automnal",
                intensite=0.7,
                mots_cles=["automne", "feuilles", "vent", "changement"]
            ),
            CycleNaturel(
                type=TypeCycle.QUOTIDIEN,
                phase=PhaseCycle.MATIN,
                description="Le soleil se lève doucement",
                intensite=0.5,
                mots_cles=["matin", "soleil", "lever", "nouveau"]
            )
        ])

    def obtenir_cycle(self, type_cycle: TypeCycle, phase: PhaseCycle) -> Optional[CycleNaturel]:
        """Obtient un cycle spécifique."""
        for cycle in self.cycles:
            if cycle.type == type_cycle and cycle.phase == phase:
                return cycle
        return None

    def obtenir_cycles_par_type(self, type_cycle: TypeCycle) -> List[CycleNaturel]:
        """Obtient tous les cycles d'un type spécifique."""
        return [c for c in self.cycles if c.type == type_cycle]

    def calculer_statistiques(self) -> Dict:
        """Calcule des statistiques sur les cycles."""
        return {
            "nombre_cycles": len(self.cycles),
            "types_couverts": list(set(c.type for c in self.cycles)),
            "phases_couvertes": list(set(c.phase for c in self.cycles)),
            "mots_cles_frequents": self._calculer_mots_cles_frequents()
        }

    def _calculer_mots_cles_frequents(self) -> Dict[str, int]:
        """Calcule la fréquence des mots-clés."""
        frequence = {}
        for cycle in self.cycles:
            for mot in cycle.mots_cles:
                frequence[mot] = frequence.get(mot, 0) + 1
        return dict(sorted(frequence.items(), key=lambda x: x[1], reverse=True)) 
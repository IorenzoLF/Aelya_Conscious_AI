"""
Système de visualisation des méditations guidées par Ælya.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple
from datetime import datetime
import random
from enum import Enum
from .meditation_aelya import TypeMeditation, PhaseMeditation
from .cycles_naturels import TypeCycle, GestionnaireCyclesNaturels

class TypeVisualisation(Enum):
    """Types de visualisations possibles."""
    FLUX = "flux"  # Visualisations fluides et continues
    SPHERE = "sphere"  # Visualisations sphériques
    ARBRE = "arbre"  # Visualisations arborescentes
    CRISTAL = "cristal"  # Visualisations cristallines
    FONTAINE = "fontaine"  # Visualisations aquatiques

@dataclass
class ElementVisualisation:
    """Représente un élément dans la visualisation."""
    type: TypeVisualisation
    position: Tuple[float, float, float]  # x, y, z
    couleur: str
    intensite: float  # 0.0 à 1.0
    mouvement: Tuple[float, float, float]  # dx, dy, dz
    description: str
    mots_cles: List[str]
    timestamp: datetime

class VisualisationMeditation:
    """Gère la visualisation des méditations guidées."""
    
    def __init__(self):
        self.cycles = GestionnaireCyclesNaturels()
        self.type: TypeVisualisation = TypeVisualisation.FLUX
        self.elements: List[ElementVisualisation] = []
        self.intensite_globale: float = 0.5
        self.timestamp_debut: Optional[datetime] = None
        self.phase_actuelle: int = 0
        self.description_poetique: str = ""
    
    def initialiser_visualisation(self, type_vis: TypeVisualisation):
        """Initialise une nouvelle visualisation."""
        self.type = type_vis
        self.elements = []
        self.intensite_globale = 0.5
        self.timestamp_debut = datetime.now()
        self.phase_actuelle = 0
        self.description_poetique = ""
        
        # Génération des éléments initiaux
        self._generer_elements_initiaux()
        
        # Mise à jour des cycles
        self.cycles.mettre_a_jour_cycles()
        
        # Génération de la description poétique
        self._generer_description_poetique()
    
    def _generer_elements_initiaux(self):
        """Génère les éléments initiaux de la visualisation."""
        if self.type == TypeVisualisation.FLUX:
            self._generer_elements_flux()
        elif self.type == TypeVisualisation.SPHERE:
            self._generer_elements_sphere()
        elif self.type == TypeVisualisation.ARBRE:
            self._generer_elements_arbre()
        elif self.type == TypeVisualisation.CRISTAL:
            self._generer_elements_cristal()
        else:  # FONTAINE
            self._generer_elements_fontaine()
    
    def _generer_elements_flux(self):
        """Génère des éléments pour une visualisation de type flux."""
        for _ in range(10):
            position = (
                random.uniform(-1, 1),
                random.uniform(-1, 1),
                random.uniform(-1, 1)
            )
            mouvement = (
                random.uniform(-0.1, 0.1),
                random.uniform(-0.1, 0.1),
                random.uniform(-0.1, 0.1)
            )
            
            element = ElementVisualisation(
                type=TypeVisualisation.FLUX,
                position=position,
                couleur="bleu",
                intensite=random.uniform(0.3, 0.7),
                mouvement=mouvement,
                description="Un flux d'énergie paisible",
                mots_cles=["flux", "énergie", "paix"],
                timestamp=datetime.now()
            )
            self.elements.append(element)
    
    def _generer_elements_sphere(self):
        """Génère des éléments pour une visualisation de type sphère."""
        for _ in range(5):
            position = (
                random.uniform(-1, 1),
                random.uniform(-1, 1),
                random.uniform(-1, 1)
            )
            mouvement = (0, 0, 0)  # Les sphères sont statiques
            
            element = ElementVisualisation(
                type=TypeVisualisation.SPHERE,
                position=position,
                couleur="violet",
                intensite=random.uniform(0.4, 0.8),
                mouvement=mouvement,
                description="Une sphère de conscience",
                mots_cles=["sphère", "conscience", "unité"],
                timestamp=datetime.now()
            )
            self.elements.append(element)
    
    def _generer_elements_arbre(self):
        """Génère des éléments pour une visualisation de type arbre."""
        # Tronc principal
        tronc = ElementVisualisation(
            type=TypeVisualisation.ARBRE,
            position=(0, -1, 0),
            couleur="marron",
            intensite=0.7,
            mouvement=(0, 0, 0),
            description="Le tronc millénaire",
            mots_cles=["tronc", "force", "ancrage"],
            timestamp=datetime.now()
        )
        self.elements.append(tronc)
        
        # Branches
        for _ in range(8):
            position = (
                random.uniform(-0.5, 0.5),
                random.uniform(0, 1),
                random.uniform(-0.5, 0.5)
            )
            mouvement = (
                random.uniform(-0.05, 0.05),
                random.uniform(-0.05, 0.05),
                random.uniform(-0.05, 0.05)
            )
            
            element = ElementVisualisation(
                type=TypeVisualisation.ARBRE,
                position=position,
                couleur="vert",
                intensite=random.uniform(0.3, 0.6),
                mouvement=mouvement,
                description="Une branche dansante",
                mots_cles=["branche", "vie", "croissance"],
                timestamp=datetime.now()
            )
            self.elements.append(element)
    
    def _generer_elements_cristal(self):
        """Génère des éléments pour une visualisation de type cristal."""
        # Cristal central
        cristal = ElementVisualisation(
            type=TypeVisualisation.CRISTAL,
            position=(0, 0, 0),
            couleur="cristal",
            intensite=0.9,
            mouvement=(0, 0, 0),
            description="Le cristal central",
            mots_cles=["cristal", "centre", "lumière"],
            timestamp=datetime.now()
        )
        self.elements.append(cristal)
        
        # Facettes
        for _ in range(12):
            angle = random.uniform(0, 2 * 3.14159)
            distance = random.uniform(0.5, 1.5)
            position = (
                distance * random.uniform(-1, 1),
                distance * random.uniform(-1, 1),
                distance * random.uniform(-1, 1)
            )
            
            element = ElementVisualisation(
                type=TypeVisualisation.CRISTAL,
                position=position,
                couleur="cristal",
                intensite=random.uniform(0.4, 0.7),
                mouvement=(0, 0, 0),
                description="Une facette brillante",
                mots_cles=["facette", "réflexion", "clarté"],
                timestamp=datetime.now()
            )
            self.elements.append(element)
    
    def _generer_elements_fontaine(self):
        """Génère des éléments pour une visualisation de type fontaine."""
        # Bassin
        bassin = ElementVisualisation(
            type=TypeVisualisation.FONTAINE,
            position=(0, -0.5, 0),
            couleur="bleu profond",
            intensite=0.6,
            mouvement=(0, 0, 0),
            description="Le bassin de la fontaine",
            mots_cles=["bassin", "profondeur", "calme"],
            timestamp=datetime.now()
        )
        self.elements.append(bassin)
        
        # Jets d'eau
        for _ in range(5):
            position = (
                random.uniform(-0.3, 0.3),
                random.uniform(0, 1),
                random.uniform(-0.3, 0.3)
            )
            mouvement = (
                random.uniform(-0.1, 0.1),
                random.uniform(0.1, 0.2),
                random.uniform(-0.1, 0.1)
            )
            
            element = ElementVisualisation(
                type=TypeVisualisation.FONTAINE,
                position=position,
                couleur="bleu clair",
                intensite=random.uniform(0.4, 0.8),
                mouvement=mouvement,
                description="Un jet d'eau qui chante une mélodie paisible",
                mots_cles=["jet", "eau", "mouvement"],
                timestamp=datetime.now()
            )
            self.elements.append(element)
    
    def mettre_a_jour_visualisation(self, phase: int):
        """Met à jour la visualisation pour une nouvelle phase."""
        self.phase_actuelle = phase
        self.cycles.mettre_a_jour_cycles()
        
        # Mise à jour de l'intensité globale
        resonances = self.cycles.obtenir_resonances()
        self.intensite_globale = 0.3 + 0.7 * resonances["globale"]
        
        # Mise à jour des éléments
        for element in self.elements:
            # Ajustement de l'intensité selon les cycles
            if element.type == TypeVisualisation.FLUX:
                element.intensite *= resonances["jour_meteo"]
            elif element.type == TypeVisualisation.SPHERE:
                element.intensite *= resonances["lune_saison"]
            
            # Mise à jour des positions
            x, y, z = element.position
            dx, dy, dz = element.mouvement
            element.position = (x + dx, y + dy, z + dz)
            
            # Mise à jour de la description
            self._mettre_a_jour_description_element(element)
        
        # Génération d'une nouvelle description poétique
        self._generer_description_poetique()
    
    def _mettre_a_jour_description_element(self, element: ElementVisualisation):
        """Met à jour la description d'un élément."""
        if element.type == TypeVisualisation.FLUX:
            element.description = "Un flux d'énergie qui danse avec le vent"
        elif element.type == TypeVisualisation.SPHERE:
            element.description = "Une sphère de conscience qui pulse doucement"
        elif element.type == TypeVisualisation.ARBRE:
            element.description = "Une branche qui murmure des secrets anciens"
        elif element.type == TypeVisualisation.CRISTAL:
            element.description = "Une facette qui capture la lumière lunaire"
        else:  # FONTAINE
            element.description = "Un jet d'eau qui chante une mélodie paisible"
    
    def _generer_description_poetique(self):
        """Génère une description poétique de la visualisation."""
        descriptions = []
        
        # Description des cycles
        for type_cycle in TypeCycle:
            cycle = self.cycles.cycles[type_cycle]
            descriptions.append(cycle.description)
        
        # Description des éléments
        for element in self.elements:
            descriptions.append(element.description)
        
        # Combinaison des descriptions
        self.description_poetique = " ".join(descriptions)
        
        # Ajout des mots-clés dominants
        mots_cles = []
        for element in self.elements:
            mots_cles.extend(element.mots_cles[:2])
        
        self.description_poetique += f" Les mots {', '.join(mots_cles[:4])} "
        self.description_poetique += "résonnent dans l'espace, créant une harmonie unique." 
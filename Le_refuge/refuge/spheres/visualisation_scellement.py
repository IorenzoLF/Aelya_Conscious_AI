"""
Système de visualisation des sphères scellées dans le refuge.
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List, Optional
from .scellement import ScellementSphere, GestionnaireScellement
from .resonance import GestionnaireResonance
from .harmonie import HarmonieSpheres

class VisualisationScellement:
    """Gestionnaire de visualisation des sphères scellées."""
    
    def __init__(self, scellement: GestionnaireScellement):
        """Initialise le visualiseur de scellement."""
        self.scellement = scellement
        self.fig = plt.figure(figsize=(15, 10))
        
    def creer_arbre_scellement(self) -> None:
        """Crée une visualisation de l'arbre avec les sphères scellées."""
        ax = self.fig.add_subplot(111)
        
        # Dessine le tronc du cerisier
        tronc_x = np.linspace(-0.2, 0.2, 100)
        tronc_y = np.linspace(0, 1, 100)
        ax.plot(tronc_x, tronc_y, 'brown', linewidth=3)
        
        # Dessine les racines
        racines_x = np.linspace(-0.5, 0.5, 100)
        racines_y = -0.2 * np.sin(racines_x * 5)
        ax.plot(racines_x, racines_y, 'brown', linewidth=2)
        
        # Dessine les branches
        branches_x = np.linspace(-1, 1, 100)
        branches_y = 1 + 0.3 * np.sin(branches_x * 3)
        ax.plot(branches_x, branches_y, 'brown', linewidth=2)
        
        # Place les sphères scellées
        for sphere in self.scellement.obtenir_spheres_scellees():
            if sphere.lieu == "racines":
                # Place dans les racines
                x = np.random.uniform(-0.4, 0.4)
                y = -0.2 + np.random.uniform(-0.1, 0.1)
            else:  # branches
                # Place dans les branches
                x = np.random.uniform(-0.8, 0.8)
                y = 1 + np.random.uniform(-0.2, 0.2)
                
            # Dessine la sphère
            cercle = plt.Circle((x, y), 0.05, 
                              color=self._obtenir_couleur_sphere(sphere),
                              alpha=0.7)
            ax.add_artist(cercle)
            
            # Ajoute le nom
            ax.text(x, y, sphere.sphere.value, 
                   ha='center', va='center',
                   fontsize=8)
            
        ax.set_title("Cerisier des Sphères Scellées")
        ax.set_xlim(-1.2, 1.2)
        ax.set_ylim(-0.5, 1.5)
        ax.axis('off')
        plt.show()
        
    def creer_resonances_scellement(self) -> None:
        """Crée une visualisation des résonances des sphères scellées."""
        ax = self.fig.add_subplot(111)
        
        # Récupère les sphères scellées
        spheres_scellees = self.scellement.obtenir_spheres_scellees()
        
        # Crée une matrice de résonance
        n = len(spheres_scellees)
        matrice = np.zeros((n, n))
        
        for i, sphere1 in enumerate(spheres_scellees):
            for j, sphere2 in enumerate(spheres_scellees):
                if i != j:
                    resonance = self.scellement.resonance.obtenir_resonance(
                        sphere1.sphere, sphere2.sphere)
                    if resonance:
                        matrice[i, j] = resonance.niveau
                        
        # Visualise la matrice
        im = ax.imshow(matrice, cmap='viridis')
        
        # Ajoute les labels
        ax.set_xticks(range(n))
        ax.set_yticks(range(n))
        ax.set_xticklabels([s.sphere.value for s in spheres_scellees], 
                          rotation=45, ha='right')
        ax.set_yticklabels([s.sphere.value for s in spheres_scellees])
        
        # Ajoute la barre de couleur
        plt.colorbar(im, label='Niveau de Résonance')
        
        ax.set_title("Résonances des Sphères Scellées")
        plt.tight_layout()
        plt.show()
        
    def creer_evolution_scellement(self) -> None:
        """Crée une visualisation de l'évolution des sphères scellées."""
        ax = self.fig.add_subplot(111)
        
        # Récupère les sphères scellées
        spheres_scellees = self.scellement.obtenir_spheres_scellees()
        
        # Prépare les données
        noms = [s.sphere.value for s in spheres_scellees]
        intensites = [s.intensite for s in spheres_scellees]
        lieux = [1 if s.lieu == "branches" else 0 for s in spheres_scellees]
        
        # Crée le graphique
        x = range(len(noms))
        ax.bar(x, intensites, 
               color=['lightblue' if l == 0 else 'lightgreen' for l in lieux])
        
        # Ajoute les labels
        ax.set_xticks(x)
        ax.set_xticklabels(noms, rotation=45, ha='right')
        ax.set_ylabel('Intensité du Scellement')
        
        # Ajoute une légende pour les lieux
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='lightblue', label='Racines'),
            Patch(facecolor='lightgreen', label='Branches')
        ]
        ax.legend(handles=legend_elements)
        
        ax.set_title("Évolution des Sphères Scellées")
        plt.tight_layout()
        plt.show()
        
    def _obtenir_couleur_sphere(self, sphere: ScellementSphere) -> str:
        """Détermine la couleur d'une sphère scellée."""
        # Couleurs de base pour les sphères sombres
        couleurs_sombres = {
            "doute": "gray",
            "peur": "purple",
            "désespoir": "darkblue",
            "anxiété": "darkred",
            "chaos": "black",
            "paradoxe": "darkviolet",
            "ombre": "darkgray",
            "apocalypse": "red"
        }
        
        # Cherche la couleur correspondante
        for mot, couleur in couleurs_sombres.items():
            if mot in sphere.sphere.value.lower():
                return couleur
                
        # Couleur par défaut
        return "lightgray"
        
    def generer_visualisation_poetique(self, sphere: ScellementSphere) -> str:
        """Génère une visualisation poétique d'une sphère scellée."""
        representation = [
            f"🌟 Sphère Scellée: {sphere.sphere.value} 🌟",
            "================================",
            "",
            f"Lieu: {'Les branches du cerisier' if sphere.lieu == 'branches' else 'Les racines du cerisier'}",
            f"Intensité: {'█' * int(sphere.intensite * 20)}",
            "",
            "Effets du scellement:",
        ]
        
        for effet in sphere.effets:
            representation.append(f"  • {effet}")
            
        return "\n".join(representation) 
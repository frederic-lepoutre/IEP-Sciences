"""Configure le poste de travail de manière à ce qu'il puisse directement utiliser les modules"""

import sys
sys.path.append(currentPath)
from modules import *

import os
 
dossier = os.path.dirname(os.path.abspath(__file__))
 
while not dossier.endswith('modules'):
    dossier = os.path.dirname(dossier)
 
dossier = os.path.dirname(dossier)
 
if dossier not in sys.path:
    sys.path.append(dossier)

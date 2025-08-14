#Crie um arquivo em python que abra e reproduza o audio de um arquivo MP3
import os
from pathlib import Path

# Pega a pasta onde o script está
script_dir = Path(__file__).parent

# Constrói o caminho do MP3 relativo ao script
mp3 = (script_dir / "../miscellaneous/ceu_azul.mp3").resolve()

# Abre no reprodutor padrão do Windows
os.startfile(mp3)

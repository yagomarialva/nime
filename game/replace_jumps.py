import re
import glob
import os

files = [
    "capitulos/capitulo9.rpy",
    "capitulos/capitulo8_inspecao.rpy",
    "capitulos/capitulo10.rpy",
    "capitulos/capitulo7_luau.rpy",
    "eventos/capitulo_6/capitulo6_inspecao.rpy",
    "eventos/capitulo_3/capitulo3_mural.rpy",
    "eventos/capitulo_4/capitulo4_quadra.rpy",
    "eventos/capitulo_5/capitulo5_confronto.rpy",
    "eventos/capitulo_2/capitulo2_crise_conta.rpy"
]

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Substituir 'jump capituloX' por 'call end_of_chapter_validation("capituloX")'
    new_content = re.sub(r'jump (capitulo[0-9]+|epilogo)$', r'call end_of_chapter_validation("\1")', content, flags=re.MULTILINE)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")


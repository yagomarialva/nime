label capitulo15_huey:
    if status_huey == "amizade":
        scene bg galeria_arte with fade
        narrator "A exposição exclusiva na galeria do centro era de Huey."
        narrator "As telas exibiam retratos fotográficos pintados à mão de bilionários aborrecidos e naturezas-mortas matematicamente precisas."
        narrator "Não havia cor, nem respingos fora do lugar."
        narrator "Huey assinou meu catálogo de braços cruzados. Ela era milionária. E era a artista mais triste do mundo. Eu desejei o melhor e voltei à minha vida sem cor."
        jump creditos_finais
        
    elif status_huey == "romance":
        scene bg galeria_arte_caos with fade
        narrator "O museu de arte contemporânea de Paris havia cedido a maior ala para a exposição de Huey."
        narrator "Era um caos de luzes, tintas vibrantes e abstrações que tiravam o fôlego de críticos engravatados."
        show huey happy at center
        narrator "A peça central do salão custava milhões. E era um retrato absurdamente apaixonado de nós dois nos beijando, pintado inteiramente com as 'cores mágicas' dela."
        narrator "Ela apareceu no meio da multidão, usando um vestido rasgado e respingado intencionalmente."
        show huey blush
        mc "Eu achei que o combinado era você não pintar a gente gigante no meio da França."
        huey "Você sabe que a geometria do amor não segue acordos verbais."
        narrator "Ela puxou minha gravata de forma abrupta, quebrando todo o protocolo de classe daquele lugar requintado."
        huey "Os críticos franceses disseram que a minha musa inspiradora é brilhante."
        mc "A obra deles é muito melhor pessoalmente."
        narrator "No meio dos flashes e das câmeras internacionais, nós nos beijamos na frente da nossa pintura. Nós éramos a verdadeira obra prima de Huey."
        jump creditos_finais

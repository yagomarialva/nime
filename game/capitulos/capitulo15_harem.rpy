label capitulo15_harem:
    if status_harem == "amizade":
        scene bg pub with fade
        narrator "Eu estava bebendo sozinho num pub, numa noite de chuva."
        narrator "O celular no meu bolso vibrou. Era uma notificação no grupo de WhatsApp 'Rua Aurora', que estava silenciado há três anos."
        narrator "Samantha enviou uma foto antiga de nós sete na escadaria da casa. Larissa comentou com um coração enferrujado. As outras apenas visualizaram."
        narrator "Dei um sorriso amargo, digitei 'Bons tempos', guardei o celular e terminei a minha cerveja solitária. A magia de morar juntos nunca mais seria recriada."
        jump creditos_finais
        
    elif status_harem == "romance":
        scene bg quintal_festa with fade
        narrator "A música pulsava. O cheiro de churrasco, incenso e tinta se misturavam de forma que só a casa da Rua Aurora conseguiria exalar."
        narrator "Nós éramos donos da casa agora. Compramos o lote completo e o dividimos."
        
        show larissa happy at left
        show samantha happy at right
        narrator "Larissa, a técnica invicta de vôlei, derrubava uma cerveja enquanto debatia a lógica de um novo sistema de jogo que Samantha desenhava numa das telas espalhadas pelo gramado."
        
        hide larissa
        hide samantha
        show katia happy at left
        show nicole happy at right
        narrator "A vereadora Katia discutia de forma calorosa (e regada a drinks baratos) com Nicole, que contava rindo como fez a mãe surtar numa reunião familiar quando descobriu que Nicole vivia num romance poliamoroso com um grupo tão caótico."
        
        hide katia
        hide nicole
        show camille blush at left
        show huey blush at right
        narrator "Camille pendurava prismas nos galhos da árvore, acalmando o caos de Huey que sujava as flores com spray brilhante."
        
        narrator "Elas pararam o que estavam fazendo. Todas as seis caminharam juntas na minha direção."
        narrator "Katia me puxou pelo colarinho, me roubando um beijo intenso. Larissa veio logo depois, enlaçando meu pescoço. Samantha se aconchegou nos meus braços, enquanto Camille deixava um rastro de beijos suaves no meu ombro."
        narrator "Huey manchou meu nariz de tinta vermelha beijando minha testa, e Nicole tomou os meus lábios na frente de todo o quintal."
        narrator "Não era uma amizade exótica. Era uma família."
        narrator "Uma família de mulheres apaixonadas umas pelas outras e completamente devotas à vida insana e barulhenta que construímos em volta do meu eixo."
        narrator "Era, sem a menor sombra de dúvidas, a vitória definitiva."
        jump creditos_finais

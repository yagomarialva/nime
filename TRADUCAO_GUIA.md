# Guia de Tradução - Ren'Py - NIME

## 📋 Estrutura de Tradução no Ren'Py

### 1. **Estrutura de Diretórios**

```
game/
├── capitulos/          # Código base (português - idioma padrão)
│   ├── intro.rpy
│   ├── capitulo1.rpy
│   └── ...
├── tl/                 # Diretório de traduções
│   ├── en/            # Traduções em inglês
│   │   ├── common.rpy
│   │   ├── gui.rpy
│   │   ├── intro_dialogues.rpy
│   │   └── capitulo1.rpy (criar quando necessário)
│   └── pt/            # Traduções em português (geralmente vazio, pois é o padrão)
│       └── ...
└── ...
```

### 2. **Princípios Fundamentais**

#### ✅ **Código Base (Português)**
- O código em `game/capitulos/` é o **idioma padrão** (português)
- **NÃO** use blocos `translate portuguese` no código base
- Escreva diretamente em português:

```python
# ✅ CORRETO - Código base
label prologo:
    sombra "Este jogo é recomendado para maiores de 18 anos."
    menu:
        "Sim, tenho 18 anos ou mais.":
            jump nome_jogador
        "Não, sou menor de idade.":
            return
```

#### ✅ **Traduções (Inglês)**
- Crie arquivos em `game/tl/en/` com blocos `translate english`
- Use o **mesmo nome do label**:

```python
# ✅ CORRETO - Tradução em inglês (game/tl/en/intro_dialogues.rpy)
translate english prologo:
    sombra "This game is recommended for ages 18 and up."
    menu:
        "Yes, I am 18 years old or older.":
            jump nome_jogador
        "No, I am underage.":
            return
```

### 3. **Como Traduzir Labels**

#### **Passo 1: Identificar Labels no Código Base**

No arquivo `game/capitulos/capitulo1.rpy`:
```python
label capitulo1:
    narrator "O auditório da Faculdade Solária estava repleto..."
    professor_wendell "Bem-vindos à Faculdade Solária..."
```

#### **Passo 2: Criar Arquivo de Tradução**

Crie `game/tl/en/capitulo1.rpy`:
```python
# English Translation - Chapter 1
translate english capitulo1:
    narrator "The Solária College auditorium was filled with anticipation..."
    professor_wendell "Welcome to Solária College, bright young minds..."
```

### 4. **Traduzindo Strings da Interface (GUI)**

#### **No Código Base:**
Use `_()` para strings traduzíveis:

```python
# ✅ CORRETO
textbutton _("Iniciar") action Start()
textbutton _("Carregar") action ShowMenu("load")
```

#### **Nas Traduções:**
Em `game/tl/en/gui.rpy`:
```python
translate english strings:
    old "Iniciar"
    new "Start"
    
    old "Carregar"
    new "Load"
```

### 5. **Traduzindo Nomes de Personagens**

#### **No Código Base:**
```python
define narrator = Character(None)
define nicole = Character("Nicole", color="#FF69B4")
```

#### **Na Tradução:**
Em `game/tl/en/common.rpy`:
```python
translate english strings:
    old "Nicole"
    new "Nicole"  # Nomes próprios geralmente não mudam
```

### 6. **Traduzindo Menus**

#### **No Código Base:**
```python
menu:
    "Quero aprender sobre as mecânicas do jogo":
        jump explicar_mecanicas
    "Prefiro descobrir jogando":
        jump iniciar_aventura
```

#### **Na Tradução:**
```python
translate english tutorial_mecanicas:
    menu:
        "I want to learn about the game mechanics":
            jump explicar_mecanicas
        "I prefer to discover by playing":
            jump iniciar_aventura
```

### 7. **Organização de Arquivos de Tradução**

#### **Estrutura Recomendada:**

```
game/tl/en/
├── common.rpy          # Strings comuns (títulos, UI básica)
├── gui.rpy             # Interface do usuário
├── intro_dialogues.rpy # Diálogos da introdução
├── capitulo1.rpy       # Capítulo 1
├── capitulo2.rpy       # Capítulo 2
└── ...
```

### 8. **Boas Práticas**

#### ✅ **FAÇA:**
1. **Mantenha a mesma estrutura** entre código base e traduções
2. **Use nomes de labels consistentes** - o nome do label deve ser idêntico
3. **Organize por capítulo** - um arquivo por capítulo facilita manutenção
4. **Comente suas traduções** - adicione comentários explicando contexto
5. **Teste ambas as versões** - sempre teste em português e inglês

#### ❌ **NÃO FAÇA:**
1. **Não use `translate portuguese`** no código base
2. **Não altere nomes de labels** nas traduções
3. **Não esqueça de traduzir menus** - menus também precisam de tradução
4. **Não misture idiomas** - mantenha consistência

### 9. **Exemplo Completo**

#### **Código Base (`game/capitulos/intro.rpy`):**
```python
label prologo:
    scene bg city with fade
    sombra "Este jogo é recomendado para maiores de 18 anos."
    sombra "Você confirma que tem 18 anos ou mais?"
    
    menu:
        "Sim, tenho 18 anos ou mais.":
            jump nome_jogador
        "Não, sou menor de idade.":
            sombra "Infelizmente, você não poderá jogar este jogo."
            return

label nome_jogador:
    $ nome = renpy.input("Digite seu nome:", length=20)
    $ nome = nome.strip()
    if nome == "":
        $ nome = "Jogador"
    sombra "Olá, [nome]. Seja bem-vindo(a)!"
    jump aviso_jogo
```

#### **Tradução (`game/tl/en/intro_dialogues.rpy`):**
```python
# English Translation - Introduction Dialogues
translate english prologo:
    scene bg city with fade
    sombra "This game is recommended for ages 18 and up."
    sombra "Do you confirm that you are 18 years old or older?"
    
    menu:
        "Yes, I am 18 years old or older.":
            jump nome_jogador
        "No, I am underage.":
            sombra "Unfortunately, you will not be able to play this game."
            return

translate english nome_jogador:
    $ nome = renpy.input("Enter your name:", length=20)
    $ nome = nome.strip()
    if nome == "":
        $ nome = "Player"
    sombra "Hello, [nome]. Welcome!"
    jump aviso_jogo
```

### 10. **Verificando Traduções**

#### **Ferramenta do Ren'Py:**
1. Abra o Launcher do Ren'Py
2. Selecione seu projeto
3. Clique em "Extract Dialogue" (Extrair Diálogo)
4. Isso criará um arquivo `.txt` com todas as strings que precisam de tradução

#### **Verificação Manual:**
1. Teste o jogo em português (idioma padrão)
2. Mude para inglês no menu
3. Verifique se todos os textos foram traduzidos
4. Procure por textos em português que aparecem em inglês (strings não traduzidas)

### 11. **Dicas Importantes**

- **Variáveis em strings**: `[nome]` funciona em ambos os idiomas
- **Nomes de personagens**: Geralmente não precisam tradução
- **Nomes de lugares**: Decida se traduz ou mantém (ex: "Faculdade Solária" vs "Solária College")
- **Expressões idiomáticas**: Adapte, não traduza literalmente
- **Contexto cultural**: Considere adaptações culturais quando necessário

### 12. **Fluxo de Trabalho Recomendado**

1. **Escreva o código base** em português
2. **Teste o jogo** em português
3. **Crie arquivo de tradução** em `game/tl/en/`
4. **Traduza label por label** mantendo a estrutura
5. **Teste em inglês** verificando todas as strings
6. **Corrija problemas** encontrados
7. **Repita para cada novo conteúdo**

---

## 🎯 Resumo Rápido

- **Código base** = Português (sem `translate portuguese`)
- **Traduções** = Inglês em `game/tl/en/` (com `translate english`)
- **Mesmo nome de label** em ambos
- **Use `_()`** para strings da interface
- **Organize por capítulo** em arquivos separados
- **Teste sempre** em ambos os idiomas


# Como Aplicar Traduções no Projeto NIME

## 🎯 Resumo Rápido

### Estrutura Atual do Projeto

```
game/
├── capitulos/              # ✅ Código base em PORTUGUÊS (idioma padrão)
│   ├── intro.rpy
│   ├── capitulo1.rpy
│   └── ...
│
└── tl/                     # ✅ Traduções
    ├── en/                 # Inglês
    │   ├── common.rpy      # ✅ Strings comuns
    │   ├── gui.rpy         # ✅ Interface
    │   ├── intro_dialogues.rpy  # ✅ Introdução
    │   └── capitulo1.rpy   # ✅ Capítulo 1 (criado)
    │
    └── pt/                 # Português (geralmente vazio - é o padrão)
```

## 📝 Passo a Passo para Traduzir

### 1. **Para Traduzir um Novo Capítulo**

#### Exemplo: Traduzir `capitulo2.rpy`

**Passo 1:** Verifique o código base em `game/capitulos/capitulo2.rpy`:
```python
label capitulo2:
    narrator "Texto em português aqui..."
    menu:
        "Opção 1":
            jump proximo
```

**Passo 2:** Crie `game/tl/en/capitulo2.rpy`:
```python
# English Translation - Chapter 2
translate english capitulo2:
    narrator "Text in English here..."
    menu:
        "Option 1":
            jump proximo
```

**Pronto!** O Ren'Py automaticamente usará a tradução quando o idioma for inglês.

### 2. **Para Traduzir Strings da Interface**

#### Exemplo: Traduzir texto do menu de idiomas

**No código base** (`game/language_menu.rpy`):
```python
text _("Selecionar Idioma / Select Language"):
```

**Na tradução** (`game/tl/en/gui.rpy`):
```python
translate english strings:
    old "Selecionar Idioma / Select Language"
    new "Select Language"
```

### 3. **Checklist de Tradução**

Para cada novo conteúdo adicionado:

- [ ] **Código base** escrito em português (sem `translate portuguese`)
- [ ] **Arquivo de tradução** criado em `game/tl/en/`
- [ ] **Mesmo nome de label** usado na tradução
- [ ] **Menus traduzidos** (opções de menu também precisam tradução)
- [ ] **Strings da interface** usando `_()` no código base
- [ ] **Testado** em ambos os idiomas

## 🔍 Verificando o que Precisa Traduzir

### Método 1: Usar a Ferramenta do Ren'Py

1. Abra o **Ren'Py Launcher**
2. Selecione seu projeto **NIME**
3. Clique em **"Extract Dialogue"** (Extrair Diálogo)
4. Isso criará um arquivo `.txt` listando todas as strings

### Método 2: Verificação Manual

1. **Execute o jogo em português** - verifique se tudo está correto
2. **Mude para inglês** no menu de idiomas
3. **Navegue pelo jogo** - qualquer texto em português que aparecer precisa de tradução
4. **Anote os labels** que não foram traduzidos
5. **Crie os arquivos de tradução** correspondentes

## 📂 Organização Recomendada

### Estrutura de Arquivos de Tradução

```
game/tl/en/
├── common.rpy              # Strings comuns (títulos, nomes, etc.)
├── gui.rpy                 # Interface do usuário
├── intro_dialogues.rpy     # Introdução e prólogo
├── capitulo1.rpy           # Capítulo 1
├── capitulo2.rpy           # Capítulo 2
├── capitulo3.rpy           # Capítulo 3
└── ...                     # Um arquivo por capítulo
```

### Por que Separar por Capítulo?

- ✅ **Fácil de encontrar** traduções específicas
- ✅ **Fácil de manter** - editar um capítulo não afeta outros
- ✅ **Fácil de revisar** - tradutores podem trabalhar em paralelo
- ✅ **Organizado** - estrutura clara e lógica

## ⚠️ Erros Comuns a Evitar

### ❌ ERRADO:
```python
# No código base
translate portuguese capitulo1:
    narrator "Texto..."
```

### ✅ CORRETO:
```python
# No código base (sem translate)
label capitulo1:
    narrator "Texto..."

# Na tradução (game/tl/en/capitulo1.rpy)
translate english capitulo1:
    narrator "Text..."
```

### ❌ ERRADO:
```python
# Mudar o nome do label na tradução
translate english capitulo_1:  # Nome diferente!
    narrator "Text..."
```

### ✅ CORRETO:
```python
# Mesmo nome do label
translate english capitulo1:  # Nome idêntico!
    narrator "Text..."
```

## 🎨 Exemplo Prático Completo

### Cenário: Adicionar um novo diálogo

**1. No código base** (`game/capitulos/capitulo3.rpy`):
```python
label capitulo3:
    scene bg classroom with fade
    show nicole happy at center
    
    nicole "Olá! Como foi seu dia?"
    
    menu:
        "Foi ótimo, obrigado!":
            nicole "Que bom! Fico feliz em saber."
            $ points_nicole += 5
        "Está sendo difícil...":
            nicole "Entendo. Se precisar conversar, estou aqui."
            $ points_nicole += 3
    
    jump capitulo3_continue
```

**2. Na tradução** (`game/tl/en/capitulo3.rpy`):
```python
# English Translation - Chapter 3
translate english capitulo3:
    scene bg classroom with fade
    show nicole happy at center
    
    nicole "Hello! How was your day?"
    
    menu:
        "It was great, thanks!":
            nicole "That's great! I'm glad to hear that."
            $ points_nicole += 5
        "It's been difficult...":
            nicole "I understand. If you need to talk, I'm here."
            $ points_nicole += 3
    
    jump capitulo3_continue
```

## 🚀 Fluxo de Trabalho Recomendado

1. **Desenvolver em português** - escreva todo o conteúdo em português primeiro
2. **Testar em português** - certifique-se de que está funcionando
3. **Criar estrutura de tradução** - crie o arquivo em `game/tl/en/`
4. **Traduzir conteúdo** - traduza label por label
5. **Testar em inglês** - mude o idioma e teste tudo
6. **Revisar e corrigir** - corrija qualquer problema encontrado

## 📊 Status Atual do Projeto

### ✅ Já Traduzido:
- [x] Strings comuns (`common.rpy`)
- [x] Interface (`gui.rpy`)
- [x] Introdução (`intro_dialogues.rpy`)
- [x] Capítulo 1 (`capitulo1.rpy`) - **criado agora**

### ⏳ Precisa Traduzir:
- [ ] Capítulo 2
- [ ] Capítulo 3
- [ ] Capítulo 4
- [ ] ... (outros capítulos)
- [ ] Eventos especiais
- [ ] Final do jogo

## 💡 Dicas Finais

1. **Sempre teste** após adicionar traduções
2. **Mantenha consistência** - use os mesmos termos em todo o jogo
3. **Adapte, não traduza literalmente** - considere o contexto cultural
4. **Revise com nativos** - se possível, peça revisão de falantes nativos
5. **Use comentários** - adicione comentários explicando contexto quando necessário

---

## 🎯 Resumo em Uma Frase

**Escreva em português no código base, crie arquivos `translate english` em `game/tl/en/` com o mesmo nome de label, e o Ren'Py fará o resto automaticamente!**


# Estrutura Correta de Tradução - Ren'Py

## ✅ Estrutura Atual (CORRETA)

```
game/
├── capitulos/          # ✅ Código base em PORTUGUÊS (idioma padrão)
│   ├── intro.rpy
│   ├── capitulo1.rpy
│   └── ...
│
└── tl/                 # ✅ Diretório de traduções
    ├── en/            # ✅ Traduções em INGLÊS
    │   ├── common.rpy
    │   ├── gui.rpy
    │   ├── intro_dialogues.rpy
    │   └── capitulo1.rpy
    │
    └── pt/            # ⚠️ Geralmente vazio (português é o padrão)
```

## 🔍 Por que não está traduzindo?

### Possíveis Causas:

1. **Idioma padrão não configurado** - Adicionei `config.language = "portuguese"` no `options.rpy`
2. **Tradução incompleta** - O arquivo `capitulo1.rpy` em inglês só tem a primeira parte
3. **Cache do Ren'Py** - Pode precisar limpar o cache

## ✅ Solução: Estrutura Mantida (Recomendada)

**NÃO é necessário mover os arquivos!** A estrutura atual está correta. O problema é que:

1. ✅ O código base em `game/capitulos/` é o idioma padrão (português)
2. ✅ As traduções em `game/tl/en/` são para inglês
3. ⚠️ O Ren'Py precisa que o idioma padrão esteja configurado

## 🔧 O que foi corrigido:

1. ✅ Adicionei `config.language = "portuguese"` no `options.rpy`
2. ✅ O sistema de troca de idioma já está funcionando
3. ⚠️ Você precisa completar as traduções dos capítulos

## 📝 Próximos Passos:

1. **Teste novamente** - O idioma padrão agora está configurado
2. **Complete as traduções** - Adicione todos os labels do capítulo 1 em inglês
3. **Limpe o cache** se necessário:
   - Delete a pasta `game/cache/`
   - Ou use "Force Recompile" no Ren'Py Launcher

## 🎯 Como Funciona:

- **Português (padrão)**: Ren'Py usa `game/capitulos/` diretamente
- **Inglês**: Ren'Py procura em `game/tl/en/` e substitui os labels traduzidos

**A estrutura atual está CORRETA!** Não precisa mover nada.


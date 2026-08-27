# Traduzir os artigos EN → PT preservando o layout

Pipeline **testado de ponta a ponta** em 27/08/2026, nos próprios artigos do bloco 2. O que está
aqui foi executado, não copiado de documentação.

Ferramenta: **pdf2zh-next** (PDFMathTranslate v2), que roda sobre a biblioteca **BabelDOC**.
Faz análise de layout, traduz só os blocos de texto, preserva fórmulas e figuras, e gera **dois
PDFs**: um só em português (`mono`) e um **bilíngue lado a lado** (`dual`).

## Instalação no Windows

```powershell
py -m venv venv-traducao
.\venv-traducao\Scripts\activate
pip install pdf2zh-next
```

> ⚠️ **Não instale `pdf2zh` (v1).** Testado aqui: a v1 (1.9.11) **quebra na importação** com as
> dependências atuais — `ImportError: cannot import name 'TextTranslateRequest'` vindo do SDK da
> Tencent. O pacote correto é **`pdf2zh-next`** (v2.9.0 no teste).

Boa notícia sobre peso: usa **onnxruntime**, não PyTorch. Roda em CPU, sem GPU. O modelo de
análise de layout é baixado sozinho no primeiro uso.

## Uso — PDF normal (nascido digital)

```powershell
pdf2zh artigo.pdf --lang-in en --lang-out pt --google `
  --watermark-output-mode no_watermark --output saida
```

Gera em `saida\`:

| Arquivo | O que é |
|---|---|
| `artigo.pt.dual.pdf` | **bilíngue**, página original à esquerda e tradução à direita (folha de 1224 pt de largura) |
| `artigo.pt.mono.pdf` | só português, mesmo layout do original |

O `dual` é o melhor para estudar: quando a tradução ficar estranha, o original está do lado.

Sem `--watermark-output-mode no_watermark`, o BabelDOC carimba um aviso em chinês no topo da
primeira página.

## Uso — PDF escaneado

Alguns artigos do acervo são **digitalizações**, não PDFs nascidos digitais. O pdf2zh detecta e
**se recusa a traduzir**: `Detected 12 scanned pages` → `Scanned PDF detected`.

Duas saídas, e a diferença de qualidade é enorme:

**Rápida — aceitar a camada de OCR que já existe:**

```powershell
pdf2zh artigo.pdf --lang-in en --lang-out pt --google --auto-enable-ocr-workaround --output saida
```

Funciona, mas **se o OCR original for ruim, a tradução herda o lixo**. Testado no Newell & Simon
de 1976: a frase famosa *"Computer science is an empirical discipline"* saiu como *"()u~ view é
apenas um de Jmu~y"*. Inutilizável.

**Correta — re-OCRizar antes:**

```powershell
pip install ocrmypdf
ocrmypdf --force-ocr -l eng artigo.pdf artigo_ocr.pdf
pdf2zh artigo_ocr.pdf --lang-in en --lang-out pt --google `
  --watermark-output-mode no_watermark --skip-scanned-detection --output saida
```

O `ocrmypdf` no Windows precisa de **Tesseract** e **Ghostscript** instalados à parte
(https://github.com/UB-Mannheim/tesseract/wiki e https://www.ghostscript.com/releases/). Depois
do re-OCR, o mesmo trecho saiu como *"A ciência da computação é uma disciplina empírica"*.

## Serviços de tradução

O `--google` usa o endpoint gratuito, **sem chave de API**. Foi o que funcionou nos testes.
Outras opções sem chave: `--bing` (falhou no teste, HTTPError) e `--siliconflowfree`. Com chave:
`--deepl`, `--openai`, `--gemini`, entre outras. E `--ollama` roda com modelo local, se quiser
tudo offline.

Para ver tudo: `pdf2zh --help`.

## Qualidade — o que esperar

Do teste real nos artigos do bloco 2:

| Elemento | Resultado |
|---|---|
| Texto corrido | **muito bom** — português natural, termos técnicos corretos |
| Layout de duas colunas | **preservado** |
| Fórmulas e figuras | **preservadas** (não são traduzidas, é o desejado) |
| Numeração de páginas e seções | preservada |
| Nomes e afiliações de autores | ⚠️ **erra** — "Michael D. Mumford, University of Oklahoma" virou "Universidade Michael D. Mumford de Oklahoma" |
| Tabelas | só com `--translate-table-text` |
| PDF escaneado | exige re-OCR antes, senão o resultado é inutilizável |

Vale a regra geral: **para citar no artigo da Tarefa 1, volte sempre ao original em inglês.** A
tradução é para estudar, não para citar.

## Privacidade

`--google` e `--bing` **enviam o texto dos artigos para servidores de terceiros**. Para material
didático publicado isso é irrelevante, mas se algum dia for texto próprio não publicado, use
`--ollama` com modelo local.

## Já traduzidos

Em `../materiais/02-busca/traduzidos/`:

- `2005_Heuristics_Mumford_PT-dual.pdf` — bilíngue, direto
- `1975_NewellSimon_TuringAward_PT-dual.pdf` — bilíngue, após re-OCR
- `1975_NewellSimon_TuringAward_reOCR-EN.pdf` — o original re-OCRizado, útil por si só, porque
  agora é pesquisável

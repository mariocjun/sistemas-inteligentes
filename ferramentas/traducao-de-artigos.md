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

## Como o app funciona — e onde entra a tradução

O pdf2zh **não tem modelo de tradução próprio**. Ele faz três coisas, e só a primeira é local:

1. **Análise de layout**, com um modelo **DocLayout-YOLO** em ONNX que roda **na sua máquina**.
   É ele que identifica colunas, parágrafos, fórmulas, figuras e legendas. Não precisa de GPU
   nem de internet.
2. **Extração e reagrupamento** do texto dos blocos que devem ser traduzidos, protegendo fórmulas
   e figuras como espaços reservados.
3. **Tradução**: manda o texto para um **serviço externo que você escolhe** e recebe de volta.
4. **Retipografia**: reencaixa o texto traduzido nas caixas originais, ajustando quebras e fontes,
   e gera os dois PDFs.

Ou seja: o "cérebro" que entende a página é local; o "tradutor" é terceirizado.

### Os 24 motores de tradução

A versão 2.9.0 oferece 24 motores. **Sem chave paga:**

| Motor | Como funciona |
|---|---|
| `--siliconflowfree` | **é o padrão**. Usa o modelo **THUDM/GLM-4-9B-0414** através de um proxy do mantenedor do projeto |
| `--google` | endpoint público do Google Tradutor. **Foi o usado nos nossos testes** |
| `--bing` | endpoint público do Bing. Falhou aqui com HTTPError |
| `--ollama` / `--xinference` | **LLM local na sua máquina** — nada sai do computador |
| `--clitranslator` | chama qualquer comando externo seu |

Com chave própria: `--deepl`, `--openai`, `--gemini`, `--deepseek`, `--grok`, `--groq`,
`--azure`, entre outros.

> ⚠️ `--google` e `--bing` estão marcados como **DEPRECATED** na documentação oficial. Funcionam
> hoje, mas podem parar sem aviso. Se pararem, o caminho é `--siliconflowfree` (padrão) ou
> `--ollama` com modelo local.

### Custo

**Zero.** O projeto é open source, o modelo de layout roda local, e os motores acima não pedem
cartão nem chave. O único custo é tempo de CPU.

## Privacidade — leia antes de usar em material sensível

- `--google` e `--bing` enviam o texto para Google e Microsoft.
- `--siliconflowfree`, que é o **padrão**, envia o conteúdo para um **proxy do mantenedor do
  projeto** antes de chegar à SiliconFlow. Está na própria documentação oficial.
- Para material didático publicado isso é irrelevante. Para texto próprio não publicado — um
  rascunho de artigo, por exemplo — use **`--ollama`** com modelo local.

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

## Validação das traduções

Conferidas contra o original, passagem a passagem. **Veredito: fiéis, não simplificadas.** Nada
de conteúdo foi omitido ou resumido; a estrutura argumentativa dos resumos foi preservada
integralmente, e os termos técnicos saíram corretos — *complexidade computacional*, *nível
algorítmico*, *racionalidade ecológica*, *enculturação*, *compromisso precisão-esforço*.

Dois problemas reais, ambos de forma e não de conteúdo:

**1. Mistura de português europeu e brasileiro, às vezes no mesmo parágrafo.** No Pantsar 2019
aparecem "é frequentemente **aceite**", "**modelação** de tarefas cognitivas" e "algoritmos
humanamente **óptimos**" — e, três linhas depois, "**modelagem**" e "**ótimos**". No Gigerenzer
2011, "Tal como **reflectido**". Não atrapalha a leitura, mas se algum trecho for parar num texto
seu, normalize.

**2. Quebras de palavra no meio.** Ocasionalmente sai "est\nudados" em vez de "estudados", quando
a retipografia quebra a linha dentro da palavra.

Um terceiro ponto, estrutural: o roadmap do BabelDOC ainda lista como **não implementado** o
suporte a parágrafos que atravessam colunas ou páginas. Na prática, um parágrafo que começa no pé
de uma coluna e termina no topo da outra é traduzido como dois pedaços independentes, o que
ocasionalmente produz uma emenda estranha.

> Regra prática: **a tradução serve para estudar; para citar no artigo, volte ao original.**

## Já traduzidos

Em `../materiais/02-busca/traduzidos/`:

| Arquivo | Estado |
|---|---|
| `2005_Heuristics_Mumford_PT-dual.pdf` | ✅ bom |
| `1991_Gigerenzer_BeyondBiases_PT-dual.pdf` | ✅ bom |
| `2011_Gigerenzer_HeuristicDecisionMaking_PT-dual.pdf` | ✅ bom |
| `2019_Pantsar_CognitiveComputationalComplexity_PT-dual.pdf` | ✅ bom |
| `1975_NewellSimon_TuringAward_PT-dual-PARCIAL.pdf` | ⚠️ **parcial** — ver abaixo |
| `1975_NewellSimon_TuringAward_reOCR-EN.pdf` | o original re-OCRizado, em inglês, agora pesquisável |

### O caso do Newell & Simon (1976)

Esse artigo é uma **digitalização** de uma revista de 1976, e derrotou o pipeline. O histórico do
que foi tentado, porque é instrutivo:

| Tentativa | Resultado |
|---|---|
| pdf2zh direto | recusa: `Detected 12 scanned pages` |
| `--auto-enable-ocr-workaround` no original | traduz e **aparece na página**, mas o OCR original é péssimo: *"Computer science is an empirical discipline"* virou *"()u~ view é apenas um de Jmu~y"* |
| `ocrmypdf --force-ocr` e depois traduzir | o texto extraído fica em português, mas **a página continua mostrando inglês** — o `--force-ocr` rasteriza a página em imagem, e a tradução vai só para a camada de texto invisível |
| `ocrmypdf --force-ocr` + `--skip-scanned-detection` + `--ocr-workaround` | idem: `--skip-scanned-detection` desliga justamente a etapa que cobriria a imagem |
| `ocrmypdf --redo-ocr` + `--auto-enable-ocr-workaround` | **melhor resultado**, mas ainda parcial: alguns blocos aparecem em português e outros permanecem em inglês |

**Lição:** verificar a tradução de um PDF escaneado **rasterizando a página e olhando**, nunca só
extraindo o texto — a camada de texto pode estar traduzida enquanto a imagem visível continua no
original.

Para digitalizações antigas, o caminho confiável é usar o `reOCR-EN` (pesquisável) e traduzir
trecho a trecho conforme a leitura, em vez de tentar produzir um PDF traduzido inteiro.

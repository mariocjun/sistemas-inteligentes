# Exemplos AIMA (Artificial Intelligence: A Modern Approach)

**Localização:** `C:\Users\MarioCordeiroJunior\.gemini\antigravity\scratch\antigravity-master\lib\aima-python`

Repositório oficial: https://github.com/aimacode/aima-python

## 📚 Módulos principais (aima/)

| Módulo | Conteúdo | Relevância |
|--------|----------|-----------|
| `search.py` | BFS, DFS, A*, best-first, hill-climbing, simulated annealing, genetic algorithms | **Bloco 2 — Busca** |
| `learning.py` | Decision trees, ensemble methods (Random Forest), neural networks | **Blocos 4-5** |
| `planning.py` | STRIPS, forward/backward search, GraphPlan | **Bloco 3** |
| `games.py` | Minimax, alpha-beta pruning, game trees | **Bloco 2** |
| `logic.py` | Propositional/first-order logic, inference (resolution) | **Bloco 3** |
| `probability.py` | Probabilistic inference, Bayes nets | **Complementar** |
| `agents.py` | Agent architecture, environment simulation | **Bloco 1** |
| `csp.py` | Constraint satisfaction (backtracking, AC-3) | **Complementar** |

## 🎮 Exemplos com GUI (gui/)

### Busca e TSP
- **`tsp.py`** — Traveling Salesman Problem
  - Simulated annealing
  - 2-opt neighborhood
  - Map of Romania exemplo
  - **Para Tarefa 1**

- **`eight_puzzle.py`** — 8-puzzle problem
  - A* search
  - Manhattan distance heuristic
  - Visualização interativa

- **`romania_problem.py`** — Graph search (mapa Romênia)
  - BFS, DFS, UCS, A*
  - Mapa interativo

### Algoritmos evolutivos
- **`genetic_algorithm_example.py`** — Phrase generation com AG
  - Crossover e mutação
  - Population management
  - Fitness tracking
  - **Para Tarefa 1**

### Outros
- **`vacuum_agent.py`** — Vacuum world agent
- **`tic-tac-toe.py`** — Jogo da velha com adversarial search
- **`grid_mdp.py`** — Markov Decision Process

## 📓 Notebooks (notebooks/)

Encontrados durante exploração anterior (78 arquivos):
- `search.ipynb` — Busca detalhada
- `learning.ipynb` — Aprendizado
- `neural_nets.ipynb` — Redes neurais
- `planning.ipynb` — Planejamento
- `games.ipynb` — Jogos
- E mais 73 arquivos específicos por capítulo

## ✅ Integração ao repositório

### Próximas ações:

1. **Copiar módulos AIMA principais** para `implementacoes/aima/`
2. **Adaptar exemplos TSP/AG** para trabalhar com nosso projeto
3. **Criar wrapper** que use classes AIMA em vez de reimplementação
4. **Adicionar notebooks** dos capítulos relevantes

### Exemplo de uso direto:

```python
import sys
sys.path.insert(0, r'C:\Users\MarioCordeiroJunior\.gemini\antigravity\scratch\antigravity-master\lib')
from aima.search import Problem, simulated_annealing

class TSPProblem(Problem):
    # Herdar de Problem do AIMA
    pass
```

## 🔗 Referências

- **Repositório oficial:** https://github.com/aimacode/aima-python
- **Livro:** Russell & Norvig (2020) — Inteligência Artificial (4ª ed.)
- **Documentação:** Comentários inline nos arquivos `.py` do AIMA

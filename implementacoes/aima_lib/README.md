# AIMA — Biblioteca de Inteligência Artificial

Módulos copiados do repositório oficial [AIMA Python](https://github.com/aimacode/aima-python).

**Referência:** Russell & Norvig (2020) — *Artificial Intelligence: A Modern Approach* (4ª ed.)

## 📦 Módulos inclusos

| Módulo | Tamanho | Uso |
|--------|---------|-----|
| `search.py` | 78.5 KB | BFS, DFS, A*, Simulated Annealing, Genetic Algorithm |
| `learning.py` | 56.7 KB | Decision Trees, Random Forest, Neural Networks |
| `planning.py` | 108.6 KB | STRIPS, GraphPlan |
| `logic.py` | 82.6 KB | First-order logic, Inference |
| `agents.py` | 39.4 KB | Agent architecture |
| `games.py` | 24.7 KB | Minimax, Alpha-Beta |
| `utils.py` | 26.6 KB | Utilidades (heap, vectors) |

**Total:** ~417 KB de código Python puro

## 🚀 Como usar

### Importar diretamente

```python
from aima.search import (
    BreadthFirstSearch, DepthFirstSearch, AStarSearch,
    simulated_annealing, genetic_algorithm,
    Problem, Graph
)

from aima.learning import DecisionTreeLearner, RandomForestLearner

from aima.planning import GraphPlan
```

### Exemplo: TSP com Simulated Annealing (AIMA)

```python
from aima.search import Problem, simulated_annealing
import math

class TSProblem(Problem):
    def actions(self, state):
        return [lambda s: two_opt(s, i, j) 
                for i in range(len(state))
                for j in range(i+1, len(state))]
    
    def result(self, state, action):
        return action(state)
    
    def value(self, state):
        # Negative cost (maximizing = minimizing distance)
        return -1 * path_cost(state)

# Usar
problem = TSProblem(initial=initial_tour)
solution = simulated_annealing(problem)
```

## 📚 Blocos de cobertura

- **Bloco 1 (Agentes):** `agents.py`
- **Bloco 2 (Busca):** `search.py` com 8 algoritmos diferentes
- **Bloco 3 (Lógica/Planning):** `logic.py`, `planning.py`
- **Bloco 4 (Aprendizado Simbólico):** `learning.py` com árvores e florestas
- **Bloco 5 (Redes Neurais):** `learning.py` tem bases (ver para deep learning)

## 🔗 Referências

- Repositório oficial: https://github.com/aimacode/aima-python
- Documentação online: https://aimacode.github.io/aima-python/
- Livro: https://aima.cs.berkeley.edu/

## ⚠️ Notas

- Código comentado em inglês (documentação do livro)
- Cada classe/função tem docstring descrevendo algoritmo
- Compatível com Python 3.6+
- Uso livre sob licença MIT (ver repositório oficial)

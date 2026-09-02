#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TSP com AIMA — Versão standalone (roda tudo de uma vez)

Integra biblioteca AIMA para resolver Traveling Salesman Problem.
Simulated Annealing + Genetic Algorithm + Comparação.
"""

import sys
import os

# Adicionar aima_lib ao path como pacote 'aima'
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(script_dir, '..')
parent_dir = os.path.abspath(parent_dir)

if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

import numpy as np
import matplotlib.pyplot as plt
import random
import math
from typing import List, Tuple

# Tentar importar AIMA
AIMA_AVAILABLE = False
try:
    # Tentar importar do pacote aima_lib
    import aima_lib.search as search_aima
    from aima_lib.search import Problem

    simulated_annealing = search_aima.simulated_annealing
    genetic_algorithm = search_aima.genetic_algorithm
    init_population = search_aima.init_population
    hill_climbing = search_aima.hill_climbing
    AIMA_AVAILABLE = True
except (ImportError, AttributeError) as e:
    print(f"Aviso: AIMA nao carregado ({e})")

random.seed(42)
np.random.seed(42)

print("=" * 70)
print("TSP com AIMA (Artificial Intelligence: A Modern Approach)")
print("=" * 70)

# ============================================================================
# 1. FALLBACK: Definir classe Problem se AIMA nao estiver disponivel
# ============================================================================

if not AIMA_AVAILABLE:
    class Problem:
        """Classe base para problemas de busca (fallback)."""
        def __init__(self, initial):
            self.initial = initial

# ============================================================================
# 2. DEFINIR TSPProblem
# ============================================================================

class TSPProblem(Problem):
    """Traveling Salesman Problem usando classe Problem do AIMA."""

    def __init__(self, cities: np.ndarray, initial_state=None):
        self.cities = cities
        self.n_cities = len(cities)
        self.distances = self._compute_distances()

        if initial_state is None:
            initial_state = list(range(self.n_cities))
            random.shuffle(initial_state)

        super().__init__(tuple(initial_state))

    def _compute_distances(self) -> np.ndarray:
        """Calcula matriz de distâncias euclidianas."""
        n = len(self.cities)
        distances = np.zeros((n, n))
        for i in range(n):
            for j in range(i+1, n):
                dist = np.linalg.norm(self.cities[i] - self.cities[j])
                distances[i, j] = distances[j, i] = dist
        return distances

    def actions(self, state):
        """2-opt: retorna pares (i, j) para reverter."""
        n = len(state)
        return [(i, j) for i in range(n) for j in range(i+2, n)]

    def result(self, state, action):
        """Aplicar 2-opt: reverter segmento."""
        state = list(state)
        i, j = action
        state[i:j+1] = reversed(state[i:j+1])
        return tuple(state)

    def value(self, state) -> float:
        """Valor heurístico para otimização (negativo = minimizar)."""
        return -self._calculate_cost(state)

    def _calculate_cost(self, state) -> float:
        """Calcula distância total de um tour."""
        cost = 0.0
        for i in range(len(state)):
            from_city = state[i]
            to_city = state[(i + 1) % len(state)]
            cost += self.distances[from_city, to_city]
        return cost

    def goal_test(self, state):
        """TSP é problema de otimização, não tem objetivo."""
        return False


# Criar instância
print("\n1. CRIANDO INSTANCIA TSP")
print("-" * 70)

np.random.seed(42)
cities = np.random.rand(10, 2) * 100
tsp_problem = TSPProblem(cities)

print(f"Numero de cidades: {tsp_problem.n_cities}")
print(f"Estado inicial: {tsp_problem.initial[:5]}...")
print(f"Custo inicial: {tsp_problem._calculate_cost(tsp_problem.initial):.2f}")

# ============================================================================
# 2. SIMULATED ANNEALING
# ============================================================================

print("\n2. SIMULATED ANNEALING (AIMA)")
print("-" * 70)

def schedule(t):
    """Agenda de temperatura: T(t) = T0 * exp(-c*t)"""
    return 1000.0 * math.exp(-0.005 * t)

solution_sa = None
cost_sa = None

if AIMA_AVAILABLE:
    try:
        print("Executando simulated_annealing()...")
        solution_sa = simulated_annealing(tsp_problem, schedule)
        cost_sa = tsp_problem._calculate_cost(solution_sa)
        print(f"Solucao: {solution_sa[:5]}...")
        print(f"Custo: {cost_sa:.2f}")
    except Exception as e:
        print(f"Erro: {e}")
else:
    print("AIMA nao disponivel")

# ============================================================================
# 3. GENETIC ALGORITHM
# ============================================================================

print("\n3. GENETIC ALGORITHM (AIMA)")
print("-" * 70)

solution_ga = None
cost_ga = None

if AIMA_AVAILABLE:
    try:
        print("Executando genetic_algorithm()...")

        gene_pool = list(range(tsp_problem.n_cities))

        def fitness_tsp(individual):
            cost = tsp_problem._calculate_cost(individual)
            return 1.0 / (1.0 + cost)

        # Inicializar populacao
        population = init_population(pop_size=30, gene_pool=gene_pool, n=tsp_problem.n_cities)

        # Rodar AG
        solution_ga = genetic_algorithm(
            population,
            fitness_fn=fitness_tsp,
            gene_pool=gene_pool,
            f_thres=1e6,
            ngen=100,
            pmut=0.1
        )

        cost_ga = tsp_problem._calculate_cost(solution_ga)
        print(f"Solucao: {solution_ga[:5]}...")
        print(f"Custo: {cost_ga:.2f}")
    except Exception as e:
        print(f"Erro: {e}")
else:
    print("AIMA nao disponivel")

# ============================================================================
# 4. HILL CLIMBING
# ============================================================================

print("\n4. HILL CLIMBING (AIMA)")
print("-" * 70)

solution_hc = None
cost_hc = None

if AIMA_AVAILABLE:
    try:
        print("Executando hill_climbing()...")
        solution_hc = hill_climbing(tsp_problem)
        cost_hc = tsp_problem._calculate_cost(solution_hc)
        print(f"Solucao: {solution_hc[:5]}...")
        print(f"Custo: {cost_hc:.2f}")
        print("(Hill climbing fica facilmente em otimos locais)")
    except Exception as e:
        print(f"Erro: {e}")
else:
    print("AIMA nao disponivel")

# ============================================================================
# 5. COMPARACAO
# ============================================================================

print("\n5. COMPARACAO DE RESULTADOS")
print("-" * 70)

solutions = []
if solution_sa is not None:
    solutions.append(("Simulated Annealing", cost_sa, solution_sa))
    print(f"SA: {cost_sa:.2f}")

if solution_ga is not None:
    solutions.append(("Genetic Algorithm", cost_ga, solution_ga))
    print(f"AG: {cost_ga:.2f}")

if solution_hc is not None:
    solutions.append(("Hill Climbing", cost_hc, solution_hc))
    print(f"HC: {cost_hc:.2f}")

if solutions:
    best_name, best_cost, best_solution = min(solutions, key=lambda x: x[1])
    print(f"\nVencedor: {best_name} (custo: {best_cost:.2f})")

# ============================================================================
# 6. VISUALIZACOES
# ============================================================================

print("\n6. GERANDO GRAFICOS")
print("-" * 70)

def plot_tour(cities, tour, title, cost, filename):
    """Plota um tour."""
    fig, ax = plt.subplots(figsize=(8, 8))

    ax.scatter(cities[:, 0], cities[:, 1], c='red', s=100, zorder=3)

    tour_list = list(tour)
    tour_points = cities[tour_list + [tour_list[0]]]
    ax.plot(tour_points[:, 0], tour_points[:, 1], 'b-', linewidth=2, zorder=1)

    for i, (x, y) in enumerate(cities):
        ax.annotate(str(i), (x, y), xytext=(5, 5), textcoords='offset points', fontsize=9)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f"{title}\n(Custo: {cost:.2f})")
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.savefig(filename, dpi=100, bbox_inches='tight')
    plt.close()
    print(f"  Salvo: {filename}")

if solution_sa is not None:
    plot_tour(cities, solution_sa, "AIMA: Simulated Annealing", cost_sa, "tour_sa_aima.png")

if solution_ga is not None:
    plot_tour(cities, solution_ga, "AIMA: Genetic Algorithm", cost_ga, "tour_ga_aima.png")

if solution_hc is not None:
    plot_tour(cities, solution_hc, "AIMA: Hill Climbing", cost_hc, "tour_hc_aima.png")

# ============================================================================
# 7. RESUMO
# ============================================================================

print("\n" + "=" * 70)
print("RESUMO")
print("=" * 70)
print(f"\nTSP com {tsp_problem.n_cities} cidades")
print(f"Espaco de buscas: {math.factorial(tsp_problem.n_cities):,} permutacoes")
print(f"\nAlgoritmos testados: {len(solutions)}")
if solutions:
    print(f"Melhor solucao: {best_name} ({best_cost:.2f})")
print("\nGraficos salvos:")
for name, cost, _ in solutions:
    print(f"  - tour_{name.lower().replace(' ', '_')}_aima.png")

print("\n" + "=" * 70)
print("AIMA + TSP CONCLUIDO")
print("=" * 70)
print("\nReferencias:")
print("  - https://github.com/aimacode/aima-python")
print("  - Russell & Norvig (2020) — Artificial Intelligence (4a ed.)")

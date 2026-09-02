#!/usr/bin/env python3
"""
Executa o notebook TSP — Tempera Simulada e Algoritmo Genetico
"""

import json
import numpy as np
import matplotlib.pyplot as plt
import random
from typing import List
import math

# ============================================================================
# SETUP
# ============================================================================

random.seed(42)
np.random.seed(42)

# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("=" * 70)
print("TSP - Tempera Simulada e Algoritmo Genetico")
print("=" * 70)

# ============================================================================
# 1. DEFINIÇÃO DO PROBLEMA TSP
# ============================================================================

class TSPInstance:
    """Instância do Problema do Caixeiro Viajante."""

    def __init__(self, cities: np.ndarray, name: str = "TSP"):
        self.cities = cities
        self.n_cities = len(cities)
        self.name = name
        self._compute_distances()

    def _compute_distances(self):
        """Pré-computa matriz de distâncias euclidianas."""
        self.distances = np.zeros((self.n_cities, self.n_cities))
        for i in range(self.n_cities):
            for j in range(self.n_cities):
                if i != j:
                    dx = self.cities[i][0] - self.cities[j][0]
                    dy = self.cities[i][1] - self.cities[j][1]
                    self.distances[i][j] = np.sqrt(dx**2 + dy**2)

    def evaluate(self, tour: List[int]) -> float:
        """Calcula o custo total de um tour (menor é melhor)."""
        cost = 0.0
        for i in range(len(tour)):
            from_city = tour[i]
            to_city = tour[(i + 1) % len(tour)]
            cost += self.distances[from_city][to_city]
        return cost

    def random_tour(self) -> List[int]:
        """Gera um tour aleatório."""
        tour = list(range(self.n_cities))
        random.shuffle(tour)
        return tour


# Criar instância de exemplo: 10 cidades aleatórias
print("\n Criando instância TSP com 10 cidades...")
np.random.seed(42)
cities = np.random.rand(10, 2) * 100
tsp = TSPInstance(cities, name="TSP-10-aleatorio")

print(f"   Nome: {tsp.name}")
print(f"   Número de cidades: {tsp.n_cities}")
print(f"   Espaço de buscas: {math.factorial(tsp.n_cities):,} permutações")

# ============================================================================
# 2. TÊMPERA SIMULADA
# ============================================================================

print("\n" + "=" * 70)
print("2. TÊMPERA SIMULADA (Simulated Annealing)")
print("=" * 70)

class SimulatedAnnealing:
    """Tempera Simulada para TSP."""

    def __init__(self, tsp: TSPInstance, initial_temp: float = 1000.0,
                 cooling_rate: float = 0.95, max_iterations: int = 1000):
        self.tsp = tsp
        self.initial_temp = initial_temp
        self.cooling_rate = cooling_rate
        self.max_iterations = max_iterations
        self.best_tour = None
        self.best_cost = float('inf')
        self.history = {"cost": [], "temp": [], "iteration": []}

    def _2opt_neighbor(self, tour: List[int]) -> List[int]:
        """Gera vizinho via 2-opt: trocar dois arcos."""
        new_tour = tour.copy()
        i, j = random.sample(range(len(tour)), 2)
        if i > j:
            i, j = j, i
        # Reverter segmento entre i e j (2-opt clássico)
        new_tour[i:j+1] = reversed(new_tour[i:j+1])
        return new_tour

    def run(self, verbose: bool = True):
        """Executa Tempera Simulada."""
        current_tour = self.tsp.random_tour()
        current_cost = self.tsp.evaluate(current_tour)

        self.best_tour = current_tour.copy()
        self.best_cost = current_cost

        temperature = self.initial_temp

        for iteration in range(self.max_iterations):
            if temperature < 1e-3:
                if verbose:
                    print(f"    Convergido em iteração {iteration}")
                break

            # Gerar vizinho
            neighbor_tour = self._2opt_neighbor(current_tour)
            neighbor_cost = self.tsp.evaluate(neighbor_tour)

            # Delta de custo (negativo = melhoria)
            delta = neighbor_cost - current_cost

            # Critério de aceitação
            if delta < 0 or random.random() < np.exp(-delta / temperature):
                current_tour = neighbor_tour
                current_cost = neighbor_cost

            # Atualizar melhor encontrado
            if current_cost < self.best_cost:
                self.best_tour = current_tour.copy()
                self.best_cost = current_cost

            # Log
            self.history["cost"].append(self.best_cost)
            self.history["temp"].append(temperature)
            self.history["iteration"].append(iteration)

            # Agenda de resfriamento
            temperature *= self.cooling_rate

            # Progress
            if (iteration + 1) % 100 == 0:
                print(f"   Iteração {iteration+1:3d}: Melhor = {self.best_cost:.2f}, Temp = {temperature:.2f}")

        if verbose:
            print(f"\n    Tempera Simulada concluída")
            print(f"   Melhor custo encontrado: {self.best_cost:.2f}")
            print(f"   Tour: {self.best_tour}")

        return self.best_tour, self.best_cost


# Executar Tempera Simulada
print("\nExecutando Tempera Simulada...")
sa = SimulatedAnnealing(tsp, initial_temp=1000.0, cooling_rate=0.95, max_iterations=500)
best_tour_sa, best_cost_sa = sa.run(verbose=True)

# ============================================================================
# 3. ALGORITMO GENÉTICO
# ============================================================================

print("\n" + "=" * 70)
print("3. ALGORITMO GENÉTICO (Genetic Algorithm)")
print("=" * 70)

class GeneticAlgorithm:
    """Algoritmo Genetico para TSP."""

    def __init__(self, tsp: TSPInstance, population_size: int = 50,
                 mutation_rate: float = 0.1, max_generations: int = 100):
        self.tsp = tsp
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.max_generations = max_generations
        self.best_tour = None
        self.best_cost = float('inf')
        self.history = {"best_cost": [], "avg_cost": [], "generation": []}

    def _fitness(self, tour: List[int]) -> float:
        """Calcula aptidão: 1 / (1 + custo)."""
        cost = self.tsp.evaluate(tour)
        return 1.0 / (1.0 + cost)

    def _pmx_crossover(self, parent1: List[int], parent2: List[int]) -> List[int]:
        """Cruzamento PMX (Partially Mapped Crossover)."""
        n = len(parent1)
        p1, p2 = random.sample(range(n), 2)
        if p1 > p2:
            p1, p2 = p2, p1

        child = [-1] * n

        # Copiar segmento de parent1
        child[p1:p2+1] = parent1[p1:p2+1]

        # Preencher resto com parent2
        for i in range(n):
            if i < p1 or i > p2:
                city = parent2[i]
                if city not in child:
                    child[i] = city

        # Resolver conflitos
        for i in range(n):
            if child[i] == -1:
                for city in range(n):
                    if city not in child:
                        child[i] = city
                        break

        return child

    def _mutate(self, tour: List[int]) -> List[int]:
        """Mutação: inversão de segmento."""
        if random.random() < self.mutation_rate:
            new_tour = tour.copy()
            i, j = random.sample(range(len(tour)), 2)
            if i > j:
                i, j = j, i
            new_tour[i:j+1] = reversed(new_tour[i:j+1])
            return new_tour
        return tour

    def run(self, verbose: bool = True):
        """Executa Algoritmo Genetico."""
        # Inicializar população
        population = [self.tsp.random_tour() for _ in range(self.population_size)]

        for generation in range(self.max_generations):
            # Avaliar aptidão
            fitnesses = [self._fitness(tour) for tour in population]
            costs = [self.tsp.evaluate(tour) for tour in population]

            # Atualizar melhor
            best_idx = np.argmin(costs)
            if costs[best_idx] < self.best_cost:
                self.best_tour = population[best_idx].copy()
                self.best_cost = costs[best_idx]

            # Log
            self.history["best_cost"].append(self.best_cost)
            self.history["avg_cost"].append(np.mean(costs))
            self.history["generation"].append(generation)

            # Progress
            if (generation + 1) % 25 == 0:
                print(f"   Geração {generation+1:3d}: Melhor = {self.best_cost:.2f}, Média = {np.mean(costs):.2f}")

            # Seleção e reprodução
            fitness_sum = sum(fitnesses)
            if fitness_sum > 0:
                probs = [f / fitness_sum for f in fitnesses]
            else:
                probs = [1.0 / len(population)] * len(population)

            new_population = []
            while len(new_population) < self.population_size:
                # Seleção por roleta
                parent1 = population[np.random.choice(len(population), p=probs)]
                parent2 = population[np.random.choice(len(population), p=probs)]

                # Cruzamento
                child = self._pmx_crossover(parent1, parent2)

                # Mutação
                child = self._mutate(child)

                new_population.append(child)

            population = new_population

        if verbose:
            print(f"\n    Algoritmo Genetico concluído")
            print(f"   Melhor custo encontrado: {self.best_cost:.2f}")
            print(f"   Tour: {self.best_tour}")

        return self.best_tour, self.best_cost


# Executar Algoritmo Genetico
print("\nExecutando Algoritmo Genetico...")
ga = GeneticAlgorithm(tsp, population_size=30, mutation_rate=0.1, max_generations=100)
best_tour_ga, best_cost_ga = ga.run(verbose=True)

# ============================================================================
# 4. COMPARAÇÃO
# ============================================================================

print("\n" + "=" * 70)
print("4. COMPARAÇÃO DE RESULTADOS")
print("=" * 70)

print(f"\n  Tempera Simulada:")
print(f"    Custo final: {best_cost_sa:.2f}")
print(f"    Iterações: {len(sa.history['cost'])}")

print(f"\n  Algoritmo Genetico:")
print(f"    Custo final: {best_cost_ga:.2f}")
print(f"    Gerações: {len(ga.history['best_cost'])}")

if best_cost_sa < best_cost_ga:
    diff = ((best_cost_ga - best_cost_sa) / best_cost_sa) * 100
    print(f"\n   Vencedor: Tempera Simulada ({diff:.1f}% melhor)")
else:
    diff = ((best_cost_sa - best_cost_ga) / best_cost_ga) * 100
    print(f"\n   Vencedor: Algoritmo Genetico ({diff:.1f}% melhor)")

# ============================================================================
# 5. SALVAR GRÁFICOS
# ============================================================================

print("\n" + "=" * 70)
print("5. GERANDO GRÁFICOS")
print("=" * 70)

# Gráfico de convergência
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

ax1 = axes[0]
ax1.plot(sa.history["iteration"], sa.history["cost"], 'b-', linewidth=2, label='Melhor custo')
ax1.set_xlabel('Iteração')
ax1.set_ylabel('Custo')
ax1.set_title(f'Tempera Simulada (Melhor: {sa.best_cost:.2f})')
ax1.grid(True, alpha=0.3)
ax1.legend()

ax2 = axes[1]
ax2.plot(ga.history["generation"], ga.history["best_cost"], 'r-', linewidth=2, label='Melhor custo')
ax2.plot(ga.history["generation"], ga.history["avg_cost"], 'r--', linewidth=1, alpha=0.6, label='Custo médio')
ax2.set_xlabel('Geração')
ax2.set_ylabel('Custo')
ax2.set_title(f'Algoritmo Genetico (Melhor: {ga.best_cost:.2f})')
ax2.grid(True, alpha=0.3)
ax2.legend()

plt.tight_layout()
filepath = "convergencia_tsp.png"
plt.savefig(filepath, dpi=100, bbox_inches='tight')
print(f"\n    Gráfico salvo: {filepath}")
plt.close()

# Gráfico dos tours
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

def plot_tour(ax, tsp, tour, title, cost):
    """Plota um tour do TSP."""
    ax.scatter(tsp.cities[:, 0], tsp.cities[:, 1], c='red', s=100, zorder=3)
    tour_points = tsp.cities[tour + [tour[0]]]
    ax.plot(tour_points[:, 0], tour_points[:, 1], 'b-', linewidth=2, zorder=1)
    for i, (x, y) in enumerate(tsp.cities):
        ax.annotate(str(i), (x, y), xytext=(5, 5), textcoords='offset points', fontsize=9)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f"{title}\n(Custo: {cost:.2f})")
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')

plot_tour(axes[0], tsp, best_tour_sa, "Tempera Simulada", best_cost_sa)
plot_tour(axes[1], tsp, best_tour_ga, "Algoritmo Genetico", best_cost_ga)

plt.tight_layout()
filepath2 = "tours_tsp.png"
plt.savefig(filepath2, dpi=100, bbox_inches='tight')
print(f"    Gráfico salvo: {filepath2}")
plt.close()

print("\n" + "=" * 70)
print("✅ EXECUÇÃO CONCLUÍDA")
print("=" * 70)
print("\nGráficos salvos em:")
print(f"  - convergencia_tsp.png")
print(f"  - tours_tsp.png")

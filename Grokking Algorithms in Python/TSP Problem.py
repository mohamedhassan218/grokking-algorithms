from operator import attrgetter
import random, sys, time, copy

"""
    Class that implement a generic graph, it creates empty dectionaries to store the edges and 
    empty set to store the vertices. It enables you to add edge between src and destination vertices.
    It can calculate the total path of the graph, generate random pathes in your graph and show it with 
    all vertices and the weight between them. 
"""
class Graph():
    def __init__(self, amount_vertices):
        self.edges = {}
        self.vertices = set()
        self.amount_vertices = amount_vertices

    def add_edge(self, src, dest, cost = 0):
        if not self.exists_edge(src, dest):
            self.edges[(src, dest)] = cost
            self.vertices.add(src)
            self.vertices.add(dest)

    def exists_edge(self, src, dest):
        return (True if (src, dest) in self.edges else False)    
    
    def show_graph(self):
        print("I'll show the graph now:\n")
        for edge in self.edges:
            print("Node %d linked with node %d during a cost of %d" % (edge[0], edge[1], self.edges[edge]))

    def get_cost_path(self, path):
        total_cost = 0
        for i in range(self.amount_vertices - 1):
            total_cost += self.edges[(path[i], path[i+1])]
            total_cost += self.edges[(path[self.amount_vertices - 1], path[0])]
            return total_cost
    
    def get_random_pathes(self, max_size):
        random_paths, list_vertices = [], list(self.vertices)
        initial_vertice = random.choice(list_vertices)
        if initial_vertice not in list_vertices:
            print("Error, initial vertice %d not exists." % initial_vertice)
            sys.exit(1)
        list_vertices.remove(initial_vertice)
        list_vertices.insert(0, initial_vertice)
        for i in range(max_size):
            temp_list = list_vertices[1:]
            random.shuffle(temp_list)
            temp_list.insert(0, initial_vertice)
            if temp_list not in random_paths:
                random_paths.append(temp_list)
        return random_paths

"""
    A subclass that inherits form the generic graph class and adds a method
    specifically for generatin a complete graph.
"""
class Complete_Graph(Graph):
    def generate(self):
        for i in range(self.amount_vertices):
            for j in range(self.amount_vertices):
                if i != j:
                    weight = random.randint(1, 10)
                    self.add_edge(i, j, weight)

"""
    This class represents a particle in a particle swarm optimization (PSO) algorithm. Each particle
    has a solution, personal best (pbest), current cost of the solution, velocity and methods to access
    these attributes.
"""
class Particle:
    def __init__(self, solution, cost):
        self.solution = solution
        self.pbest = solution
        self.cost_current_solution = cost
        self.cost_pbest_solution = cost
        self.velocity = []
    
    def set_pbest(self, new_pbest):
        self.pbest = new_pbest

    def get_pbest(self):
        return self.pbest
    
    def set_velocity(self, new_velocity):
        self.velocity = new_velocity
    
    def get_velocity(self):
        return self.velocity
    
    def set_current_solution(self, solution):
        self.solution = solution
    
    def get_current_solution(self):
        return self.solution
    
    def set_cost_pbest(self, cost):
        self.cost_pbest_solution = cost
    
    def get_cost_pbest(self):
        return self.cost_pbest_solution
    
    def set_cost_current_solution(self, cost):
        self.cost_current_solution = cost

    def get_cost_current_solution(self):
        return self.cost_current_solution
    
    def clear_velocity(self):
        del self.velocity[:]

class PSO:
    def __init__(self, graph, iterations, size_population, beta=1, alfa=1):
        self.graph = graph
        self.iterations = iterations
        self.size_population = size_population
        self.particles = []
        self.beta = beta
        self.alfa = alfa
        solutions = self.graph.get_random_pathes(self.size_population)
        if not solutions:
            print("Initial population empty. Try run the algorithm again please.")
            sys.exit(1)
        for solution in solutions:
            particle = Particle(solution=solution, cost=graph.get_cost_path(solution))
            self.particles.append(particle)
        self.size_population = len(self.particles)  
    
    def set_gbest(self, new_gbest):
        self.gbest = new_gbest
    
    def get_gbest(self):
        return self.gbest
    
    def show_particles(self):
        print("Showing particles . . . . \n")
        for particle in self.particles:
            print("pbest: %s\t|\tcost pbest: %d\t|\tcurrent solution: %s\t|\tcost current solution: %d" \
                   % (str(particle.get_pbest()), particle.get_cost_best(), str(particle.get_current_solution()), particle.get_cost_current_solution()))
        print(" ")
    
    def run(self):
        for t in range(self.iterations):
            self.gbest = min(self.particles, key=attrgetter('cost_pbest_solution'))
            for particle in self.particles:
                particle.clear_velocity()
                temp_velocity = []
                solution_gbest = copy.copy(self.gbest.get_pbest())
                solution_pbest = particle.get_pbest()[:]
                solution_particle = particle.get_current_solution()[:]
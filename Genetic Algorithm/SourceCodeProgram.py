import numpy as np
import matplotlib.pyplot as plt

X1_BOUND = [-3, 3]
X2_BOUND = [-2, 2]
N_GENERATIONS = 100
CROSS_RATE = 0.8
MUTATION_RATE = 0.1
DNA_SIZE = 10
P_SIZE = 2000

best_score = []
minX1 = []
minX2 = []

def f(x, y): return (4-2.1*x**2+x**4/3)*x**2+x*y+(-4+4*y**2)*y**2

def fitness(value): return abs(1/(value + np.min(value)))

def decodeDNAX1(pop):
    MaxSum = 0
    XMax = X1_BOUND[1]
    XMin = X1_BOUND[0]
    DNA_BoundX1 = int(DNA_SIZE/2)+1
    x1 = np.zeros([P_SIZE], dtype=float)
    for i in range(1,DNA_BoundX1):
        MaxSum = MaxSum + 2**(-i)
    for j in range(P_SIZE):
        for k in range (1, DNA_BoundX1):
            x1[j] = x1[j]+pop[j][k-1]*2**(-k)
        x1[j] = XMin+((XMax-XMin)/MaxSum)*x1[j]
    return x1 

def decodeDNAX2(pop):
    MaxSum = 0
    XMax = X2_BOUND[1]
    XMin = X2_BOUND[0]
    DNA_BoundX2 = int(DNA_SIZE/2)
    x2 = np.zeros([P_SIZE], dtype=float)
    for i in range(1, DNA_BoundX2):
        MaxSum = MaxSum + 2**(-i)
    for j in range(P_SIZE):
        for k in range (DNA_BoundX2,DNA_SIZE):
            x2[j] = x2[j]+pop[j][k]*(2**((k-(DNA_BoundX2-1))*-1))
        x2[j] = XMin + ((XMax-XMin)/MaxSum)*x2[j]
    return x2

def decode1(isi):
    Sum = 0
    XMax = X1_BOUND[1]
    XMin = X1_BOUND[0]
    DNA_BoundX1 = int(DNA_SIZE/2)+1
    Sumx1 = 0
    x1 = np.zeros(0, dtype=float)
    for i in range(1, DNA_BoundX1):
        Sum = Sum + 2**(-i)
    for k in range (1, DNA_BoundX1):
        Sumx1 = Sumx1+isi[k]*2**(-k)
    x1 = XMin+((XMax-XMin)/Sum)*Sumx1
    return x1

def decode2(isi):
    Sum = 0
    XMax = X2_BOUND[1]
    XMin = X2_BOUND[0]
    DNA_BoundX2 = int(DNA_SIZE/2)
    Sumx2 = 0
    x2 = np.zeros(0, dtype=float)
    for i in range(1, DNA_BoundX2):
        Sum = Sum + 2**(-i)
    for k in range (DNA_BoundX2, DNA_SIZE):
        Sumx2 = Sumx2+isi[k]*(2**((k-(DNA_BoundX2-1))*-1))
    x2 = XMin+((XMax-XMin)/Sum)*Sumx2
    return x2

def Selection(pop, fitness):
    i = 0
    kumfit = 0
    while i < len(pop):
        kumfit = kumfit + fitness[i]
        if (kumfit/fitness.sum()) > np.random.uniform(0,1):
            index = i
            break
        i=i+1
    return index

def Crossover(parent, pop):
    if np.random.rand() < CROSS_RATE :
        i_ = np.random.randint(0, P_SIZE, size=1)
        cross_points = np.random.randint(0, 2, size=DNA_SIZE).astype(np.bool)
        parent[cross_points] = pop[i_, cross_points]
    return parent

def Mutate(child):
    for idx in range(DNA_SIZE):
        if np.random.rand() < MUTATION_RATE:
            child[idx] = 1 if child[idx] == 0 else 0
    return child

population = np.random.randint(2, size=(P_SIZE,DNA_SIZE))
plt.ion()

print('{:<10} {:<24s} {:<24s} {:<24s} {:<22s} {:<1s}'.format("GNERASI","INDIVIDU", "NILAI X1", "NILAI X2", "NILAI FUNGSI", "NILAI FITNESS"))
print("--------------------------------------------------------------------------------------------------------------------------")
for i in range (N_GENERATIONS):
    value = f(decodeDNAX1(population), decodeDNAX2(population))

    minimalX1 = (min(decodeDNAX1(population)))
    minX1.append(minimalX1)
    minimalX2 = (min(decodeDNAX2(population)))
    minX2.append(minimalX2)

    fit_value = fitness(value)

    score = np.max(fit_value)/(DNA_SIZE*100)
    best_score.append(score)

    plt.plot(best_score)
    plt.xlabel('Generation')
    plt.ylabel('Fitness Score')
    plt.pause(0.005)

    minimalX1 = (decode1(population[np.argmax(fit_value), :]))
    minimalX2 = (decode2(population[np.argmax(fit_value), :]))

    print('{:<10s} {:<24s} {:<24s} {:<24s} {:<22s} {:<1}'.format(str((i+1)), str(population[np.argmax(fit_value), :]), str(minimalX1), str(minimalX2), str(f(minimalX1, minimalX2)), str(np.argmax(fit_value))))
    
    population = Selection(population, fit_value)
    new_population = population.copy()
    for parent in population:
        child = Crossover(parent, new_population)
        child = Mutate(child)
        parent[:] = child

plt.ioff(); plt.show()
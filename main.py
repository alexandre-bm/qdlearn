from src.qdlearn.function import FitnessScore 
from src.qdlearn.phenotype import Phenotype

def main():
    ph = Phenotype(5)
    f = lambda x : 4 + x
    fitness = FitnessScore(f)
    print(fitness(ph))

if __name__ == '__main__':
    main()
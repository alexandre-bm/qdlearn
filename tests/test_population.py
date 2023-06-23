def test_append_population(population, genotype):
    assert len(population) + 1 == len(population.append(genotype)) 

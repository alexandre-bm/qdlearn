from pytest import fixture 

from qdlearn.core.genotype import Genotype, Population 

@fixture 
def genotype():
    return Genotype([1,2,3])

@fixture
def population():
    return Population([Genotype([1,2,3]), Genotype([1,2,3])])
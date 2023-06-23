# from hypothesis import given
# from hypothesis.strategies import floats

# from qdlearn.functions.function import FitnessScore
# from qdlearn.core.phenotype import Phenotype

# @given(floats(allow_nan=False))
# def test_call_fitness_score_function(value:float) -> None:
#     phenotype = Phenotype(value)
#     f = lambda x : 4 + x
#     assert FitnessScore(f)(phenotype) == f(phenotype.value)
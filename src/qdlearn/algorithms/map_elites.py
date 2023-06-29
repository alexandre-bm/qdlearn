from ..containers.map_elites import MAPEliteRepertoire
from ..functions.function import FitnessScore, ScoringFunction



class MAPElite:

    def __init__(
        self,
        repertoire:MAPEliteRepertoire,
        scoring_function:ScoringFunction,
        fitness_function: FitnessScore
    ) -> None:
        self.repertoire = repertoire
        self.scoring_function = scoring_function
        self.fitness_function = fitness_function



    
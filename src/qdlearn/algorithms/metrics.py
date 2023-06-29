from dataclasses import dataclass, field


@dataclass
class PRIMMetrics:

    coverage: float 
    density: float 
    interpretability: float



@dataclass
class QDMetrics:

    global_performance: float 
    global_reliability: float 
    precision: float 
    coverage: float 


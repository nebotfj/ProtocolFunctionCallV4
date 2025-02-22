"""Update Derivatives Package"""

from .gmx_v2 import GMX_V2_FUNCTIONS
from .gains import GAINS_FUNCTIONS
from .vela import VELA_FUNCTIONS
from .polynomial import POLYNOMIAL_FUNCTIONS
from .synthetix import SYNTHETIX_FUNCTIONS
from .ribbon import RIBBON_FUNCTIONS
from .level import LEVEL_FUNCTIONS

DERIVATIVES_PROTOCOLS = {
    'GMX_V2': GMX_V2_FUNCTIONS,
    'GAINS': GAINS_FUNCTIONS,
    'VELA': VELA_FUNCTIONS,
    'POLYNOMIAL': POLYNOMIAL_FUNCTIONS,
    'SYNTHETIX': SYNTHETIX_FUNCTIONS,
    'RIBBON': RIBBON_FUNCTIONS,
    'LEVEL': LEVEL_FUNCTIONS
}
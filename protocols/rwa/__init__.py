"""RWA Protocols Package"""

from .centrifuge import CENTRIFUGE_FUNCTIONS
from .goldfinch import GOLDFINCH_FUNCTIONS
from .truefi import TRUEFI_FUNCTIONS

RWA_PROTOCOLS = {
    'CENTRIFUGE': CENTRIFUGE_FUNCTIONS,
    'GOLDFINCH': GOLDFINCH_FUNCTIONS,
    'TRUEFI': TRUEFI_FUNCTIONS
}
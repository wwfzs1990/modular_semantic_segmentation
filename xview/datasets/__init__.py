from .synthia import Synthia
from .raw_synthia import Synthia as SynthiaRaw
from .freiburg_forest import FreiburgForest


def get_dataset(name, config):
    if name == 'synthia':
        return Synthia(**config)
    elif name == 'raw_synthia':
        return SynthiaRaw(**config)
    elif name == 'freiburg_forest':
        return FreiburgForest(**config)
    else:
        raise UserWarning('ERROR: Dataset {} not found'.format(name))

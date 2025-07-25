"""Constants for the Marseille Luxury Objects project."""

import pandas as pd

key = pd.read_csv('data/key.csv')

DATE_GROUPINGS = {
    '1250-1299': range(1250, 1300),
    '1300-1349': range(1300, 1350),
    '1350-1399': range(1350, 1400),
    '1400-1449': range(1400, 1450),
}

FAITH_ENCODING = {
    'Christian': 0,
    'Jew': 1,
}

GENDER_ENCODING = {
    'Male': 0,
    'Female': 1,
}

FAITH_DECODING = {v: k for k, v in FAITH_ENCODING.items()}
GENDER_DECODING = {v: k for k, v in GENDER_ENCODING.items()}

DYESTUFFS = key[key['group'] == 'dyestuffs']['col_name'].tolist()
EXOTIC = key[key['group'] == 'exotic']['col_name'].tolist()
FOOD_PREPARATION = key[key['group'] == 'food_preparation']['col_name'].tolist()
HOUSEHOLD = key[key['group'] == 'household']['col_name'].tolist()
LUXURY = key[key['group'] == 'luxury']['col_name'].tolist()
WEAPONS_AND_ARMOUR = key[key['group'] == 'weapons_and_armour']['col_name'].tolist()
LINENS = key[key['group'] == 'linens']['col_name'].tolist()
CUSHIONS = key[key['subgroup'] == 'cushions']['col_name'].tolist()
PILLOWS = key[key['subgroup'] == 'pillows']['col_name'].tolist()

# P/A group columns
PA_GROUPS = [
    'dyestuffs',
    'exotic',
    'food_prep',
    'household',
    'luxury',
    'weapons',
]

# presence counts for groups
VAR_GROUPS = [
    'var_dyestuffs',
    'var_exotic',
    'var_food_prep',
    'var_household',
    'var_luxury',
    'var_weapons',
]

# P/A objects but weapons, linens, cushions, and pillows remain grouped
PA_OBJECTS = [
    'candelabra',
    'lamps',
    'cushions',
    'pillows',
    'weapons',
    'linens',
    *DYESTUFFS,
    *EXOTIC,
    *FOOD_PREPARATION,
    *LUXURY,
]

# P/A objects
PA_FULL = [
    *DYESTUFFS,
    *EXOTIC,
    *FOOD_PREPARATION,
    *HOUSEHOLD,
    *LUXURY,
    *WEAPONS_AND_ARMOUR,
]

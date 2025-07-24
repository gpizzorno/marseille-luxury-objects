"""Constants for the Marseille Luxury Objects project."""

DYESTUFF_COLS = [
    'green_dyestuff',
    'ruby_red_dyestuff',
    'black_dyestuff',
    'purple_dyestuff',
    'yellow_dyestuff',
]

WEAPONS_AND_ARMOR_COLS = [
    'arcus',
    'ballista',
    'bassinetus',
    'bloquerius',
    'brassaletus',
    'caliga',
    'camallia',
    'camberia',
    'capellus',
    'carcays',
    'chavarina',
    'cirotheca',
    'clipeus',
    'curassia',
    'elma',
    'ensis',
    'gantelletus',
    'gladius',
    'gorjerium',
    'lanceus',
    'lorica',
    'manutecha',
    'massa',
    'panseria',
    'pavesius',
    'plata',
    'rudella',
    'scutum',
    'servelleria',
    'sotulares_ferreos',
    'spontonum',
    'targia',
]

CUSHIONS_COLS = [
    'pulvinar',
    'coysin',
    'auricula',
    'fluna',
    'transverser',
]

EXOTIC_COLS = [
    'silk',
    'sendal',
    'alexandria',
    'damascus',
    'amber',
]

LINEN_COLS = ['tablecloths', 'bedsheets', 'tunics']

OTHER_OBJECTS_COLS = [
    'cushions',
    'mortars',
    'dough_troughs',
    'candelabra',
    'spits',
    'lamps',
    'decorative_gold',
    'alembics',
]

OBJECT_COLS = [
    *OTHER_OBJECTS_COLS,
    *DYESTUFF_COLS,
    *EXOTIC_COLS,
    *LINEN_COLS,
    'linens',
    'weapons',
]

FULL_OBJECT_COLS = [
    *OBJECT_COLS,
    *WEAPONS_AND_ARMOR_COLS,
    *CUSHIONS_COLS,
    'var_weapons',
    'var_exotic',
    'var_dyestuff',
]

DATE_GROUPINGS = {
    '1250-1299': range(1250, 1300),
    '1300-1349': range(1300, 1350),
    '1350-1399': range(1350, 1400),
    '1400-1449': range(1400, 1450),
}

FAITH_ENCODINGS = {
    'Christian': 0,
    'Jew': 1,
}

GENDER_ENCODINGS = {
    'Male': 0,
    'Female': 1,
}

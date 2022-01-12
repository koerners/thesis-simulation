import random

from palettable.cartocolors.qualitative import Prism_10
from palettable.cartocolors.qualitative import Vivid_10

# https://jiffyclub.github.io/palettable/
color_pallet = Prism_10.mpl_colors

COLOR_MAP = {
    # Agents
    "GroupAgent": color_pallet[1],
    "CultureAgent": color_pallet[2],
    "AltruismAgent": color_pallet[3],
    "UnconditionalAgent": color_pallet[4],
    "FakeGreenBeardAgent": color_pallet[5],
    "GreenBeardAgent": color_pallet[6],
    "ReputationAgent": color_pallet[7],
    "EatingAgent": color_pallet[8],
    "KinSelectionAgent": color_pallet[3],
    # Statistics
    "below_median": color_pallet[2],
    "above_median": color_pallet[-1],
    "average": color_pallet[5],
    "avg_fitness_alt": color_pallet[2],
    "avg_fitness_non_alt": color_pallet[-1],
    # Numbers
    "0": color_pallet[0],
    "1": color_pallet[1],
    "2": color_pallet[2],
    "3": color_pallet[3],
    "4": color_pallet[4],
    "5": color_pallet[6],
    "6": color_pallet[7],
    "7": color_pallet[8],
    "8": color_pallet[9],
    "25": color_pallet[2],
    "60": color_pallet[-1],
    # Alphabet
    "A": color_pallet[0],
    "B": color_pallet[1],
    "C": color_pallet[2],
    "D": color_pallet[3],
    "E": color_pallet[4],
    "F": color_pallet[6],
    "G": color_pallet[7],
    "H": color_pallet[8],
    "I": color_pallet[9],
    # Boolean
    "True": color_pallet[2],
    "False": color_pallet[-1],
}


def get_color_by_value(value):
    return COLOR_MAP.get(str(value), random.choice(Vivid_10.mpl_colors))

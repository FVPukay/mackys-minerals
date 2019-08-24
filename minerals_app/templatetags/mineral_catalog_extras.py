from collections import OrderedDict
from django import template
from minerals_app.models import Mineral

import json

register = template.Library()

occurences = OrderedDict({
        'group': 0,
        'formula': 0,
        'category': 0,
        'strunz_classification': 0,
        'crystal_system': 0,
        'unit_cell': 0,
        'color': 0,
        'crystal_symmetry': 0,
        'cleavage': 0,
        'mohs_scale_hardness': 0,
        'luster': 0,
        'streak': 0,
        'diaphaneity': 0,
        'optical_properties': 0,
        'refractive_index': 0,
        'crystal_habit': 0,
        'specific_gravity': 0,
    })

no_underscore = {
    'strunz_classification': 'strunz classification',
    'crystal_system': 'crystal system',
    'unit_cell': 'unit cell',
    'crystal_symmetry': 'crystal symmetry',
    'mohs_scale_hardness': 'mohs scale hardness',
    'optical_properties': 'optical properties',
    'refractive_index': 'refractive index',
    'crystal_habit': 'crystal habit',
    'specific_gravity': 'specific gravity',
    }


def get_occurences(occurences):
    """Get the number of times each attribute occurs in the JSON file"""
    with open('minerals.json') as file:
        file = json.loads(file.read())

    mineral_name_list = []

    for mineral in file:
        if mineral['name'] not in mineral_name_list:
            mineral_name_list.append(mineral['name'])
            for key in mineral.keys():
                if key in occurences:
                    occurences[str(key)] += 1

    return occurences


def remove_underscores(occurences):
    """Remove underscores from the attribute names"""
    occurences_copy = occurences.copy()

    for key in occurences_copy.keys():
        if key in no_underscore.keys():
            occurences[no_underscore[key]] = occurences.pop(key)

    return occurences


def sort_occurences(occurences):
    """Sort attributes by occurence in descending order"""
    occurences_sorted = sorted(occurences.items(), key=lambda x:x[1])
    attr_list = []  # list of tuples ('group', 874), ('category', 874), ...
    for item in occurences_sorted:
        attr_list.append(item)

    attr_list_desc = attr_list[::-1]

    return attr_list_desc


@register.filter('mineral_attributes')
def mineral_attributes(pk):
    """Generate an ordered dictionary consisting of key-value
    pairs so that the most commonly occuring attributes/values come first
    when they are displayed in the mineral_details page for a specific
    mineral.
    """
    mineral = Mineral.objects.get(id=pk)
    all_occurences = get_occurences(occurences)
    all_occurences = remove_underscores(all_occurences)
    attr_list = sort_occurences(all_occurences)
    mineral_dict = OrderedDict({
        f"{attr_list[0][0]}": mineral.category,
        f"{attr_list[1][0]}": mineral.group,
        f"{attr_list[2][0]}": mineral.formula,
        f"{attr_list[3][0]}": mineral.strunz_classification,
        f"{attr_list[4][0]}": mineral.crystal_system,
        f"{attr_list[5][0]}": mineral.mohs_scale_hardness,
        f"{attr_list[6][0]}": mineral.luster,
        f"{attr_list[7][0]}": mineral.color,
        f"{attr_list[8][0]}": mineral.specific_gravity,
        f"{attr_list[9][0]}": mineral.cleavage,
        f"{attr_list[10][0]}": mineral.diaphaneity,
        f"{attr_list[11][0]}": mineral.crystal_habit,
        f"{attr_list[12][0]}": mineral.streak,
        f"{attr_list[13][0]}": mineral.optical_properties,
        f"{attr_list[14][0]}": mineral.refractive_index,
        f"{attr_list[15][0]}": mineral.crystal_symmetry,
        f"{attr_list[16][0]}": mineral.unit_cell,
    })

    return mineral_dict

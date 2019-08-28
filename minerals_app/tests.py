from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.test import TestCase
from minerals_app.models import Mineral
from minerals_app.templatetags import mineral_catalog_extras

import json
import random


def populate_t_database():
    """Populate the test database using the JSON file"""
    with open('minerals.json') as file:
        file = json.loads(file.read())

    for mineral in file:
        mineral_entry = Mineral.objects.get_or_create(**mineral)


def random_pk():
    return int(random.random() * int(Mineral.objects.count()) + 1)


class MineralModelTests(TestCase):
    def setUp(self):
        populate_t_database()
        self.minerals = Mineral.objects.all()
        self.mineral = get_object_or_404(Mineral, name=u'\u00c5kermanite')

    def test_mineral_creation(self):
        self.assertIn(self.mineral, self.minerals)

    def test_dunder_str(self):
        self.assertEqual(self.mineral.__str__(), self.mineral.name)


class MineralViewsTests(TestCase):
    def setUp(self):
        populate_t_database()
        self.mineral_1 = get_object_or_404(Mineral, name='Baryte (barite)')
        self.mineral_2 = get_object_or_404(Mineral, name='Ferrierite')

    def test_index_view(self):
        response = self.client.get(reverse('minerals_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.mineral_1, response.context['minerals'])
        self.assertIn(self.mineral_2, response.context['minerals'])
        self.assertTemplateUsed(response, 'minerals_app/index.html')
        self.assertContains(response, "Mackey's Minerals")
        self.assertContains(response, "Show random mineral")

    def test_mineral_details_view(self):
        response = self.client.get(reverse(
            'mineral:detail', kwargs={'pk': self.mineral_2.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.mineral_2, response.context['mineral'])
        self.assertTemplateUsed(response, 'minerals_app/mineral_details.html')
        self.assertContains(response, "Mackey's Minerals")
        self.assertContains(response, "Show random mineral")


class RandomMineralTests(TestCase):
    def setUp(self):
        populate_t_database()
        self.rand_pk = random_pk()
        self.mineral = get_object_or_404(Mineral, id=self.rand_pk)

    def test_show_random_mineral(self):
        response = self.client.get(reverse(
            'mineral:detail', kwargs={'pk': self.rand_pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.mineral, response.context['mineral'])


class MineralAttributesFilterTests(TestCase):
    def setUp(self):
        populate_t_database()
        self.rand_pk = random_pk()
        self.min_attrs = mineral_catalog_extras.mineral_attributes(
            self.rand_pk
        )

    def test_mineral_attributes(self):
        response = self.client.get(reverse(
            'mineral:detail', kwargs={'pk': self.rand_pk})
        )

        self.assertEqual(
            self.min_attrs['category'],
            response.context['mineral'].category
        )
        self.assertEqual(
            self.min_attrs['group'],
            response.context['mineral'].group
        )
        self.assertEqual(
            self.min_attrs['formula'],
            response.context['mineral'].formula
        )
        self.assertEqual(
            self.min_attrs['strunz classification'],
            response.context['mineral'].strunz_classification
        )
        self.assertEqual(
            self.min_attrs['crystal system'],
            response.context['mineral'].crystal_system
        )
        self.assertEqual(
            self.min_attrs['mohs scale hardness'],
            response.context['mineral'].mohs_scale_hardness
        )
        self.assertEqual(
            self.min_attrs['luster'],
            response.context['mineral'].luster
        )
        self.assertEqual(
            self.min_attrs['color'],
            response.context['mineral'].color
        )
        self.assertEqual(
            self.min_attrs['specific gravity'],
            response.context['mineral'].specific_gravity
        )
        self.assertEqual(
            self.min_attrs['cleavage'],
            response.context['mineral'].cleavage
        )
        self.assertEqual(
            self.min_attrs['diaphaneity'],
            response.context['mineral'].diaphaneity
        )
        self.assertEqual(
            self.min_attrs['crystal habit'],
            response.context['mineral'].crystal_habit
        )
        self.assertEqual(
            self.min_attrs['streak'],
            response.context['mineral'].streak
        )
        self.assertEqual(
            self.min_attrs['optical properties'],
            response.context['mineral'].optical_properties
        )
        self.assertEqual(
            self.min_attrs['refractive index'],
            response.context['mineral'].refractive_index
        )
        self.assertEqual(
            self.min_attrs['crystal symmetry'],
            response.context['mineral'].crystal_symmetry
        )
        self.assertEqual(
            self.min_attrs['unit cell'],
            response.context['mineral'].unit_cell
        )

import json
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase

from rest_framework import status

from api.factories import DataFieldFactory, RiskTypeFactory
from api.models import FIELD_TYPE


class RiskTypeTests(APITestCase):
    def setUp(self):
        d1 = DataFieldFactory(is_required=True, field_type=FIELD_TYPE.text)
        d2 = DataFieldFactory(is_required=False, field_type=FIELD_TYPE.number)
        d3 = DataFieldFactory(is_required=True, field_type=FIELD_TYPE.date)
        d4 = DataFieldFactory(is_required=True, field_type=FIELD_TYPE.enum,
                              enum_values=json.dumps([{'key': 'automobiles', 'value': 'Automobiles'},
                                                      {'key': 'houses', 'value': 'Houses'}]))

        RiskTypeFactory(id=1, fields=[d1, d2, d3, d4])
        RiskTypeFactory(id=2, fields=[d1, d4])

    def test_get_all_risk_types(self):
        url = reverse('risktype-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    def test_get_one_risk_type(self):
        url = reverse('risktype-detail', kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        risk_type = response.json()
        self.assertEqual(risk_type['id'], 1)

    def test_get_risk_type_not_found(self):
        url = reverse('risktype-detail', kwargs={'pk': 3})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_risk_type_field(self):
        url = reverse('risktype-detail', kwargs={'pk': 1})
        response = self.client.get(url, format='json')

        risk_type = response.json()
        self.assertEqual(len(risk_type['fields']), 4)
        self.assertEqual(risk_type['fields'][0]['is_required'], True)
        self.assertEqual(risk_type['fields'][1]['is_required'], False)
        self.assertEqual(risk_type['fields'][2]['is_required'], True)
        self.assertEqual(risk_type['fields'][3]['is_required'], True)

        self.assertEqual(risk_type['fields'][0]['field_type'], FIELD_TYPE.text)
        self.assertEqual(risk_type['fields'][1]['field_type'], FIELD_TYPE.number)
        self.assertEqual(risk_type['fields'][2]['field_type'], FIELD_TYPE.date)
        self.assertEqual(risk_type['fields'][3]['field_type'], FIELD_TYPE.enum)

    def test_get_risk_type_enum_field(self):
        url = reverse('risktype-detail', kwargs={'pk': 1})
        response = self.client.get(url, format='json')

        risk_type = response.json()
        self.assertEqual(len(risk_type['fields']), 4)

        self.assertEqual(len(risk_type['fields'][3]['read_enum_values'].keys()), 2)
        self.assertEqual(risk_type['fields'][3]['read_enum_values']['automobiles'], 'Automobiles')
        self.assertEqual(risk_type['fields'][3]['read_enum_values']['houses'], 'Houses')

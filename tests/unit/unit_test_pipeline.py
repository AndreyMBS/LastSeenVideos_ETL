import unittest
import json
import jsonschema 
from jsonschema import validate
from pipeline import Pipeline
import pandas as pd
from datetime import datetime

class Test_Pipeline(unittest.TestCase):

    def test_dataTransformation_unit_test(self):
        # Define the test DataFrame with known input data
        test_df = pd.DataFrame({'publishTime':  ['2022-01-01T20:00:00Z', 
                                                    '2022-02-02T20:00:00Z'],
                                'title':        ['ANDREINA BRAVO 🇪🇨 RECIBE sus #3 PREMIOS CHARTS ECUADOR y Lo Celebró de Ésta Form ma 😱🔥', 
                                                    'Castigos del fútbol tico: ¿Sanciones ejemplares ó muy poco drásticas? ✍🏼❌'],
                                'description':  ['SALVE RAPEIZE TUDO BEM MEU INSTA @celio_gabriel_yt   patrocinador @renatongarcia.', 
                                                    'Telegram: https://t.me/Elguardiancr Nota Completa en www.elguardian.cr #elguardiancr #wwwelguardiancr #analisis #política ...']})
        
        # Call the dataTransformation function on the test DataFrame
        Pipeline.dataTransformation(test_df)

        # Assertions to check if the expected transformations are applied
        # Asserts for publishTime column
        self.assertIsInstance(test_df['publishTime'][0], datetime)  # Asserts that the 'publishTime' column is converted to pd.Timestamp
        self.assertIsNone(test_df['publishTime'].dt.tz)  # Asserts that the 'publishTime' column has no timezone information

        # Asserts for title column
        self.assertIn('title', test_df.columns.tolist())  # Asserts that the 'title' column is still present
        self.assertEqual(test_df['title'][0], 'andreina bravo recibe sus premios charts ecuador y lo celebro de esta form ma')  # Asserts that the 'title' column is not modified

        # Asserts for description column
        self.assertIn('description', test_df.columns.tolist())  # Asserts that the 'description' column is still present
        self.assertFalse(test_df['description'].str.contains(r'[^A-Za-z ]').any())  # Asserts that the 'description' column has no non-alphabetic characters

        # Additional assertions for timezone localization
        self.assertIsNone(test_df['publishTime'].dt.tz_localize(None).dt.tz)  # Asserts that the 'publishTime' column is timezone-naive after localization

if __name__ == '__main__':
    unittest.main()
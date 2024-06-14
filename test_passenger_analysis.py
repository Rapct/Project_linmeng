import unittest
import pandas as pd
from passenger_analysis import load_data, clean_data, calculate_average_age, find_loyalty_members

class TestPassengerAnalysis(unittest.TestCase):
    def setUp(self):
        self.file_path = 'passengers.csv'
        self.df = load_data(self.file_path)
        self.cleaned_df = clean_data(self.df)
    
    def test_load_data(self):
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertEqual(self.df.shape[1], 6)
    
    def test_clean_data(self):
        self.assertEqual(self.cleaned_df['Birthdate'].dtype, 'datetime64[ns]')
        self.assertEqual(self.cleaned_df['LoyaltyMember'].dtype, bool)
    
    def test_calculate_average_age(self):
        travel_class = 'Economy'
        loyalty_members = calculate_average_age(self.cleaned_df, travel_class)
        self.assertIsInstance(loyalty_members, list)
        self.assertTrue(all(isinstance(name, str) for name in loyalty_members))
    
    def test_find_loyalty_members(self):
        years = 50
        experienced_members = find_loyalty_members(self.cleaned_df, years)
        self.assertIsInstance(experienced_members, list)
        self.assertTrue(all(isinstance(name, str) for name in experienced_members))

if __name__ == '__main__':
    unittest.main()
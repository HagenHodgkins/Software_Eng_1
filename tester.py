import unittest
import converter
import pandas as pd

csv = pd.read_csv('input.csv')

class testing(unittest.TestCase):
	def test_conversion(self):
		self.assertEqual(converter.csv_2_xml(csv), '''<Department>
	<Record>
		<StudentID="0    970100
1    970101
Name: StudentID, dtype: int64">
		<FirstName>0      Tom
1    David
Name: FirstName, dtype: object</FirstName>
		<LastName>0         Smith
1    Washington
Name: LastName, dtype: object</LastName>
	</Record>
</Department>
''' );
 
if __name__ == '__main__':
	unittest.main()
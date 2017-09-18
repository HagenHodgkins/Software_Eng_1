import pandas as pd

csv = pd.read_csv('input.csv')#opens the csv file
#------------------------------------------------------------------
def csv_2_xml(csv): # converts the csv file to an xml format
	return """<Department>
	<Record>
		<StudentID="%s">
		<FirstName>%s</FirstName>
		<LastName>%s</LastName>
	</Record>
</Department>
""" % (csv.StudentID, csv.FirstName, csv.LastName)
#------------------------------------------------------------------
xml = open('output.xml', 'w') # open/create an xml file called output
xml.write(''.join(csv.apply(csv_2_xml, axis=1))) # write the conversion to the new xml file

if __name__ == "__main__":
	print csv_2_xml(csv)


#edit for v2 commit
#edit for v3 commit

#edit for v5 commit after merger with branch_2

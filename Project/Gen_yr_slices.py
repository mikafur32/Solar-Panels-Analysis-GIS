'''
Selects all points from LBNL_file_GeocodeAddresses that fall within a given year range.
The output is a new feature class for each year.
complex_selector_ is the SQL expression that selects the points within the given year range.
The SQL expression is based on the field 'USER_installation_date' which is a time field in the LBNL_file_GeocodeAddresses feature class.

Author: Mikey Sison

'''

import arcpy
arcpy.env.workspace = "C:/Users/Perso/Desktop/Tulane U/Junior Year/Semester 6/EENS 4030- Advanced GIS/FINAL PROJECT/Project/New Folder/Default.gdb"
arcpy.env.overwriteOutput = True


LBNL_path = "LBNL_file_GeocodeAddresses" 

delim_field = arcpy.AddFieldDelimiters(LBNL_path, "USER_installation_date")

for yr in range(1998, 2020):
    outfc = "yr_"+ str(yr)    
    delim_field = arcpy.AddFieldDelimiters(LBNL_path, "USER_installation_date")
    complex_selector_ = '{delim_field} >= timestamp \'{year}-01-01 00:00:00\' And {delim_field} <= timestamp \'{year}-12-31 00:00:00\''.format(delim_field= delim_field, year= str(yr))
    
    arcpy.Select_analysis(LBNL_path, outfc, complex_selector_)



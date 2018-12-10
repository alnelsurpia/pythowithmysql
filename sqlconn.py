import mysql.connector
import terminaltables
from terminaltables import AsciiTable

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="asdlkj",
    database="dbpos2a"
)

header = ('Itemcode', 'Description','Price') #--> format and static value of header of the final_table
final_table = list()  #--> we make the final_table as a list in order to allow to be modified

mycursor = mydb.cursor()
# SQL statement to get the 3 field in the database
sql = "SELECT itemcode,description,perpiece FROM tblitemlist"
mycursor.execute(sql)

myresult = mycursor.fetchall()

#final_table is my given name for the final table
final_table.append(header) #--> to put the header to the final_table


for result in myresult:
    tcontent = (result[0], result[1],result[2])  #--> format and Dynamic value of content of the final_table
    final_table.append(tcontent)  #--> to put the Content to the final_table

final_table = AsciiTable(final_table)  #--> Print the final output of the final_table
print(final_table.table)

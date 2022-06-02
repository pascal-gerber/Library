#CSV files short for Comma-separated values
#and is a file type "extension".
#CSV files can be opened on editor to simply write text or/and open them on Excel
with open("list of peoples.csv", "w") as workers:
    #CSV files can be edited in multiples different ways
    workers.write("""id;name;salary;start_date;dept
1;Rick;623.3;2012-01-01;IT
2;Dan;515.2;2013-09-23;Operations
3;Michelle;611;2014-11-15;IT
4;Ryan;729;2014-05-11;HR
5;Gary;843.25;2015-03-27;Finance
6;Nina;578;2013-05-21;IT
7;Simon;632.8;2013-07-30;Operations
8;Guru;722.5;2014-06-17;Finance""")
    #either \n or going on the next line will go on the next line
    #the sign ; is for going one field to the right.

with open("list of peoples.csv", "r") as show:
    #now it will simply show up as a CSV but it is editable on Excel too.
    print(show.read())
    #its a simple text, but opening it is different

#for opening the file on excel directly you can use the OS module
import os
os.startfile("list of peoples.csv")
#of course there are other ways, but on my opinion, it is the best

#there are websites ive used as source, if you wanna get deeper into the subject
#use this
#https://www.tutorialspoint.com/r/r_csv_files.htm

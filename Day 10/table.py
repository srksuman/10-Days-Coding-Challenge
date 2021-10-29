from prettytable import PrettyTable as pt
from prettytable.prettytable import PrettyTable

#column
table = PrettyTable(['S.N','Full Name','Position','Salary'])
#adding rows
table.add_row(['1','Bill Gates','Founder Microsoft','$1000'])
table.add_row(['2','Stev Jobs','Founder Apple','$1200'])
table.add_row(['3','Larry Page','Founder Google','$1100'])
table.add_row(['4','Mark Zuckerberg','Founder Meta','$1300'])
print(table)

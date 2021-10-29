# # PrettyTable 
Install via pip:

    python -m pip install -U prettytable
Let's suppose we have a shiny new PrettyTable:

    from prettytable import PrettyTable
    table = PrettyTable()
and you want to put some data into it.
#### Row by row

    table.fields_name = ["S.N","Full Name","Position","Salary"]
    table.add_row(['1','Bill Gates','Founder Microsoft','$1000'])
    table.add_row(['2','Stev Jobs','Founder Apple','$1200'])
    table.add_row(['3','Larry Page','Founder Google','$1100'])
    table.add_row(['4','Mark Zuckerberg','Founder Meta','$1300'])
# Output
![enter image description here](https://i.imgur.com/ZAbD5GW.png)
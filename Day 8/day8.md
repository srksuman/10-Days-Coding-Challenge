# Hack Github Contribution Graph With Just 11 Lines Of Python Code
## Import os module
    import os
### Recursive Functions
* Termination point or base case "days < 1"
* Function call itself until it reaches "days <1"
## Create function 

    def  contributions(days):
	    if  days < 1:
		    return  os.system("git push")
	    else:
		    with  open("file.txt",'a') as  file:
			    file.write('Writing something\n')
		    os.system("git add file.txt")
		    os.system(f'git commit --date="{days} days ago" -m "commit_message"')
		    return  days*contributions(days-1)
* --date in git --> 	Helps to specify the author date that git attaches to the commit
* How you can:-
--date="YYYY-MM-DD HH:MM:SS"
--date= "120 days ago"
## Calling Function 

    contributions(665)

import os
def contributions(days):
    if days < 1:
	    return os.system("git push")
    else:
        with open("file.txt",'a') as file:
            file.write('Writing something\n')
        os.system("git add file.txt")
        os.system(f'git commit --date="{days} days ago" -m "commit_message"')
        return days*contributions(days-1)
contributions(365)
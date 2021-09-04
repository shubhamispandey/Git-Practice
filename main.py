
import os
import random

def oddEven(n):
    if (n % 2) == 0:
        return 1
    else:
        return 0


def make_commit(days: int):
    if days<1:
        # push
        return os.system('git push')
    else:
        if oddEven(random.randint(0,4)) == 1:

            dates = f'{days} days ago'

            with open('bot.txt', 'a') as file:
                file.write(f'{dates}\n')
            
            # staging
            os.system('git add bot.txt')
            # commit
            os.system('git commit --date="'+dates+'" -m "First Commit"')

        return days*make_commit(days-1)

make_commit(365)
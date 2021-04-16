import os
import shutil
import time

time = time.time()

path = input('Pleae enter the Path\n')

if os.path.exists(path):
    walk = os.walk(path)
    fileJoin = os.path.join(path)

    ctime = os.stat(path).st_ctime

    if time > ctime:
        if os.path.isfile(path):
            os.remove(path)
            print('\nFile Removed...')

        else:
            shutil.rmtree(path)
            print('\nFolder Removed...')

else:
    print('\nLocation of the file is not valid')

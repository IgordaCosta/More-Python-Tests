import os
import path

def ChangeStartupDirectory(Folder,midFolder='Documents'):
        
        home = os.path.expanduser('~')

        location = os.path.join(home, 'Documents', Folder)
        
        if not os.path.exists(location):
            os.makedirs(location)

        else:

            pass
         
        os.chdir(location)
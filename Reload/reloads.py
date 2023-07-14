# import simple
# import simple
# import simple

# import importlib
# import simple
# importlib.reload(simple)
# importlib.reload(simple)
# importlib.reload(simple)

import importlib
import filechanges
def changes():
    try:
        importlib.reload(filechanges)
        filechanges.print_changes()
    except:
        pass

for i in range(5):
    changes()
    input("Hit enter to reload...")
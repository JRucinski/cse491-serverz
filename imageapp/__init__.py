#__init__.py is the top level file in a Python package.

from quixote.publish import Publisher

# this imports the class RootDirectory from the file 'root.py'
from .root import RootDirectory
from . import html, image

#this imports the sqlite3 commands
import sqlite3

def create_publisher():
     p = Publisher(RootDirectory(), display_exceptions='plain')
     p.is_thread_safe = True
     return p
 
def setup():                            # stuff that should be run once.
     db = sqlite3.connect('images.sqlite')
     db.execute('CREATE TABLE IF NOT EXISTS image_store (i INTEGER PRIMARY KEY, image BLOB)');
     db.commit()
     db.close()
     print 'Creating data table'
    
     html.init_templates()

     some_data = open('imageapp/dice.png', 'rb').read()
    # image.add_image(some_data, 'png')
    

def teardown():                         # stuff that should be run once.
    pass


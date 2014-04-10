# image handling API
import sqlite3
images = {}

def add_image(data, filetype):
    db = sqlite3.connect('images.sqlite')
    db.text_factory = bytes
    
    #r = open(name,'rb').read()
    db.execute('INSERT INTO image_store (image) VALUES (?)', (data,))
    db.commit()

def get_image(num):
    
    return images[num]

def get_latest_image():
    # connect to database
    db = sqlite3.connect('images.sqlite')

    # configure to retrieve bytes, not text
    db.text_factory = bytes

    # get a query handle (or "cursor")
    c = db.cursor()

    # select all of the images
    c.execute('SELECT i, image FROM image_store ORDER BY i DESC LIMIT 1')
    #          ^      ^             ^           ^
    #          ^      ^             ^           ^----- details of ordering/limits
    #          ^      ^             ^
    #          ^      ^             ^--- table from which you want to extract
    #          ^      ^
    #          ^      ^---- choose the columns that you want to extract
    #          ^
    #          ^----- pick zero or more rows from the database


    # grab the first result (this will fail if no results!)
    i, image = c.fetchone() 
    return image

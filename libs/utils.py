import os


# Metodo che salva un'immagine (img) nel target fornito con il nome di new_filename
def saveImg(img, target, new_filename):
    destination = "/".join([target, new_filename])
    if os.path.isfile(destination):
        os.remove(destination)
    img.save(destination)

# get dell'immagine
def getSourceImg(target, filename):
    source = "/".join([target, filename])
    return source

# DEPRECATED 
# il base64 ha dei caratteri strani all'inizio. quindi lo devo pulire
def cleanbase64(str):
    l = list(str)  # convert to list
    # del(l[0:2]) # si deve eliminare b' non so perché lo ritorni..
    # del(l[-1]) # .. ed anche un " ' " finale

    #elimino i primi caratteri che sarebbero base:64 ecc...
    del(l[0:23])

    s = "".join(l)  # convert back to string
    

    return s
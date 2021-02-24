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
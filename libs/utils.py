import os
import re, time, base64

# get dell'immagine
def getSourceImg(target, filename):
    source = "/".join([target, filename])
    return source


# da una stringa in base64 ritorna i byte da cui poi sarà possibile ricostruire un'img..
def getI420FromBase64(codec):
    base64_data = re.sub('^data:image/.+;base64,', '', codec)
    byte_data = base64.b64decode(base64_data)

    return byte_data

    # per ritornare direttamente l'immagine...
    # image_data = BytesIO(byte_data)
    # img = Image.open(image_data)
    # t = time.time() # ????
    # return img

# *******************************
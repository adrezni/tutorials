from io import BytesIO
import base64


class ImageRead:
    """
    Reads an image into a BytesIO buffer, encodes the buffer contents into base64 and converts the
    base64 from a byte array into a str array
    """
    def readImage(self):
        with open("static/pixelated-number_3.png", "rb") as fh:
            buffer = BytesIO(fh.read())
        buffContents = buffer.getvalue() # Get contents of buffer as byte object of UNICODE
        buffEncoded = base64.b64encode(buffContents) # Convert byte object UNICODE to byte object ASCII
        buffStr = buffEncoded.decode('ascii') # Convert byte object ASCII to str object ASCII
        return buffStr

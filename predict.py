import io
import cv2
import requests
from PIL import Image
from requests_toolbelt.multipart.encoder import MultipartEncoder
import image_slicer
import os


def predict_image(impath):
    imname = impath.split('/')[-1]
    image = cv2.imread(impath)
    image = cv2.resize(image,(900,900))
    cv2.imwrite(impath,image)
    image_slicer.slice(impath, 9)
    counter = 0
    for i in os.listdir('images'):
        if '.png' in i and i!=imname:
            img = cv2.imread("images/"+i)
            image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            pilImage = Image.fromarray(image)

            # Convert to JPEG Buffer
            buffered = io.BytesIO()
            pilImage.save(buffered, quality=100, format="JPEG")

            # Build multipart form and post request
            m = MultipartEncoder(fields={'file': ("imageToUpload", buffered.getvalue(), "image/jpeg")})

            response = requests.post("https://classify.roboflow.com/oil-spill-9x2kp/1?api_key=lI0DaQXnzMfaJyRorPKc", data=m, headers={'Content-Type': m.content_type})

            if response.json()['top']=="oilspill":
                counter+=1
            else:
                pass
            os.remove("images/"+i)

    print(counter)
    if counter==0:
        return "<h3>There is no oil spill</h3>"
    elif counter>6:
        return "<h3>There are severe oil spills</h3>"
    else:
        return "<h3>Oil spill found</h3>"

import os, io
from google.cloud import vision_v1
import pandas as pd

request = vision_v1.GetProductSetRequest(name="name")

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'###Directory to Google Cloud Key#####'

client = vision_v1.ImageAnnotatorClient()

file_name = "offenders1.png"
image_path = f'.\Images\{file_name}'

with io.open(image_path, "rb") as image_file:
    content = image_file.read()

image = vision_v1.types.Image(content=content)
response = client.face_detection(image=image)
faceAnnotations = response.face_annotations

print("Faces Borders:")
for face in faceAnnotations:
    face_vertices = ['({0},{1})'.format(vertex.x, vertex.y) for vertex in face.bounding_poly.vertices]
    print("Face Bound: {0}".format(",".join(face_vertices)))
    print("")

question = input("Do you want to see all the details? (y/N)\n")
question.lower()
if question == "y":
    print(faceAnnotations)

#
# print("Faces Borders:")
# for face in faceAnnotations:
#     for position in face.landmarks:
#         landmark_nose_tip = ['({0},{1},{2})'.format(position.x, position.y, position.z)]
#     # print("Face Bound: {0}".format(",".join(face_vertices)))
#     # print("")

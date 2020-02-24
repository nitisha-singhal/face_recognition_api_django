from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import face_recognition
import cv2
from .serializers import PersonSerializer
from .models import Person
import base64
import numpy as np
from PIL import Image


def convert(image):
    im = Image.fromarray(image)
    im.save('hello.jpg')
    image_file = open('hello.jpg', 'rb')
    base64string = base64.b64encode(image_file.read())
    return base64string


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        person_serializer = PersonSerializer(data=request.data)

        if person_serializer.is_valid():

            person_match = person_serializer.save()
            person_match = face_recognition.load_image_file(person_match.image)
            face_locations = face_recognition.face_locations(person_match)
            face_encodings = face_recognition.face_encodings(person_match, face_locations)
            face_names = []
            known_face_encodings = []
            known_face_names = []
            for i in Person.objects.all():
                known_face_encodings.append(
                    face_recognition.face_encodings(face_recognition.load_image_file(i.image))[0])
                known_face_names.append(i.name)
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Draw a box around the face
                cv2.rectangle(person_match, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(person_match, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(person_match, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            return Response({'image': convert(image=person_match)}, status=status.HTTP_201_CREATED)

        else:
            return Response(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

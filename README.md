# face_recognition_api_django
An implementation of face recognition API with a model in django

# Running instructions 
Install all requirements by pip install -r requirements.txt<br>
Run python manage.py migrate from bolt/<br>
Run python manage.py createsuperuser and follow the prompts to add a super user <br>
Run python manage.py runserver<br>
Go to localhost:8000/admin and login <br>
Add a user with image<br>
Use Postman to make a POST request to http://localhost:8000/recognize/ with image as multipart/form-data<br>
A base64 encoded image is returned and is also saved in bolt/ with the name hello.jpg<br>
You can decode the image as base64.b64decode(returned_string) <br>
You can then save the image in jpg using : <br>
  filename = 'test.jpg'<br>
  with open(filename, 'wb') as f:<br>
      f.write(image)<br>

# face_recognition_api_django
An implementation of face recognition API with a model in django

# Running instructions 
Install all requirements by pip install -r requirements.txt
Run python manage.py migrate from bolt/
Run python manage.py createsuperuser and follow the prompts to add a super user 
Run python manage.py runserver
Go to localhost:8000/admin and login 
Add a user with image
Use Postman to make a POST request to http://localhost:8000/recognize/ with image as multipart/form-data
A base64 encoded image is returned and is also saved in bolt/ with the name hello.jpg
You can decode the image as base64.b64decode(returned_string) 
You can then save the image in jpg using : 
  filename = 'test.jpg'
  with open(filename, 'wb') as f:
      f.write(image)

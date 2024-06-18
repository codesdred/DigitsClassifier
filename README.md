# How to run the project :
1. Open terminal.
2. Write `pip install -r requirements.txt`
3. The file contains dependencies based on `python --version == 3.12.3`,
   incase of errors, remove the versions and only install -
   - `pip install Flask`
   - `pip install tensorflow==2.16.1`
   - `pip install Pillow`
   <br>
   All required packages will be installed based on your Python version.
   <br>
> Note: tensorflow version needs to be 2.16.1 as the model was trained using this version.
   
5. Now run `python wsgi.py`
6. Flask application will start in the localhost.

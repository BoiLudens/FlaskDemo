<h2>Create the Environment</h2>
py -3 -m venv env

<h2>Activate the environment</h2>
Linux/MacOS
. env/bin/activate
Windows
env\Scripts\activate

<h2>Install Dependencies</h2>
pip install -r requirements/dev.txt

<h2>To Run Flask at localhost:5000</h2>
Linux/MacOS
python -m flask run
Windows
python -m flask run

<h2>To Configure Environment in PyCharm IDE<h/2>
ScriptPath : FlaskDemo\env\Scripts\flask.exe
Parameters : run
Environment Variables : PYTHONUNBUFFERED=1;FLASK_APP=app.py
WorkingDirectory : FlaskDemo
# OctopusEnergy
## Flow File Upload
This is a Django app developed by Anagha Radhakrishnan.

### Installation
Clone the repository: git@github.com:Anagha22/Octopus_energy_task.git

### Create a virtual environment and activate it:
python3 -m venv env
##### Activate the environment
source env/bin/activate

### Install requirements
pip install -r requirements.txt

### Run migrations: 
python manage.py migrate

### Usage:
Start the development server: python manage.py runserver
#### Access the app in your browser at http://localhost:8000/

### Management Command
#### To use the management command for processing D0010 files, run the following command:

python manage.py files_upload <path_to_file>

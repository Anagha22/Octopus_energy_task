# OctopusEnergy
## Flow File Upload
This is a Django app developed by Anagha Radhakrishnan.

### Installation
Clone the repository: git clone https://github.com/Anagha22/OctopusEnergy.git

### Create a virtual environment and activate it:
python3 -m venv env
source env/bin/activate

### Run migrations: 
python manage.py migrate

### Usage:
Start the development server: python manage.py runserver
Access the app in your browser at http://localhost:8000/

### Management Command
#### To use the management command for processing D0010 files, run the following command:

python manage.py files_upload <path_to_file>

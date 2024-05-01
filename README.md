
# etl-application-dsvc

### Owned by: Data Engineering Squad

---
# Description
This is a Python application hosted in Kubernetes. The purpose of this application is to pull data from source, perform transformations, and load to destination. 

The data flow is as follows: source -> App -> destination.

Further documentation describing useful commands, the permission groups, Jenkins etc can be found here: 

## Application logic: 
- An in depth description of the application logic
E.g Describing the API calls / Database queries / file read/writes / and transformations performed


## Entity Relationship Diagram: 
- Diagrams showing the entity relationships

# Set up
- Navigate to code\etl_application\etl_application
- Setup a Virtual Environment
- - run `python -m venv venv`
- - `venv\Scripts\activate.bat` (Windows)
- - `pip install -r ..\requirements.txt`

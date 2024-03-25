import os, sys
from pathlib import Path
import logging

while True:
  project_title = input("Enter your project name :")
  if project_title !="":
    break

#src/__init__.py
list_of_files = [
f"{project_title}/__init__.py",
f"{project_title}/components/__init__.py",
f"{project_title}/config/__init__.py",
f"{project_title}/constants/__init__.py",
f"{project_title}/entity/__init__.py",
f"{project_title}/exception/__init__.py",
f"{project_title}/logger/__init__.py",
f"{project_title}/pipeline/__init__.py",
f"{project_title}/utils/__init__.py",
"config/config.yaml",
"schema.yaml",
"app.py",
"main.py",
"logs.py",
"exception.py",
"setup.py"
]

for filepath in list_of_files:
  filepath = Path(filepath)
  filedir,filename = os.path.split(filepath)

  if filedir !="":
    os.makedirs(filedir,exist_ok=True)
    
  if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0 ):
    with open(filepath,'w') as f:
      pass
  else:
    logging.info(f"File is already present at : {filepath}")

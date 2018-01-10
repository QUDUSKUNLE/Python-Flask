"""
  How to set up virtual environment
    pip install virtualenv
    pip install virtualenvwrapper

  # export WORKON_HOME=~/Envs
  source /usr/local/bin/virtualenvwrapper.sh

  # To activate virtualenv and set up flask
  1.  mkvirtualenv my-venv
  ###2.  workon my-venv
  3.  pip install Flask
  4.  pip freeze
  5. # To put all dependencies in a file
      pip freeze > requirements.txt

  6. run.py: entry point of the application
  7. relational database management system
      SQLite, MYSQL, PostgreSQL
      SQLAlchemy is an Object Relational Mapper (ORM),
      which means that it connects the objects of an application to tables in a
      relational database management system.
"""
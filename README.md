# InterpLinks1.0


InterpLinks is a Flask application to connect client of foreign language with interpreters on any language

## Development Environment

At the bare minimum you'll need the following for your development environment:

1. [Python](http://www.python.org/)
2. [PostgreSQL](http://www.postgresql.com/)


It is strongly recommended to also install and use the following tools:

1. [virtualenv](https://python-guide.readthedocs.org/en/latest/dev/virtualenvs/#virtualenv)

### Local Setup

The following assumes you have all of the recommended tools listed above installed.

#### 1. Clone the project:

    $ git clone https://github.com/ait-sv/InterpLinks.git
    $ cd InterpLinks

#### 2. Create and initialize virtual environment for the project:

    $ py -3 -m venv env
    $ pip install -r requirements.txt

#### 3. Upgrade the database:

    $ alembic upgrade head

#### 4. Run the development server:

    $ python wsgi.py

#### 5. Open [http://localhost:5000](http://localhost:5000)


### Development

If all went well in the setup above you will be ready to start hacking away on
the application.

#### Database Migrations

This application uses [Alembic](http://alembic.readthedocs.org/) for database
migrations and schema management. Changes or additions to the application data
models will require the database be updated with the new tables and fields.
Additionally, ensure that any new models are imported into the consolidated
models file at `main.models`. To generate a migration file based on the
current set of models run the following command:

    $ alembic revision --autogenerate -m "<a description of what was modified>"

Review the resulting version file located in the `alembic/versions` folder. If
the file is to your liking upgrade the database with the following command:

    $ alembic upgrade head

For anything beyond this workflow please read the Alembic documentation.

#### Management Commands

Management commands can be listed with the following command:

    $ python manage.py

These can sometimes be useful to manipulate data while debugging in the browser.


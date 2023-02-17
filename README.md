# FASTAPI + Alembic + SQLAlchemy Tutorial 

A FastAPI + Alembic + Sqlalchemy tutorial written by: Paul C. Nnaoji

Step 1) Clone the repo. (For a finished version of this tutorial switch to the "finished" branch. Run `docker volume create --name=postgres_data`, and then go into the running alembic_tutorial-web-1 container from here run `alembic upgrade head` this will create the tables in your db. Next login to pgadmin (use the credentials found in docker-compose.yml file) and run this insert to create data `INSERT INTO users (user_id,name) VALUES ('c2d29867-3d0b-d497-9191-18a9d8ee7830', 'Gandalf')`. Now you can go to your FastAPI GUI and query all users. Congrats! You should see the data you inserted via pgadmin! )

The Following Instructions below are for those who want to set up alembic from scratch in the `main` branch.

Step 2) Run `alembic init alembic` in the root of your project directory. Look at the repo structure here if you are unsure what the root level is. (You can run this command in the docker GUI or docker compose exec into container ) This command will create all the files you need in your project for alembic!

Step 3) Go to line 53 in the `alembic.ini` file and update the `sqlalchemy.url` with the path to your postgresql db (your url should be in the `docker-compose.yml` file)

Step 4) Create your tables in `db.py` (I created a `User` that takes a `UUID` and `name`) ex: ("c2d29867-3d0b-d497-9191-18a9d8ee7830", "Gandalf").

Step 5) In the alembic folder find `env.py` and import your `metadata` object from `app.db` then update line 21 so that the variable equals your `metadata` object.

Step 6) Now you should be able to run `alembic revision --autogenerate -m "Added user table"` in your container and it will automatically generate a script that scaffolds your tables and columns. 

Step 7) Check to see if your migration script was generated in the migration folder. If it was created, and the script looks good run `alembic upgrade head` to push the changes to the DB. Consult the Alembic documentation to learn how to move back and forth between versions of your DB(each migration file represents changes made to your tables). Moving forward you can use the autogenerate command whenever you change your db to detect changes and prepare a migration script. 

Step 8) Verify the tables were created in pgadmin and add data to it from the GUI.

Step 9) - Create a FastAPI endpoint to test your data. (See the "finished" branch for an example.) *Note this is a demo so data validation via our Pydantic models are missing and the project structure is not modular. For a good project structure study tiangolo's template here.* <a href="https://github.com/tiangolo/full-stack-fastapi-postgresql/tree/master/%7B%7Bcookiecutter.project_slug%7D%7D">Example</a>

Step 10) Write a SQL Query in your FastAPI project and use your db connection object to execute the query.

Step 11) Return your data as a dictionary. Congrats you’ve got a working FastPAI application with SQLAlchemy and Alemic!

Potential next steps? Create a `POST` request to create more `User` data or add another column to your `User` table and migrate those changes so that your DB gets those latest changes.

Happy Coding!!!

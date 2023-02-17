# alembic_tutorial

alembic tutorial using sqlalchemy

FASTAPI + Alembic + SQLAlchemy

Step 1 Clone the repo 

Step 2 alembic init alembic (you can do this in the docker GUI or docker compose exec into container )

Step 3 Go to line 53 and update the sqlalchemy.url with the path to your postgresql db

Step 4 Create db files in db.py

Step 5 Update env.py with metadata object

Step 6 alembic revision --autogenerate -m "Added user table"

Step 7 Check to see if your migration script was generated in the migration folder

Step 8 -  Verify and insert data via pgadmin

Step 9 - Create an endpoint to test your data

Step 10 - Write a SQL Query in your FastAPI project and use your db connection object to execute the query

Step 11 - Return your query as a dictionary! Congrats you’ve got a working FastPAI project with SQLAlchemy and Alemic

written by: Paul C. Nnaoji

# BOTS FUSION AI

## :snowflake: Deployment

- Heroku - https://joy-bots-fusion-ai.herokuapp.com/
- API docs - https://joy-bots-fusion-ai.herokuapp.com/docs

## :crossed_swords: EndPoints

1. ### GET all
   - `client/` - Retrives all clients from the database.
2. ### GET one
   - `client/{client_id}` - Retrives data of client with `client_id` from the database.
3. ### POST
   - `client/` - Adds data into data base
4. ### PUT
   - `client/{client_id}` - Updates data of client with `client_id` from the database.
5. ### DELETE
   - `client/{client_id}` - Delete data of client with `client_id` from the database.

- check [postman_collection.json](https://github.com/J0SAL/ibm-rush-estimator/edit/main/fastapi.postman_collection.json) for more details

## :runner: Local setup - Backend

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Python](https://www.python.org/) installed.

```bash
# Clone this repository
$ git clone https://github.com/J0SAL/bots-fusion-ai.git
# Go into the repository
$ cd bots-fusion-ai
# Create & Activate Environment (optional) here's a sample code
$ pyton -m venv project_env
$ project_env\Scripts\activate.bat
# Install dependencies
pip -r requirements.txt
# Run the app
python main.py
# The server will start at <http://localhost:8000>
```

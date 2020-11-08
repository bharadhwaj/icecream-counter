# Icecream Counter

A django application to track, calculate and collect fines from
colleagues who keeps missing the meetings. 

This is a plug and play application where you can just configure
database details and application is ready to be launched.

---

## Running the application

1. Clone the application  
    ```shell script
    $ git clone git@github.com:bharadhwaj/icecream-counter.git
    ```

2. Install the required libraries to run from `requirements.txt`
    ```shell script
    $ pip install -r requirements.txt
    ```

3. Set up the `.env` file in the root folder. Here is the sample
`.env` file
    ```.env
    SECRET_KEY=<<django_secret_token>>
    
    SITE_HEADER=<<site_header>>
    INDEX_TITLE=<<index_title>>
    
    # If you don't define any values below, 
    # SQLite instance will be created
   
    DB_ENGINE=<<django.db.backends.mysql>>
    DB_HOST=<<host_name/host_ip>>
    DB_PORT=<<host_port>>
    DB_USER=<<db_user>>
    DB_PASSWORD=<<db_user_password>>
    DB_NAME=<<db_name>>
    ```
    
4. Apply the migrations by for the first time when running,
application.
    ```shell script
    $ python manage.py migrate
    ```
   
5. Run the application.
    ```shell script
    $ python manage.py runserver
    ```
   
---

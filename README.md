# PostgreSQL is enough 


## Random learning 


[https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING](PostgreSQL connection string)

can be 2 types:

    key / value 

        host=localhost port=5432 user=postgres password=secure_password db_name=local_db

    URIs 

        postgresql://<user>:<password>@<host>:<port>/<db>?<query_params> 
        postgresql://postgres:secure_password@localhost:5432/local_db






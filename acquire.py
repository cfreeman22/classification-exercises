
import pandas as pd

def get_db_url(db_name):
    from env import username, host, password
    return f'mysql+pymysql://{username}:{password}@{host}/{db_name}'



import os

def get_titanic_data():
    '''
    This function reads csv stored in the computer or the iris data from the Codeup db into a df.
    '''
    filename = "titanic.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=0)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('SELECT * FROM passengers', get_db_url('titanic_db'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df  


def get_iris_data():
    '''
    This function reads csv stored in the computer or the iris data from the Codeup db into a df.
    '''
    filename = "iris.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=0)
    else:
        # read the SQL query into a dataframe
        sql_query = """
                SELECT 
                    species_id,
                    species_name,
                    sepal_length,
                    sepal_width,
                    petal_length,
                    petal_width
                FROM measurements
                JOIN species USING(species_id)
                """
        df = pd.read_sql(sql_query, get_db_url('iris_db'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df  

def get_telco_data():
    '''
    This function reads csv stored in the computer or the iris data from the Codeup db into a df.
    '''
    filename = "telco_df.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=0)
    else:
        # read the SQL query into a dataframe
        sql_query = """
                select * from customers
                join contract_types using (contract_type_id)
                join internet_service_types using (internet_service_type_id)
                join payment_types using (payment_type_id)
                """
        df = pd.read_sql(sql_query, get_db_url('telco_churn'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df  

 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import splitting and imputing functions
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# turn off pink boxes for demo
import warnings
warnings.filterwarnings("ignore")

# import our own acquire module
import acquire


def clean_iris(df):
    '''
    This function acquires the data from source, cleans the data, creates  dummy variables,
    and prepares the data for analysis
    '''
    
    df = df.drop('species_id', axis =1)
    df.rename(columns={'species_name':'species'}, inplace=True)
    #dummy_df = pd.get_dummies(df_iris[['species']], dummy_na=False, drop_first=[True, True])

    dummy_df = pd.get_dummies(df.species)
    df = pd.concat([df, dummy_df], axis=1)
    
    return df

def split_iris(df):

    '''
    Takes in a dataframe and return train, validate, test subset dataframes
    '''
    train, test = train_test_split(df, test_size = .2, random_state=123, stratify=df.species)
    train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train.species)
    return train, validate, test


def prep_iris_data(df):
    '''
        This function cleans the data and prepares the data for analysis and testing

    '''
    df = clean_iris(df)
    
    train, validate, test = split_data(df)
     
    return train, validate, test



def clean_titanic(df):
    '''
    This function acquires the data from source, cleans the data, creates  dummy variables,
    and prepares the data for analysis
    '''
    df = df.drop_duplicates()
    #dropping unwanted columns 
    cols_to_drop = ['deck', 'embarked', 'class', 'age']
    df = df.drop(columns=cols_to_drop)
    # Run .fillna() on the entire df for embark_town with most common value, 'Southampton'.
    df['embark_town'] = df.embark_town.fillna(value='Southampton')
    #Get dummy vars for sex and embark_town
    dummy_df = pd.get_dummies(df[['sex', 'embark_town']], dummy_na=False, drop_first=[True, True])
    # Concatenate the dummy_df dataframe above with the original df and validate.
    df = pd.concat([df, dummy_df], axis=1)
    
    return df

def split_data(df):
    '''
    Takes in a dataframe and return train, validate, test subset dataframes
    '''
    train, test = train_test_split(df, test_size = .2, random_state=123, stratify=df.survived)
    train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train.survived)
    return train, validate, test


def prep_titanic_data(df):
    '''
    This function cleans the titanic data and prepares the data for analysis and testing
    '''
    df = clean_data(df)
    train, validate, test = split_data(df)

    return train, validate, test
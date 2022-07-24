
#importing dependencies
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import normalize

# loading data

def read_data():
  return pd.read_csv('autos.csv', encoding='Windows-1252')

cars_data = read_data()
# print(cars_data)
# print(cars_data.info())


# change name format from camelCase to snake_case
# defining the format

new_column_name = {"dateCreated": "ad_created",
    "dateCrawled": "date_crawled",
    "fuelType": "fuel_type",
    "lastSeen": "last_seen",
    "monthOfRegistration": "registration_month",
    "notRepairedDamage": "unrepaired_damage",
    "nrOfPictures": "num_of_pictures",
    "offerType": "offer_type",
    "postalCode": "postal_code",
    "powerPS": "power_ps",
    "vehicleType": "vehicle_type",
    "yearOfRegistration": "registration_year"}
      
## rename to new format name
cars_data = cars_data.rename(columns=new_column_name)
# print(cars_data.info())


# change date format column type to datetime dtype
cars_data[["ad_created", "date_crawled", "last_seen"]]=cars_data[["ad_created", "date_crawled", "last_seen"]].astype('datetime64')

# print(cars_data.info())

# remove units from price and odometer
# remove price unit
cars_data['price'] = cars_data['price'].str.replace('$','').str.replace(',','').astype('int64')

# print(cars_data['price'])

## remove odometer unit
cars_data['odometer'] = cars_data['odometer'].str.replace('km','').str.replace(',','').astype('int64')

# print(cars_data['odometer'])

# drop columns with too many unique var
## define the columns to drop 
cols_to_drop = [
    'name', #terlalu kecil
    'seller', #di atas 90%
    'offer_type', #di atas 90%
    'num_of_pictures', #di atas 90%
    'postal_code', #di atas 90%
]

cars_data_dropped = cars_data.drop(cols_to_drop, axis=1)
# print(cars_data_dropped.info())

# removing outliers in price (limit to between 500-40,000)
cars_data_drop = cars_data_dropped[ # Inputkan kode disini
    (cars_data_dropped['price'] > 500) 
    & 
    (cars_data_dropped['price'] < 40000)
]

# data imputation for NaN
## for object dtype column, impute with mode
### defining the columns to be imputed
cols_object = [
                'abtest', 
                'vehicle_type',
                'gearbox', 
                'model',
                'fuel_type',
                'brand',
                'unrepaired_damage',
                ]
### fill nan with mode data
cars_data_drop[cols_object] = cars_data_drop[cols_object].fillna(cars_data_drop[cols_object].mode().iloc[0])

## for numeric (int64) dtype column, impute with median
### defining the columns to be imputed
cols_num = [
    'price', 
    'registration_year',
    'power_ps', 
    'odometer', 
    'registration_month',
]

### fill nan with median
cars_data_drop[cols_num] = cars_data_drop[cols_num].fillna(cars_data_drop[cols_num].median())

# data normalization
## normalize value for numeric type, except "price"
### defining the scaler
def standard_scaler(df: pd.DataFrame):
    """Scaling standard scaler transform."""
    index_cols = df.index
    scaler = preprocessing.StandardScaler()
    np_scaler = scaler.fit_transform(df)
    df_transformed = pd.DataFrame(
        np_scaler, index=index_cols, columns=df.columns
    )
    return df_transformed

### dropping 'price' column from col_num
cols_num.remove('price')

### normalize columns in col_num (after removed for price)
cars_data_drop[cols_num] = standard_scaler(cars_data_drop[cols_num])

# encoding categorical column
## create get dummies from cars data with object column
dum_df = pd.get_dummies(cars_data_drop, columns=cols_object)

## merge dummies and initial data
cars_data_final = pd.merge(cars_data_drop, dum_df, how='inner')
print(cars_data_final)

# output as final csv file

cars_data_final.to_csv('cars_data_final_pipelined.csv')
print('Data Cleanup Complete!!, \n\nFile saved as: cars_data_final_pipelined.csv')



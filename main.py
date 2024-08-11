import os

from src.database_PostgreSQL import DataBase
from src.API_HH import HeadHunterRuAPI
from config import config


def main():
    params = config()
    database_name = "hh"  #Название базы данных

    hh_api = HeadHunterRuAPI    #Получение данных по API
    companies = hh_api.getting_info_company()   #Получение данных по компаниям
    vacancies = hh_api.getting_vacancy()    #Получение данных по вакансиям

    # Создание базы данных и таблиц
    hh_database = DataBase
    hh_database.create_database(database_name, params)

    # Внесение данных в таблицу "company"
    hh_database.save_data_to_database_company(companies, database_name, params)
    # Внесение данных в таблицу "vacancy"
    hh_database.save_data_to_database_vac(vacancies, database_name, params)


if __name__ == '__main__':
    main()

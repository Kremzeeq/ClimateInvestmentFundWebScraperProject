from pymongo import MongoClient

class Database(object):
    DATABASE = None

    @staticmethod
    def initialize(db_name):
        conn = MongoClient(host ='localhost', port=27017)
        Database.DATABASE = conn[db_name]

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def insert_many(collection, data):
        Database.DATABASE[collection].insert_many(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_and_spec_columns(collection, query, columns):
        return Database.DATABASE[collection].find(query, columns)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def delete(collection, query):
        Database.DATABASE[collection].delete(query)

    @staticmethod
    def delete_id(collection, id):
        Database.DATABASE[collection].delete_one({"id": id})


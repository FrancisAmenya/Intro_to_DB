#!/usr/bin/env python3
"""
This script connects to a MySQL server and creates the 'alx_book_store' database.
If the database already exists, it will not fail.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server (edit user/password/host if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rootpass"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Ensure the connection is properly closed
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            # Uncomment for confirmation
            # print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()

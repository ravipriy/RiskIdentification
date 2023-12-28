import mysql.connector

mysql_config = {
    'host': 'localhost', 
    'user': 'root',
    'password': 'admin',
    'database': 'cyber', 
}

def conn():
    try:
        connection = mysql.connector.connect(**mysql_config)
        return connection
    
    except mysql.connector.Error as e:
        print(f"Error: {e}")


connection=conn()

def registerUserIntoDb(name,email,password):
    if connection.is_connected():
                cursor = connection.cursor()
                insert_query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
                data = (name, email, password)

                cursor.execute(insert_query, data)
                connection.commit()
                return True
    return False
                

def login_user(email, password):
    try:
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Check if the user exists in the 'users' table
            select_query = "SELECT * FROM users WHERE email = %s AND password = %s"
            data = (email, password)

            cursor.execute(select_query, data)

            # Fetch the result
            user = cursor.fetchone()

            if user:
                return user[1]
            else:
                print("Login failed. Invalid email or password.")

    except mysql.connector.Error as e:
        print(f"Error: {e}")


def forgotPassword(email):
    try:
        cursor = connection.cursor()
        select_query = "SELECT * FROM users WHERE email = %s"
        
        # Make sure data is a tuple by adding a comma
        data = (email,)
        cursor.execute(select_query, data)

        # Fetch the result
        user = cursor.fetchone()

        if user:
            # If the user is found, retrieve the password
            
            return user[3]
        else:
            return False
    except mysql.connector.Error as e:
        print(f"Exception occur in forgotpassword: {e}")

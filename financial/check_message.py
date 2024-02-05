import mysql.connector
from Reply_messages.reply import ReplyConfig

class Checkconfig:
    def __init__(self, db_config):
        self.db_config = db_config

    def get_data_from_database(self, db_config,message):
        check=Checkconfig()
        UPI_traction_id,trust=check.get_data_from_database(db_config,message)
        if trust == "trust":
            connection = mysql.connector.connect(**db_config)
            try:
                cursor = connection.cursor()

                query = "SELECT * FROM trust_payments where UPI_traction_id=%s"
                cursor.execute(query, (UPI_traction_id,))
                data = cursor.fetchall()
                return data
            except mysql.connector.Error as err:
                print(f"Error: {err}")
            finally:
                if 'cursor' in locals() and cursor is not None:
                    cursor.close()
                if 'connection' in locals() and connection.is_connected():
                    connection.close()
        else:
            connection = mysql.connector.connect(**db_config)
            try:
                cursor = connection.cursor()
                query = "SELECT * FROM club_payments where UPI_traction_id=%s"
                cursor.execute(query, (UPI_traction_id,))
                data = cursor.fetchall()
                return data
            except mysql.connector.Error as err:
                print(f"Error: {err}")
            finally:
                if 'cursor' in locals() and cursor is not None:
                    cursor.close()
                if 'connection' in locals() and connection.is_connected():
                    connection.close()

class check_message_config:
    def __init__(self):
        pass 

    def main(self,db_config,message):
        check_config=Checkconfig()
        data=check_config.get_data_from_database(db_config,message)
        return data

        





























        

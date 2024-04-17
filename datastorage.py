import time
from datetime import datetime

from mysql import connector


def uncompleted_contact(data):
    connection = connector.connect(host='datastuntstaging.co.in',
                                   user='u385679644_wpautomation',
                                   password='z>P4I+3L/Q2a',
                                   database='u385679644_wpautomation')
    cursor = connection.cursor()
    try:
        connection.start_transaction()

        # Bulk insert data from logs dictionary into MySQL table
        for entry in data:
            job_id = entry.get('jobid')  # Use .get() method to safely retrieve values
            contact_name = entry.get('contact_name')  # Use .get() method to safely retrieve values
            contact_number = entry.get('contact_number')  # Use .get() method to safely retrieve values
            status = entry.get('status')  # Use .get() method to safely retrieve values
            timestamp = entry.get('timestamp')  # Use .get() method to safely retrieve values
            # Example SQL query to insert data into a table named 'automation_progress'
            sql = "INSERT INTO Successfull_jobs (jobid, contact_name, contact_number, status, timestamp) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (job_id, contact_name, contact_number, timestamp, status))

        # Commit changes to the database
        connection.commit()

    except connector.Error as err:
        print("An error occurred during save in database: ", err)
        connection.rollback()

    finally:
        # Close the database connection
        cursor.close()
        connection.close()


def completed_contact(data):
    connection = connector.connect(host='datastuntstaging.co.in',
                                   user='u385679644_wpautomation',
                                   password='z>P4I+3L/Q2a',
                                   database='u385679644_wpautomation')
    cursor = connection.cursor()
    try:
        connection.start_transaction()
        # Iterate over each dictionary in the data list
        for entry in data:
            # Extract values from the dictionary
            job_id = entry.get('jobid')  # Use .get() method to safely retrieve values
            contact_name = entry.get('contact_name')  # Use .get() method to safely retrieve values
            contact_number = entry.get('contact_number')  # Use .get() method to safely retrieve values
            status = entry.get('status')  # Use .get() method to safely retrieve values
            timestamp = entry.get('timestamp')  # Use .get() method to safely retrieve values

            # Example SQL query to insert data into a table named 'automation_status'
            sql = "INSERT INTO Successfull_jobs (jobid, contact_name, contact_number, status, timestamp) VALUES (%s, %s, %s, %s, %s)"
            # Execute the SQL query with values as a tuple
            cursor.execute(sql, (job_id, contact_name, contact_number, timestamp, status))
        # Commit changes to the database
        connection.commit()

    except connector.Error as err:
        # print("An error occurred during save in database:", err)
        connection.rollback()

    finally:
        # Close the database connection
        cursor.close()
        connection.close()


def current_contact_data_status(data):
    # Ensure data is a list of dictionaries
    if isinstance(data, list) and all(isinstance(entry, dict) for entry in data):
        connection = connector.connect(host='datastuntstaging.co.in',
                                       user='u385679644_wpautomation',
                                       password='z>P4I+3L/Q2a',
                                       database='u385679644_wpautomation')
        cursor = connection.cursor()
        try:
            connection.start_transaction()
            # Iterate over each dictionary in the data list
            for entry in data:
                # Extract values from the dictionary
                job_id = entry.get('jobid')  # Use .get() method to safely retrieve values
                contact_name = entry.get('contact_name')  # Use .get() method to safely retrieve values
                contact_number = entry.get('contact_number')  # Use .get() method to safely retrieve values
                status = entry.get('status')  # Use .get() method to safely retrieve values
                timestamp = entry.get('timestamp')  # Use .get() method to safely retrieve values

                # Example SQL query to insert data into a table named 'message_logs'
                sql = "INSERT INTO All_jobs (jobid, contact_name, contact_number, status, timestamp) VALUES (%s, %s, %s, %s, %s)"
                # Execute the SQL query with values as a tuple
                cursor.execute(sql, (job_id, contact_name, contact_number, timestamp, status))
            # Commit changes to the database
            connection.commit()

        except connector.Error as err:
            # print("An error occurred during save in database:", err)
            connection.rollback()

        finally:
            # Close the database connection
            cursor.close()
            connection.close()
    else:
        print("Error: 'data' must be a list of dictionaries.")


def trace_current_status():
    # Connect to the database
    connection = connector.connect(host='datastuntstaging.co.in',
                                   user='u385679644_wpautomation',
                                   password='z>P4I+3L/Q2a',
                                   database='u385679644_wpautomation')
    cursor = connection.cursor(dictionary=True)

    try:
        # Query to fetch the last added data based on timestamp
        sql = "SELECT * FROM All_jobs ORDER BY Timestamp DESC LIMIT 1"

        # Execute the query
        cursor.execute(sql)

        # Fetch the result
        last_added_data = cursor.fetchone()

        return last_added_data

    except connector.Error as err:
        # print("An error occurred while fetching last added contact:", err)
        pass

    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()



import datetime
import time


# To manage the job times
def job_time():
    current_hour = datetime.datetime.now().strftime('%H:%M:%S')
    # Checking if current time is between "10:00:00" and "23:59:59" or "00:00:00" and "05:00:00"
    if "22:00:00" <= current_hour <= "23:59:59" or "00:00:00" <= current_hour <= "05:00:00":
        print("Sleeping until 05:00:00")
        # Calculate time difference until 05:00:00
        target_time = datetime.datetime.strptime("05:00:00", "%H:%M:%S")
        current_time = datetime.datetime.strptime(current_hour, "%H:%M:%S")
        time_difference = (target_time - current_time).total_seconds()
        time.sleep(time_difference)

    else:
        pass






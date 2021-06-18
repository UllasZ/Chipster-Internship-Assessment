# Note : This code was run in Jupyter notebook. Do alter the execution as per your tools.

import pandas as pd
import sqlite3

current_directory = os.path.dirname(os.path.realpath('__file__'))
db_file_path = os.path.join(current_directory, 'Db-IMDB.db')

# convert the file path to string if neccesary.
conn = sqlite3.connect(db_file_path)


# Solution (a) : Film(s) with largest cast.
df = pd.read_sql_query("SELECT Movie.title as Title, COUNT(DISTINCT M_Cast.PID) as Cast_Size FROM Movie, M_Cast WHERE M_Cast.MID = Movie.MID GROUP BY M_Cast.MID ORDER BY Cast_Size DESC LIMIT 1;", conn)
df

'''
Expected Output:
    Title	Cast_Size
    0	Ocean's Eight	238
'''


# Solution (b) : The number of movies in that particular year that had only female actors. 
dg = pd.read_sql_query("SELECT Movie.year, COUNT(*) AS number_of_movies FROM Movie WHERE Movie.MID IN (SELECT M_Cast.MID FROM M_Cast, Person WHERE M_Cast.PID = Person.PID AND Person.Gender = 'Female');", conn)
dg


'''
Expected Output:
    year	number_of_movies
    0	None	0
'''

from sqlalchemy import create_engine
import pandas




def readSqlDatabase(table_name,columns=None):

    DatabaseName="AutoFormFiller.db"
    conn = create_engine('sqlite:///'+ DatabaseName)
    try:
        df2=pandas.read_sql_table(table_name, conn, columns=columns)
        #print(df2)
        TableFound=True
    except ValueError:
        df2=None
        TableFound=False
    return df2,TableFound
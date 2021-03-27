import sqlite3


def writeToSqlite(frame,table_name, DatabaseName):
    # DatabaseName="AutoFormFiller.db"

    conn = sqlite3.connect(DatabaseName)
    # print(frame)
    frame.to_sql(table_name, conn, if_exists="replace")
def cleanup(dbConn, dbCursor):
    dbCursor.close()
    dbConn.commit()
    dbConn.close()
import pymysql


def test_rds_connection():
    connection = pymysql.connect(
        host="augpracticedb.ctmu06kwa7xo.ap-southeast-2.rds.amazonaws.com",
        user="admin",
        password="Password9205",
        database="mysql",
        port=3306,
        connect_timeout=5
    )

    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION();")
        version = cursor.fetchone()
        print(f"\nConnected to RDS MySQL Version: {version[0]}")
        assert version is not None

    connection.close()
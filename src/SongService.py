import typing
import mysql.connector as mariadb
#from dotenv import load_dotenv
import os

from sqlalchemy import create_engine

str_conn='mysql+pymysql://root:root@localhost:3306/ultratrailv2'

cursor=create_engine(str_conn)

#load_dotenv()

if typing.TYPE_CHECKING:
    import Song


class SongService:
    tableName = 'prueba'
    str_conn='mysql+pymysql://root:root@localhost:3306/ultratrailv2'

    cursor=create_engine(str_conn)
    

    def save(self, song: 'Song'):
        self.cursor.execute(
            "INSERT INTO {} (name, artist, ranking, country, date)"
            " VALUES (\"{}\", \"{}\", \"{}\", \"{}\", \"{}\")"
            " ON DUPLICATE KEY UPDATE"
            " name=VALUES(name), "
            " artist=VALUES(artist), "
            " ranking=VALUES(ranking), "
            " country=VALUES(country), "
            " date=VALUES(date)".format(
                self.tableName,
                song.name,
                song.author,
                song.ranking,
                song.country,
                song.date
            )

        )
        self.cursor.commit()
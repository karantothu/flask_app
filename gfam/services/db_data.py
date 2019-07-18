from gfam.model.sequence_model import Sequence
import sqlite3


class SQLConnection:
    conn = None
    @staticmethod
    def get_connection():
        if not SQLConnection.conn:
            SQLConnection.conn = sqlite3.connect("example.db")
        return SQLConnection.conn

    def close_conn(self):
        # global conn
        if SQLConnection.conn:
            SQLConnection.conn.close()






# conn1 = sqlite3.connect('example.db')
# c1 = conn.cursor()

# c.execute('''CREATE TABLE sequences (
#             sequence_name text,
#             sequence text,
#             version real
#         )''')

# c.execute('''INSERT INTO sequences VALUES('gfam001','KJGFKGSADGAIUGHAVDJHGD', 1.0)''')
# c.execute('''SELECT * FROM sequences''')
# print(c.fetchall())
# conn.commit()


def insert_sequence(sequence):
    with conn:
        c.execute("INSERT INTO sequences VALUES (:sequence_name, :sequence, :version)",
                  {'sequence_name': sequence.sequence_name, 'sequence': sequence.sequence, 'version': sequence.version})


def get_sequence_by_name(sequence):

    conn = SQLConnection.get_connection()
    #
    #
    # with sqlite3.connect('example.db') as conn:
    #     print(conn)
    #     cursor = conn.cursor()
    #     print(sequence)
    cursor = conn.cursor()
    return cursor.execute("SELECT * FROM testme1 WHERE name=:sequence_name",
                          {'sequence_name': sequence.upper()}).fetchall()


def update_sequence(sequence_name, version):
    with conn:
        c.execute("""UPDATE sequences SET sequence = :sequence
                    WHERE sequence_name = :sequence_name""",
                  {'sequence_name': sequence_name, 'version': version})


def remove_sequence(sequence_name):
    with conn:
        c.execute("DELETE from sequences WHERE sequence_name = :sequence_name",
                  {'sequence': sequence_name})


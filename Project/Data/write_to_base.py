import championships_parser
from sqlite3 import connect


# ბაზაში წერს championships_parser ფაილში "გაპარსულ" მონაცემებს
# (ანუ წელსა და გამარჯვებულ გუნდს)
def to_base(championships_list=championships_parser.championships()):
    table_name = 'Championships'
    connection = connect('base.db3')
    cursor = connection.cursor()

    command = f""" 
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY, 
            Year TEXT,
            Team TEXT
        )
    """

    cursor.execute(command)

    command = f"""
        INSERT INTO {table_name}
            (Year, Team)
        VALUES
            (?, ?)
    """

    cursor.executemany(command, championships_list)
    connection.commit()


to_base()

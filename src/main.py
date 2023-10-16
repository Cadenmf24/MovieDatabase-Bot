from src.utils import connect


class main():

    def run(self):
        conn = connect()
        cur = conn.cursor()
        cur.execute('SELECT VERSION()')
        conn.close()

if __name__ == '__main__':
    main.run()
    
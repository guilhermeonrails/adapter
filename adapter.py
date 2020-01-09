class Postgres:
    def __str__(self):
        return 'Postgres Database'

    def conecta(self):
        return 'conectado'

class MySql:
    def __str__(self):
        return 'MySql:'

    def conectar(self):
        return 'running'

class MongoDB:
    def __str__(self):
        return 'Mongo'

    def execute(self):
        return 'executando o MongoDB'

class Adapter:
    def __init__(self, banco, adaptando_metodos):
        self.banco = banco
        self.__dict__.update(adaptando_metodos)
    
    def __str__(self):
        return str(self.banco)

def main():
    mongo = MongoDB()
    pg = Postgres()
    my_sql = MySql()

    adaptador_pg = Adapter(pg, dict(execute=pg.conecta))
    adaptador_my_sql = Adapter(my_sql, dict(execute=my_sql.conectar))

    bancos = [mongo, adaptador_my_sql, adaptador_pg]

    for banco in bancos:
        print('{} {}'.format(str(banco), banco.execute()))

if __name__ == "__main__":
    main()

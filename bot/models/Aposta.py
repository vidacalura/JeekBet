import db_connection as db

class Aposta:
    def __init__(self, aposta_id, titulo, opcoes, ativa, criador, data):
        self.aposta_id = aposta_id
        self.titulo = titulo
        self.opcoes = opcoes
        self.ativa = ativa
        self.criada_por = criador
        self.criada_hora = data 

    def criar_aposta(self):
        conn = db.connect()
        cur = conn.cursor()

        if self.get_aposta_ativa() != None:
            cur.close()
            conn.close()

            raise Exception("Uma aposta está em andamento no momento. Encerre-a antes de começar uma nova.")

        try:
            cur.execute("""
                INSERT INTO apostas (titulo, opcoes, ativa, criada_por, criada_hora)
                VALUES(%s, %s, %s, %s, NOW());""",
                [self.titulo, self.opcoes, True, self.criada_por])
            conn.commit()
        except:
            cur.close()
            conn.close()

            raise Exception("Erro ao cadastrar aposta. Verifique se você já não está cadastrado com !dinheiro")

        cur.close()
        conn.close()

    def get_aposta_ativa(self):
        conn = db.connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM apostas WHERE ativa = TRUE;")

        row = cur.fetchone()

        cur.close()
        conn.close()

        if row == None:
            return row

        return Aposta(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5]
        )

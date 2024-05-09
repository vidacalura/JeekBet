import db_connection as db

class Usuario:
    def __init__(self, id, nome, dinheiro):
        self.id = id
        self.nome = nome
        self.dinheiro = dinheiro

    def get_dinheiro(self):
        conn = db.connect()
        cur = conn.cursor()

        cur.execute("SELECT dinheiro FROM usuarios WHERE usu_id = %s;", [self.id])

        dinheiro = cur.fetchone()
        if dinheiro == None:
            cur.close()
            conn.close()

            raise Exception("Usuário não está cadastrado no JeekBet. Cadastre-se com !criar-conta")        
        
        self.dinheiro = dinheiro[0]

        cur.close()
        conn.close()

        return self.dinheiro

    def set_dinheiro(self, dinheiro):
        conn = db.connect()
        cur = conn.cursor()

        try:
            cur.execute("UPDATE usuarios SET dinheiro = %s WHERE usu_id = %s;",
                [dinheiro, self.id])
            conn.commit()
        except:
            cur.close()
            conn.close()

            raise Exception("Erro ao atualizar dinheiro de usuário. Informe um dev deste erro.")        
        
        self.dinheiro = dinheiro

        cur.close()
        conn.close()

    def set_nome(self, novo_nome):
        conn = db.connect()
        cur = conn.cursor()

        try:
            cur.execute("UPDATE usuarios SET nome = %s WHERE usu_id = %s;",
                [novo_nome, self.id])
            conn.commit()
        except:
            cur.close()
            conn.close()

            raise Exception("Erro ao atualizar nome de usuário. Informe um dev deste erro.")        
        
        self.nome = novo_nome

        cur.close()
        conn.close()

    def cadastrar_usuario(self):
        conn = db.connect()
        cur = conn.cursor()

        try:
            cur.execute("""
                INSERT INTO usuarios (usu_id, nome, dinheiro)
                VALUES(%s, %s, 500);""",
                [self.id, self.nome])
            conn.commit()
        except:
            cur.close()
            conn.close()

            raise Exception("Erro ao cadastrar usuário. Verifique se você já não está cadastrado com !dinheiro")

        cur.close()
        conn.close()

    def deletar_usuario(self):
        conn = db.connect()
        cur = conn.cursor()

        try:
            cur.execute("DELETE FROM usuarios WHERE usu_id = %s;", [self.id])
            conn.commit()
        except:
            cur.close()
            conn.close()

            raise Exception("Erro ao excluir conta. Informe um dev deste erro.")        
        
        cur.close()
        conn.close()


def get_ranking_usuarios():
    conn = db.connect()
    cur = conn.cursor()

    try: 
        cur.execute("SELECT usu_id, nome, dinheiro FROM usuarios ORDER BY dinheiro LIMIT 25;")

        usu_arr = []
        for usu in cur.fetchall():
            usu_arr.append(Usuario(usu[0], usu[1], usu[2]))
    except Exception as e:
        print(e)
        cur.close()
        conn.close()

        raise Exception("Erro ao retornar ranking.")

    cur.close()
    conn.close()

    return usu_arr

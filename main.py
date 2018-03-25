# -*- coding: utf-8 -*-

from database import BancoDeDados

if __name__ == '__main__':
    db = BancoDeDados()
    db.conecta()
    db.criar_tabelas()
    #db.inseri_cliente('marcos','111111111','M@gamil.com')
    #db.inseri_cliente('thomas','111111112','T@gamil.com')
    #db.inseri_cliente('mario','111111312','mari@gmail.com')
    #db.inseri_cliente ('ana','115111312','ana@gmail.com')
    #db.busca_cliente('111111111')
    db.buscar_email('M@gamil.com')
    db.buscar_email('Y@gamil.com')
    db.buscar_email('T@gamil.com')
    db.buscar_email('ana@gmail.com')
    db.remove_cliente('111111312')

    db.desconecta()

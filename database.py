# -*- coding: utf-8 -*-

import sqlite3


class BancoDeDados():

    def __init__(self, nome='Banco.db'):
        self.nome = nome
        self.conexao = None

    def conecta(self):
        self.conexao = sqlite3.connect(self.nome)

    def desconecta(self):
        try:
            self.conexao.close()

        except AttributeError:
            pass

    def criar_tabelas(self):

        try:
            cursor = self.conexao.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS clientes(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cpf VARCHAR(11) UNIQUE NOT NULL,
                    email TEXT NOT NULL            
                );
                ''')

        except AttributeError:
            print('Banco de dados não conectado.')

    def inseri_cliente(self, nome, cpf, email):
        try:
            cursor = self.conexao.cursor()
            try:
                cursor.execute('''
                    INSERT INTO clientes (nome,cpf,email) VALUES (?,?,?)
                    ''', (nome, cpf, email))
            except sqlite3.IntegrityError:
                print('O CPF: {} já esta cadastrado.'.format(cpf))

            self.conexao.commit()
        except AttributeError:
            print('Banco de dados não conectado.')

    def busca_cliente(self, cpf):
        try:
            cursor = self.conexao.cursor()

            cursor.execute('''SELECT * FROM clientes;''')

            for linha in cursor.fetchall():
                if linha[2] == cpf:
                    print('Cliente {} encontrado'.format(linha[1]))
                    break

        except AttributeError:
            print('Banco de dados não conectado.')

    def remove_cliente(self, cpf):
        try:
            cursor = self.conexao.cursor()
            cursor.execute('DELETE FROM clientes where cpf=?', [(cpf)])
            self.conexao.commit()
        except AttributeError:
            print('Banco de dados não conectado.')

    def buscar_email(self, email):

        try:
            cursor = self.conexao.cursor()

            cursor.execute('SELECT * FROM clientes WHERE email=?', [(email)])

            cliente = cursor.fetchone()

            if cliente:
                print('Cliente encontrado.')
                return True
            else:
                print('Cliente não encontrado.')
                return False

        except AttributeError:
            print('Banco de dados não conectado.')

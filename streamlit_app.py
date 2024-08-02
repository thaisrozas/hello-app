import streamlit as st
import pymysql

# Função para conectar ao banco de dados
def get_connection():
    connection = pymysql.connect(
        host='localhost',
        user='seu_usuario',  # substitua pelo seu usuário do MySQL
        password='sua_senha',  # substitua pela sua senha do MySQL
        database='nome_do_banco_moodle',  # substitua pelo nome do banco de dados do Moodle
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# Função para executar uma consulta
def execute_query(query):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        connection.commit()
    finally:
        connection.close()
    return result

st.title('Consulta ao Banco de Dados do Moodle')

# Entrada do usuário para a consulta SQL
query = st.text_area('Digite sua consulta SQL:')

if st.button('Executar Consulta'):
    if query:
        try:
            results = execute_query(query)
            st.write(results)
        except Exception as e:
            st.error(f'Ocorreu um erro: {e}')
    else:
        st.warning('Por favor, digite uma consulta SQL.')

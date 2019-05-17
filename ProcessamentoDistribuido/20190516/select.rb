# data 2019-05-16
# autor @gustavopoli
# UNIFEG - 5o Periodo Ciencia da Computacao
# -------

require 'mysql2' # importa a gem mysql2 (MySQL)

# db eh um objeto de conexao com o banco de dados MySQL
db = Mysql2::Client.new(:host     => "localhost",
                        :username => "aluno",
                        :password => "aluno123",
                        :database => "2019A5P")

# faz uma consulta no banco de dados
# seu resultado fica armazenado como uma lista
rs_client = db.query("select * from clients")

# imprime o tamanho (numero de registros) da lista
puts rs_client.size

# laco de repeticao que sera executado para cada
# elemento da lista "client" eh um element/registro
# do banco de dados retornado pela consulta
rs_client.each do |client|
    puts client # faz a impresao do dicionario com o registro do laco
end

puts "..|fim da aplicacao"



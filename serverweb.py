import socket
 
HOST = "127.0.0.1"
PORTA = 8181
 
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORTA))
servidor.listen(6)


 
def extrai_nome_doc(req):
	return req.split()[1][1:]				#Quebro a requisicao escolho a parte que contem o nome do arquivo e tiro o primeiro elemento que eh o barra
	
def constroi_resposta(doc):
	res = "HTTP/1.1 200 OK\r\n\r\n"
	if doc == "":
		narq = "index.html"
	else:
		narq = doc
	try:
		f = open(narq)
		dados = f.read()
		f.close()
	except:
		f = open("notfound.html")
		dados = f.read()
		res = "HTTP/1.1 404 Not Found\r\n\r\n"
		f.close()
	res = res + dados
	return res

while 1:
	conexao, end_remoto = servidor.accept()
	req_http = conexao.recv(1024)
	doc = extrai_nome_doc(req_http)
	print "Nome do arquivo:", doc
	resposta = constroi_resposta(doc)
	conexao.send(resposta)
	conexao.close()

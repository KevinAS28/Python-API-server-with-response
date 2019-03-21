import sys
import socket
import crypto
from threading import Thread



ip = "0.0.0.0"
port = 80
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((ip, port))
server.listen()
print("listening on: %s:%d\n\n\n"%(ip, port))
listJson = ["{userID:\"01\", rc: \"00\", kdReg: \"0011\", data: {listTrn:[{Ref: \"refnya\", Tanggal: \"Tglnya\", Jam: \"jamnya\", Debet: \"debetnya\", Ket: \"ket\"}, {Ref: \"refnya\", Tanggal: \"Tglnya\", Jam: \"jamnya\", Debet: \"debetnya\", Ket: \"ket\"}], saldoEmoney: \"12345\", noAcc: \"0000\", idMerchant: \"1111\", nmMerchant: \"merchantSaya\", saldo: \"9999\" }}", "{rc: \"01\"}"]
def handler(client, addr):
 recv = client.recv(1024)
 print("connection from %s:%d"%(addr[0], addr[1]))
 #print("real_data: \n", recv)
 print("data:\n", (recv))
 response = input("response: ")

 tosend = ((listJson[int(response)].encode("utf-8")))
 print(tosend)
 client.send(tosend)
 print("\n"*3)
 client.close()


stop = False
while (not stop):
 try:
  client, addr = server.accept()
  Thread(target=handler, args=[client, addr]).start()
 except KeyboardInterrupt:
  stop = False
  break


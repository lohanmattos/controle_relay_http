# Controle de relay via http
Esse programa é baseado em uma placa que adquirei na internet. 
Atráes do manual do fabricante consegui os parametros necessarios para realizar as requisições http.


Exemplo: 
http://ip-da-placa/relay_cgi.cgi?type=0&relay=0&on=0&time=5&pwd=4660&

Os principais paramentos a cima são:

relay = Seleciona o relé correspondente na placa. Ex: 1,2,3
on= 1 ou 0 corresponde a ligar ou desligar o relé

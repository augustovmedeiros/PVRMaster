import requests

class Botao:
    def __init__(self, botaoId, acao):
        self.botaoId = botaoId
        self.acao = acao
    def executar(self):
        numero = self.botaoId
        user_agent = {'User-agent': 'ALiPlay 2.0 @ Android'}
        jsonContent = {'request': 'key_command', 'device_id': '30:34:D2:A6:97:E1', 'key': f'{numero}'}
        try:
            response  = requests.post('http://192.168.1.6:20181', headers=user_agent, json=jsonContent)
        except:
            print("Foi")

sete = Botao(7, "ok")
dois = Botao(2, "ok")
um = Botao(1, "ok")

sete.executar()
dois.executar()
um.executar()      


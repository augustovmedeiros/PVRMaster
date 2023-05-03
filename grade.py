import json
import requests
from canais import *
from datetime import datetime, timedelta

class Programa:
    def __init__(self, inicio, fim, canal, titulo, reprise):
        self.inicio = inicio
        self.fim = fim
        self.canal = canal
        self.titulo = titulo
        self.reprise = reprise

    def reprisar(self):
        self.reprise = True

def parseTime(timeStr):
    gradeTimeParse = datetime.strptime(timeStr, '%Y-%m-%dT%H:%MZ')#iso8601
    return gradeTimeParse

def formatTime(timeStr):
    tempoFormatado = timeStr.strftime('%Y-%m-%dT%H:%M:%SZ')
    return tempoFormatado

def parseGrade(canais):
    canalStr=""
    for canal in canais:
        canalStr += f"1_{canal}+"
    inicio = formatTime(datetime.now())
    fim = formatTime(datetime.now() + timedelta(days=30))
    url = f"https://programacao.claro.com.br/gatekeeper/exibicao/select?q=id_revel:({canalStr})+AND+id_cidade:1&wt=json&rows=200000&start=0&sort=id_canal+asc,dh_inicio+asc&fl=dh_fim+dh_inicio+st_titulo+titulo+id_programa+id_canal+id_cidade&fq=dh_inicio:[{inicio}+TO+{fim}]"
    gradeRequest = requests.get(url)
    gradeParse = json.loads(gradeRequest.text)
    gradeContent = {}
    for programa in gradeParse["response"]["docs"]:
        conteudo = programa['titulo'] + programa['id_canal']
        if(conteudo in gradeContent):
            gradeContent[conteudo].reprisar()
        else:
            gradeContent[conteudo] = Programa(programa['dh_inicio'], programa['dh_fim'], programa['id_canal'], programa['titulo'], False)
    return gradeContent

meusCanais = [520, 574, 2243, 2429, 2445, 1008, 1104, 1017, 1616, 2136, 1197, 1059, 2061, 931, 1203, 950, 1619, 2309, 2224, 875, 878, 876, 1098, 2062, 2424, 838, 898, 1019, 1018, 871, 1100, 856, 1330, 2332, 1099, 1086, 2354, 2368, 2352]
#meusCanais = [1270]
canais = getCanaisArray()
programacao = parseGrade(meusCanais)


def pesquisarPrograma(pesquisa):
    for prog in programacao:
        prog = programacao[prog]
        if(pesquisa.lower() in prog.titulo.lower()):
            print(prog.titulo, "-", canais[prog.canal].nome, "-", parseTime(prog.inicio).strftime('%H:%M - %d/%m'), "- Reprise:", str(prog.reprise))
def pesquisarCanal(pesquisa):
    for prog in programacao:
        prog = programacao[prog]
        if(pesquisa.lower() in canais[prog.canal].nome.lower()):
            print(prog.titulo, "-", canais[prog.canal].nome, "-", parseTime(prog.inicio).strftime('%H:%M - %d/%m'), "- Reprise:", str(prog.reprise))

#for prog in programacao:
        #prog = programacao[prog]
        #print(prog.titulo, parseTime(prog.inicio), canais[prog.canal].nome, "Reprise:", str(prog.reprise))

import requests
from argparse import ArgumentParser

parser = ArgumentParser(description="Small script to check bondi's schedule")
parser.add_argument('-p','--parada',action='store',dest='parada',default='2664')
parser.add_argument('-b','--bondi',action='store',dest='bondi')
args = parser.parse_args()
    
url = 'http://api.montevideo.gub.uy/transporteRest/siguientesParada/'+args.parada
cabezales = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320M Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.64 Mobile Safari/537.36'}
r = requests.get(url,headers=cabezales)

if args.bondi:
    for i in r.json():
        if i['linea']==args.bondi and i['real']==True:
            print("El %s está a punto de pasar en %s minutos" % (i['linea'],i['minutos']))
        elif i['linea']==args.bondi and i['real']==False:
            print("El %s no está en camino pero se estima que pasa en %s minutos" % (i['linea'],i['minutos']))


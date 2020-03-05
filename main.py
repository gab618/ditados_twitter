import random
import oauth2
import json
import urllib.parse
import time

proverbsSource1 = [
    "Quem tem boca ",
    "Água mole e pedra dura ",
    "Mais vale um pássaro na mão ",
    "Não adiante chorar ",
    "Quem ri por último ",
    "Mente vazia ",
    "Cada macaco ",
    "O que os olhos não veêm ",
    "A vingança é um prato que ",
    "Aqui se faz ",
    "Mentira ",
    "A ocasião ",
    "A voz do povo ",
    "A cara de um ",
    "Antes só ",
    "Antes tarde ",
    "Após a tempestade ",
    "Bandido bom ",
    "Cão que ladra ",
    "Caiu na rede ",
    "Em casa de ferreiro ",
    "A cavalo dado ",
    "De grão em grão ",
    "Dar a César ",
    "Deus escreve certo ",
    "Diga-me com quem andas ",
    "Quando a esmola é demais ",
    "Em rio de piranhas ",
    "Escreveu não leu ",
    "Em boca fechada ",
    "Faço o que eu digo ",
    "Gato escaldado ",
    "Ladrão que rouba ladrão ",
    "Manda quem pode ",
    "Deus ajuda ",
    "Não deixes para amanhã ",
    "Nem tudo que reluz ",
    "O seguro ",
    "Os incomodados ",
    "Olho por olho ",
    "O que não mata ",
    "O barato ",
    "O sol nasce ",
    "O pior surdo ",
    "O pior cego ",
    "O bom filho ",
    "Para bom entendedor ",
    "Pau que nasce torto ",
    "Pimenta nos olhos dos outros ",
    "Panela velha ",
    "Quem com ferro fere ",
    "Quem não tem cão ",
    "Quem tudo quer ",
    "Quem nasceu para vintém ",
    "Quem não arrisca ",
    "Quem vê cara ",
    "Quem semeia ventos ",
    "Quem cala ",
    "Quem canta ",
    "Quem é vivo ",
    "Quem não deve ",
    "Quem não chora ",
    "Quem não usa a cabeça ",
    "Quem conta um conto ",
    "Quem diz o que quer ",
    "Quem vê cara ",
    "Quem nunca comeu melado ",
    "Quem dá aos pobres ",
    "Quando um não quer ",
    "Quando um burro fala ",
    "Roupa suja ",
    "Se Maomé não vai a montanha, ",
    "Santo de casa ",
    "Saco vazio ",
    "Tamanho ",
    "Uma mão ",
    "Vaso ruim ",
    "Onde Judas ",
    "Tirar o cavalinho ",
    "À noite ",
    "É melhor não cutucar ",
    "Não conte com o ovo ",
    "Mais vale um cachorro amigo ",
    "Quem desdenha ",
    "O mundo ",
    "Quer rir ",
    "Você tem que me ajudar ",
    "Cada cachorro "
    ]

proverbsSource2 = [
    "vai à Roma",
    "tanto bate até que fura",
    "do que dois voando",
    "pelo leite derramado",
    "ri melhor",
    "oficina do diabo",
    "no seu galho",
    "o coração não sente",
    "se come cru",
    "aqui se paga",
    "tem perna curta",
    "faz o ladrão",
    "é a voz de Deus",
    "é o focinho do outro",
    "que mal acompanhado",
    "do que nunca",
    "vem a bonança.",
    "é bandido morto",
    "não morde",
    "é peixe",
    "espeto de pau",
    "não se olha os dentes",
    "a galinha enche o papo",
    "o que é de César",
    "por linhas tortas",
    "e te direi quem és",
    "o santo desconfia",
    "jacaré nada de costas",
    "o pau comeu",
    "não entra mosca",
    "não faça o que eu faço",
    "tem medo de água fria",
    "tem cem anos de perdão",
    "obedece quem tem juízo",
    "quem cedo madruga",
    "o que podes fazer hoje",
    "é ouro",
    "morreu de velho",
    "que se mudem",
    "dente por dente",
    "engorda",
    "sai caro",
    "para todos",
    "é o que não quer ouvir",
    "é o que não quer ver",
    "a casa torna",
    "meia palavra basta",
    "morre torto",
    "é refresco",
    "é que faz comida boa",
    "com ferro será ferido",
    "caça com gato",
    "tudo perde",
    "nunca chega a tostão",
    "não petisca",
    "não vê coração",
    "colhe tempestade",
    "consente",
    "seus males espanta",
    "sempre aparece",
    "não teme",
    "não mama",
    "cansa os pés",
    "aumenta um ponto",
    "ouve o que não quer",
    "não vê coração",
    "quando come se lambuza",
    "empresta a Deus",
    "dois não brigam",
    "o outro abaixa a orelha",
    "se lava em casa",
    "a montanha vai até Maomé",
    "não faz milagre",
    "não fica em pé",
    "não é documento",
    "lava a outra",
    "não quebra",
    "perdeu as botas",
    "da chuva",
    "todos os gatos são pardos",
    "a onça com vara curta",
    "na barriga da galinha",
    "do que um amigo cachorro",
    "quer comprar",
    "da voltas",
    "tem que fazer rir",
    "a te ajudar",
    "que lamba sua caceta"
    ]

#GERADOR DE DITATOS
def newProverb(initialList, finalList):
    randomNumber1 = random.randint(0, (len(initialList) - 1))
    randomNumber2 = random.randint(0, (len(finalList) - 1))
    proverb = initialList[randomNumber1] + finalList[randomNumber2]
    return proverb
#=====================================================================

#POST NO TWITTER

#chaves
consumer_key = 'YOUR_CONSUMER_KEY_HERE'
consumer_secret = 'YOUR_CONSUMER_SECRET_HERE'
token_key = 'YOUR_TOKEN_KEY_HERE'
token_secret = 'YOUR_TOKEN_SECRET_HERE'

#autenticação
consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
client = oauth2.Client(consumer, token)

#EXECUÇÃO (em loop por limitalçao do site em que está hospedado)
while True:
    query = newProverb(proverbsSource1, proverbsSource2)
    parsedQuery = urllib.parse.quote(query, safe='')
    request = client.request('https://api.twitter.com/1.1/statuses/update.json?status=' + parsedQuery, method='POST')

    #exibir no terminal
    decode = request[1].decode()
    obj = json.loads(decode)
    print(obj['created_at'])
    print(obj['text'])
    time.sleep(7000) #tempo para looping

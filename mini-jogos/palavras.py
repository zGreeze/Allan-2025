import random
# Listas

dicionario = [
    "abacate", "abandonar", "abduzir", "abencoar", "abismo", "abobora", "abraco", "abutre", "acaso", "aceitar",
    "acidente", "acucar", "admirar", "adotar", "adormecer", "adulto", "afeto", "afiar", "agito", "agora",
    "agulha", "ajuda", "alarme", "alface", "alho", "alicate", "almoço", "alugar", "amigo", "amor",
    "ampulheta", "analfabeto", "ancora", "andar", "anel", "anfitriao", "anjo", "ansiedade", "antena", "anzol",
    "apito", "aplaudir", "aprender", "aquario", "aranha", "arco", "areia", "argila", "armario", "arte",
    "asfalto", "asno", "aspirador", "astro", "ator", "atrevido", "aumentar", "aurora", "autor", "ave",
    "avenida", "aviao", "aviso", "azul", "babador", "bacana", "baderna", "bagagem", "bailar", "baixo",
    "balanco", "baleia", "bambu", "banana", "banco", "bandeira", "banho", "baralho", "barba", "barro",
    "batata", "batida", "batom", "beber", "beijo", "belo", "berco", "beringela", "besouro", "biblioteca",
    "bicicleta", "bigode", "bilhete", "biquini", "biscoito", "bloco", "blusa", "bobo", "boca", "bola",
    "bolsa", "bomba", "bondade", "boneca", "borbulha", "borracha", "bosque", "bota", "botao", "braco",
    "bravura", "brisa", "broca", "bronze", "bruxa", "bubalo", "bule", "buraco", "busca", "buzina",
    "cabana", "cabelo", "cabo", "cachoeira", "cacto", "cadeia", "caderno", "cafe", "caixa", "cajado",
    "calca", "calma", "cama", "camelo", "caminho", "camisa", "caneca", "caneta", "canoa", "cansado",
    "cantar", "capacete", "capim", "caracol", "careca", "carimbo", "carne", "carreira", "carta", "casa",
    "casaco", "cavalo", "cebola", "cedo", "cego", "cenoura", "centro", "cerca", "cerebro", "cereja",
    "certeza", "chale", "chamada", "chantilly", "chapeu", "charme", "chave", "chefe", "chegada", "cheiro",
    "chiclete", "chifre", "chinelo", "chocolate", "choque", "choro", "chuveiro", "cigarro", "cidade", "ciencia",
    "cinema", "cinza", "circo", "cobertor", "cobra", "cocada", "coelho", "cogumelo", "colher", "cometa",
    "comida", "compacto", "computador", "concerto", "concreto", "conhecer", "contar", "convite", "copo", "coracao",
    "corda", "coroa", "corpo", "correr", "corte", "corvo", "costura", "cotovelo", "couro", "cozinha",
    "crocodilo", "cruz", "cubo", "cupido", "curioso", "curto", "curva", "custoso", "dado", "dama",
    "danca", "dardo", "data", "debate", "dedo", "defeito", "degrau", "delicado", "dentista", "dentro",
    "depender", "depois", "deriva", "desafio", "descanso", "descobrir", "desenho", "deserto", "desfile", "despedir",
    "desvio", "detalhe", "diamante", "dificil", "dinamite", "dinheiro", "dinossauro", "diploma", "direito", "discurso",
    "diversao", "dividir", "doce", "doenca", "doido", "domingo", "domino", "dormente", "dormir", "dragao",
    "drama", "duende", "duque", "durante", "duvidoso", "eclipse", "economia", "edificio", "educado", "efeito",
    "eficaz", "egoista", "elefante", "elegante", "eleitor", "elogio", "embarcar", "embora", "embrulho", "emergencia",
    "emocao", "empate", "emprego", "empresa", "encaixe", "encanto", "encontro", "energia", "enfermeiro", "enfeite",
    "engolir", "enigma", "enorme", "ensaio", "entender", "entrar", "envelope", "enviar", "enzima", "epidemia",
    "episodio", "equipe", "errado", "erva", "escada", "escola", "escova", "escudo", "esfera", "esfinge",
    "espaco", "espada", "espelho", "espiga", "espinho", "esponja", "esporte", "esquadro", "estacao", "estado",
    "esteira", "estojo", "estrago", "estrela", "estudar", "eterno", "evacuar", "evento", "evitar", "exagero",
    "exame", "exato", "exemplo", "exibir", "existir", "exposto", "extenso", "extra", "extremo", "fabricar",
    "faca", "facil", "fada", "faixa", "falar", "fama", "familia", "famoso", "fantasma", "farinha",
    "farmacia", "fascinante", "favor", "faxina", "fazenda", "febre", "fechar", "feijoada", "feira", "felino"
]
dicionario += [
    "feminino", "ferradura", "ferrugem", "festa", "fiado", "fiapo", "fibra", "ficha", "figura", "filha",
    "filme", "filtro", "firme", "fita", "flanela", "flauta", "flecha", "floco", "flora", "fluido",
    "foca", "fofoca", "fogao", "foguete", "folha", "fome", "fonte", "formiga", "formula", "forte",
    "foto", "fracasso", "fraco", "fragil", "frango", "frasco", "frase", "frente", "fresta", "frio",
    "fritar", "fronha", "fruta", "fugir", "fulano", "fumar", "funcao", "fundo", "funil", "futebol",
    "futuro", "gaivota", "galho", "galinha", "galocha", "ganhar", "garagem", "garfo", "garganta", "garrafa",
    "gasoso", "gato", "gaveta", "gazela", "gelado", "gelo", "gemada", "generoso", "genio", "gente",
    "geografia", "germe", "gesso", "gigante", "girar", "giz", "glacial", "globo", "gloria", "golfe",
    "golpe", "goma", "gordo", "gorila", "gorro", "gostoso", "goteira", "governar", "graca", "grade",
    "grampo", "granada", "grande", "granizo", "grao", "gravata", "graxa", "grife", "grilo", "gritar",
    "grosso", "grupo", "guarda", "guerra", "guia", "guloso", "habilidade", "habitat", "harmonia", "haste",
    "haver", "hectare", "herdar", "heroi", "hidratar", "hiena", "higiene", "hino", "hipopetamo", "historia",
    "hobby", "hoje", "homem", "honesto", "honra", "hora", "horizonte", "hospede", "hospital", "hotel",
    "humor", "idade", "ideal", "idioma", "idoso", "igreja", "igual", "ilha", "iluminar", "imagem",
    "imenso", "imitar", "imovel", "impacto", "impedir", "imperio", "implante", "importar", "imprensa", "imprimir",
    "impulso", "incenso", "incluir", "indicar", "indice", "individuo", "indomavel", "infancia", "inferior", "infinito",
    "informar", "ingrato", "inicial", "inimigo", "inocente", "inovar", "inseto", "insistir", "instruir", "insulto",
    "inteiro", "intimo", "inundar", "inveja", "inverno", "invocar", "iogurte", "irmao", "isento", "isolado",
    "jabuti", "jaca", "jangada", "jantar", "jaqueta", "jardim", "jarro", "javali", "jazz", "jeans",
    "jeito", "jejum", "jipe", "joelho", "jogo", "jornal", "jorro", "joia", "jovem", "judoca",
    "juiz", "jujuba", "junco", "junho", "junto", "jurado", "justo", "juventude", "kart", "karate",
    "ketchup", "kilo", "kiwi", "koala", "kung", "laco", "ladrao", "lagarto", "lagoa", "laje",
    "lama", "lampada", "lance", "lanche", "lapis", "laranja", "largo", "laser", "lateral", "latido",
    "lavanda", "lavar", "lazer", "leao", "lebre", "leite", "lembrar", "leme", "lenco", "lenda",
    "lento", "leopardo", "lepra", "leste", "letra", "leve", "liberdade", "licor", "lima", "limao",
    "limite", "limpeza", "lingua", "linha", "liquidar", "lirio", "lista", "litro", "livro", "lixo",
    "lobo", "local", "locutor", "loja", "lombo", "lona", "longe", "lote", "louco", "louva",
    "lucro", "lugar", "lunar", "lustre", "luta", "luxo", "macaco", "macio", "madeira", "madrugada",
    "maestro", "magia", "magoa", "magro", "maior", "mais", "malha", "maluco", "mamao", "mancha",
    "mandato", "maneira", "manga", "manha", "manso", "manta", "manual", "mapa", "maquina", "mar",
    "maracuja", "marcha", "marfim", "margem", "marinho", "marrom", "martelo", "mascara", "massa", "matematica",
    "matinal", "mato", "matriz", "medir", "melancia", "melhor", "melodia", "menor", "mensagem", "mente",
    "mercado", "merito", "mesmo", "metal", "metro", "miado", "microfone", "milagre", "milho", "mimo",
    "mineral", "minimo", "minuto", "miolo", "mirar", "misto", "mito", "mocidade", "moda", "moderno",
    "moeda", "moinho", "mole", "momento", "monge", "monitor", "monstro", "montanha", "morder", "morrer",
    "mosaico", "mosquito", "mostrar", "motivo", "motor", "mucosa", "mudo", "mugir", "mulher", "mundo",
    "mural", "museu", "musgo", "musica", "mutacao", "muito", "nabo", "nadar", "namorar", "nariz",
    "narrar", "nascer", "natal", "natureza", "navalha", "navegar", "nebuloso", "neblina", "nectar", "negar",
    "negocio", "negro", "nenhum", "nevasca", "neve", "nervoso", "neto", "neutro", "nevoeiro", "nexo",
    "ninho", "nitido", "nivel", "nobre", "noite", "nomade", "nome", "normal", "norte", "nota",
    "notavel", "noturno", "novela", "novembro", "novo", "nublado", "nudez", "numeral", "nunca", "nupcial",
    "nutrir", "nuvem", "obeso", "objeto", "obra", "obrigado", "ocultar", "ocupar", "ocorrer", "oculto",
    "oeste", "ofensa", "oficial", "oficina", "ofuscar", "olhar", "oliva", "ombro", "omitir", "onda",
    "ondular", "ontem", "opaco", "opcao", "opera", "opinar", "oposto", "orar", "orbe", "ordem",
    "orelha", "orfao", "orgulho", "oriente", "origem", "orla", "orsamento", "ortiga", "oscilar", "osso"
]
dicionario += [
    "pacato", "paciente", "pacote", "padre", "pagina", "pais", "palavra", "palco", "palha", "palhaco",
    "palmeira", "palpite", "panela", "papel", "parabens", "parceiro", "parede", "partir", "passado", "pasta",
    "pata", "patente", "patria", "pausa", "pavao", "pedal", "pedido", "pedra", "pegada", "peixe",
    "pele", "perigo", "perola", "perto", "pesado", "pessoa", "petala", "picada", "piedade", "pigmento",
    "pilha", "pimenta", "pincel", "pinguim", "pinha", "pino", "pintura", "piolho", "pioneiro", "pipa",
    "piranha", "pistola", "pizza", "placa", "planeta", "planta", "plastico", "pobre", "poco", "podar",
    "poder", "poema", "poesia", "polaroid", "polegar", "policia", "polo", "pomba", "pombo", "ponte",
    "ponto", "porta", "pose", "poste", "pote", "pousada", "povoar", "praca", "prado", "prata",
    "praia", "prancha", "prato", "prece", "preco", "predio", "pregar", "preguica", "prenda", "preparar",
    "presente", "presidente", "pressa", "pretexto", "prevenir", "prezar", "primavera", "primo", "principe", "prisma",
    "problema", "processo", "produto", "professor", "profundo", "programa", "promessa", "pronto", "prova", "proximo",
    "pudim", "pular", "pulga", "pulso", "pulmao", "punhal", "punho", "puxar", "quadra", "quadro",
    "quantidade", "quarenta", "quarto", "quebrar", "queda", "queijo", "quente", "querer", "questao", "quieto",
    "quilo", "quimera", "quina", "quintal", "quiosque", "quiproquo", "quitanda", "quimica", "rabisco", "rachar",
    "radar", "radical", "raiar", "rainha", "raio", "raiva", "raiz", "ralado", "ramal", "rampa",
    "rancor", "ranger", "rapaz", "rapidez", "raquete", "raridade", "rasgar", "rastro", "rato", "razao",
    "reacao", "real", "rebelde", "recado", "recente", "recheio", "recibo", "recordar", "recruta", "redacao",
    "redondo", "reduzir", "refeicao", "refletir", "refogar", "reforma", "refugio", "regador", "regime", "regra",
    "reinado", "reitor", "rejeitar", "relevo", "reliquia", "remedio", "remendo", "remeter", "remoto", "render",
    "renovar", "reparo", "repente", "repleto", "reportar", "repouso", "represa", "repudiar", "requerer", "reserva",
    "resgate", "residir", "resolver", "respeito", "resposta", "ressaca", "restante", "resumir", "retirar", "retorno",
    "reunir", "revelar", "revisar", "revolta", "riacho", "rica", "rifle", "rigido", "rigor", "rimar",
    "rio", "riqueza", "risada", "risco", "ritmo", "rival", "robusto", "rochedo", "rodada", "rodela",
    "rodovia", "roedor", "roleta", "romance", "romper", "roncar", "rosa", "rosca", "rosto", "roteiro",
    "rotina", "rotulo", "roupa", "roxo", "rubro", "ruga", "rugido", "ruido", "ruina", "ruivo",
    "rumo", "ruptura", "russo", "sabao", "saber", "sabor", "sacada", "sacar", "sadio", "safra",
    "saga", "sagrado", "saida", "salada", "salario", "salgar", "saliva", "salmo", "salto", "salvar",
    "samba", "sanfona", "sangue", "sanidade", "sapo", "sapato", "sarampo", "sarda", "sardinha", "saudade",
    "sauna", "saxofone", "sebo", "seca", "secreto", "secular", "sede", "sedoso", "sedutor", "segmento",
    "segredo", "segundo", "seguro", "seiva", "selado", "seleto", "selo", "selva", "semana", "semente",
    "senador", "sensato", "sentido", "separar", "sepultar", "sequela", "sereia", "sereno", "serio", "serpente",
    "serra", "servo", "seta", "setor", "sigilo", "silaba", "silhueta", "silicio", "simples", "simular",
    "sinal", "sincero", "singular", "sinopse", "sintonia", "sirene", "siso", "sistema", "sitio", "social",
    "socorro", "sofrer", "sogro", "solo", "soltar", "soneto", "sonhar", "sono", "soprano", "sorrir",
    "sorte", "sossego", "sotaque", "sovar", "suave", "subida", "sublime", "suborno", "sucesso", "suco",
    "sudeste", "sufixo", "sufocar", "sugerir", "sujeito", "sulfato", "sumir", "suor", "superar", "suplemento",
    "supremo", "suprimir", "surdina", "surpresa", "surreal", "surtir", "suspiro", "sussurro", "susto", "sutil",
    "tabela", "tabique", "tablado", "tabu", "tacho", "tactica", "talento", "talher", "talo", "tambor",
    "tampinha", "tangente", "tanto", "tapar", "tapioca", "tarde", "tarefa", "tarifa", "tartaruga", "tatuar",
    "taverna", "taxar", "teatro", "tecido", "teclado", "tedioso", "teflon", "telha", "tema", "tempo",
    "tenaz", "tendencia", "tenente", "tensor", "tentativa", "termo", "ternura", "terra", "tesoura", "teste",
    "teto", "textura", "tigela", "tijolo", "timbrar", "timido", "tingir", "tinta", "tirar", "titular",
    "toalha", "tocar", "tolerar", "tomada", "tomilho", "toner", "tontura", "topar", "toranja", "torcer",
    "tormenta", "torneio", "torpor", "torrar", "torto", "tostar", "touro", "toxina", "trabalho", "tracao",
    "trafego", "trajeto", "trama", "trancar", "transe", "trapo", "traseiro", "tratar", "trave", "treco",
    "tremer", "trepar", "trevo", "tribo", "trigo", "trilho", "triplo", "triste", "triunfo", "trocar",
    "trombeta", "tronco", "tropa", "trovao", "trunfo", "truque", "tubular", "tucano", "tudo", "tulipa",
    "tumor", "tunisio", "turbo", "turma", "turno", "tutelar", "tutoria", "uivar", "ulcera", "ultraje",
    "umbigo", "umidade", "unico", "unidade", "unir", "universo", "untado", "urgente", "urna", "urso",
    "urubu", "usado", "usina", "utero", "util", "utopia", "vaca", "vacina", "vadiar", "vagaroso",
    "vaidoso", "vala", "valente", "validade", "valor", "vantagem", "vaporoso", "vaqueiro", "varanda", "varejo",
    "variante", "varredor", "vaso", "vasto", "vazao", "vegetal", "veicular", "veiculo", "vela", "veleiro",
    "veludo", "vencedor", "vendaval", "veneno", "ventar", "verbal", "verdade", "vereda", "vergonha", "vermelho",
    "verniz", "versar", "vertente", "vesgo", "vestido", "veto", "vexame", "viagem", "vibrar", "vidro",
    "viela", "vigarice", "vigoroso", "vila", "vime", "vindouro", "vinha", "violar", "violeta", "virar",
    "virose", "virtude", "visita", "visto", "vital", "vitamina", "vitrola", "vitrine", "viveiro", "vizinho",
    "voador", "voar", "vocabulo", "vociferar", "voga", "volante", "voltar", "volume", "vontade", "vulcao",
    "vulto", "xadrez", "xarope", "xerife", "xingar", "zambia", "zebra", "zelador", "zero", "ziguezague",
    "zinco", "zoar", "zona", "zoologico", "zumbi"
]
alfabeto = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]

# Substituir a lista pelas letras

def substituir(letra):
    quantidade = palavra.count(letra)
    inicio = 0
    for i in range(quantidade):
        lugar = palavra.find(letra, inicio, tamanho)
        listprov[lugar] = letra.upper()
        inicio = lugar + 1
    print("  ".join(listprov))

#Repetir
jogar = True

while jogar == True:
    # Setup
    ind = random.randint(0,1394)
    palavra = dicionario[ind]
    listprov = []
    tamanho =len(palavra)
    for u in range(tamanho):
        listprov.append("_")
    resposta = []
    for r in range (tamanho):
        resposta.append(palavra[r].upper())
    erros = 0

    # Escolher dificuldade

    print("\n------------------------------Escolha sua dificuldade------------------------------")
    print("1 - facil                                15 erros")
    print("2 - médio                                10 erros")
    print("3 - difícil                               5 erros")
    print("4 - personalizado")
    print("0 - livre")
    print()
    dificuldade = int(input("--------------> "))
    while True:
        if dificuldade == 1:
            erros = 15
            break
        elif dificuldade == 2:
            erros = 10
            break
        elif dificuldade == 3:
            erros = 5
            break
        elif dificuldade == 0:
            erros = 1000
            break
        elif dificuldade == 4:
            erros = int(input("Insira um limite de erros (entre 1 a 25): "))
            while erros < 1 or erros > 25:
                erros = int(input("Insira um limite de erros valido (entre 1 a 25): "))
            break
        else:
            dificuldade = int(input("Insira uma dificuldade valida: \n------------> "))


    # Jogar

    print()
    print("  ".join(listprov))
    print()
    while (listprov != resposta) and (erros > 0):
        letrinha = str(input("insira uma letra:\n")).lower()
        while (letrinha.upper() in listprov) or (len(letrinha.upper()) > 1) or (letrinha.upper() not in alfabeto):
            print("\n               letras disponiveis: ", " ".join(alfabeto))
            letrinha = str(input("insira uma letra que esteja disponivel:\n"))
        substituir(letrinha)
        alfabeto.remove(letrinha.upper())
        print("\n               letras disponiveis: "," ".join(alfabeto))
        if palavra.find(letrinha.lower()) == -1:
            erros -= 1
        if erros < 26:
            print(f"Erros restantes = {erros}")
    if erros == 0:
        print(f"\n\nVoce perdeu, a palavra era: [{palavra.title()}].\n\nTente novamente!")
    else:
        print(f"\n\nVoce acertou conseguiu acertar ,a palavra era [{palavra.title()}].\nParabens!")

    print("\n-------------------Jogar Novamente?------------------")
    print("\n1 - sim")
    print("Qualquer outra tecla - não")
    escolha_jogar = str(input("--------> "))
    if escolha_jogar == "1":
        Jogar = True
    else:
        jogar = False
    alfabeto = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
print("\n\n------------------------------------------OBRIGADO POR JOGAR----------------------------------------\n\n\n")
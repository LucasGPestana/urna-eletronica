import datetime, os , time, tkinter

def limpaTela():
    
    os.system('cls') or None

def ordenar_candidatos(candidato):
    return candidato['votos']

def contagemDeVotos():
    for candidato in candidatos:
        candidato['votos'] = votos_confirmados.count(candidato['numero'])

def realizarClassificacao():

    ranking = sorted(candidatos, key=ordenar_candidatos, reverse=True)

    return ranking

def mostrarRanking():

    pos = 0

    for candidato in ranking:

        pos += 1

        txt_rank['text'] += f"{pos} - {candidato['nome']}, com {candidato['votos']}\n"
    
def isValidDay():

    data_atual = datetime.date.today()

    if data_atual.ctime()[0:3] == 'Thu':
        return True
    else:
        print("Hoje não é domingo!")
        return False

def isValidTime():

    data_atual = datetime.date.today()

    dia_atual = data_atual.day
    mes_atual = data_atual.month
    ano_atual = data_atual.year

    horario_atual = datetime.datetime.now()
    horario_final = datetime.datetime(ano_atual, mes_atual, dia_atual, 18, 0, 0)

    if horario_atual >= horario_final:
        print("As eleições se encerraram!")
        return False
    else:
        dif_horario = horario_final - horario_atual
        print(f"Ainda faltam {dif_horario} para encerrar as eleições")
        return True

def criarArquivoEleitores():

    arq_info_ele = open('info/eleitores.txt', 'w')

    for eleitor in info_eleitores:
        arq_info_ele.write(f"{eleitor[0]}  {eleitor[1]} {eleitor[2]}\n")

    arq_info_ele.close()

def criarArquivoCandidatos():

    arq_info_cand = open('info/candidatos.txt', 'w')

    pos = 0

    for candidato in ranking:

        pos += 1

        arq_info_cand.write(f"{pos} - {candidato['nome']}, com {candidato['votos']}\n")

    arq_info_cand.close()
        
candidatos = [dict(nome="Bolsonaro", numero = "22", votos=0), 
                  dict(nome="Lula", numero="13", votos=0),
                  dict(nome="Ciro", numero="12", votos=0)]

votos_confirmados = list()

info_eleitores = list()

num_eleitores = 0

while True:

    if isValidDay():

        if isValidTime():

            limpaTela()

            while True:

                limpaTela()

                num_eleitores += 1

                nome = input("Digite seu primeiro nome: ")

                if not(nome.isalpha()):
                    print("Nome inválido! Digite-o novamente!")
                    time.sleep(5)
                    limpaTela()
                else:
                    break

            while True:

                cpf = input("Digite seu CPF: ")

                if len(cpf) == 11 or len(cpf) == 14:
                    if ("." in cpf) and ("-" in cpf):
                        if cpf[0:3].isnumeric() and cpf[4:7].isnumeric() and cpf[8:11].isnumeric() and cpf[12:14].isnumeric():
                            cpf = cpf[0:3] + cpf[4:7] + cpf[8:11] + cpf[12:14]
                            break
                        else:
                            print("CPF inválido! Digite-o novamente!")
                            time.sleep(5)
                            limpaTela()
                    else:
                        if cpf.isnumeric():
                            break
                        else:
                            print("CPF inválido! Digite-o novamente!")
                            time.sleep(5)
                            limpaTela()
                else:
                    print("Esse CPF não atende a quantidade correta! Digite-o novamente!")
                    time.sleep(5)
                    limpaTela()
  
            for candidato in candidatos:

                nome_candidato, numero_candidato, votos_candidato = candidato.items()

                print(f"{nome_candidato} - {numero_candidato}".center(50))

            candidato_escolhido = input("Digite o número de seu candidato: ")

            if num_eleitores == 1:

                votos_confirmados.append(candidato_escolhido)

                info_eleitores.append((cpf, nome, candidato_escolhido))

                print("Voto Confirmado! Obrigado!")
                print("Por favor, espere 10 segundos!")

                time.sleep(10)
            
            else:

                if not(cpf in info_eleitores[0]):

                    votos_confirmados.append(candidato_escolhido)

                    info_eleitores.append((cpf, nome, candidato_escolhido))

                    print("Voto Confirmado! Obrigado!")
                    print("Por favor, espere 10 segundos!")

                    time.sleep(10)

                else:
                    print("Esse CPF consta como já votado!")
                    time.sleep(5)
                    limpaTela()
        else:
            break
    else:
        break

contagemDeVotos()

ranking = realizarClassificacao()

window_winner = tkinter.Tk()
window_winner.geometry('40x20')
window_winner.title("Vencedor da Eleição")

txt_vencedor = tkinter.Label(window_winner, text=f"{ranking[0]['nome']} venceu!")
txt_vencedor.grid(column=0, row=0)

window_winner.mainloop()

window_rank = tkinter.Tk()
window_rank.title("Ranking Final")

txt_rank = tkinter.Label(window_rank, text="")
txt_rank.grid(column=0, row=0)

mostrarRanking()

window_rank.mainloop()

criarArquivoEleitores()

criarArquivoCandidatos()

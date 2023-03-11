import datetime, os , time, tkinter, re

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

    for pos, candidato in enumerate(ranking):

        txt_rank['text'] += f"{pos + 1} - {candidato['nome']}, com {candidato['votos']}\n"
    
def isValidDay():

    data_atual = datetime.date.today()

    if data_atual.ctime()[0:3] == 'Sat':
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

    for pos, candidato in enumerate(ranking):

        arq_info_cand.write(f"{pos + 1} - {candidato['nome']}, com {candidato['votos']}\n")

    arq_info_cand.close()
        
candidatos = [dict(nome="Bolsonaro", numero = "22", votos=0), 
                  dict(nome="Lula", numero="13", votos=0),
                  dict(nome="Ciro", numero="12", votos=0)]

votos_confirmados = list()

info_eleitores = list()

num_eleitores = 0

def validarInformacoes():

    nome = input_nome.get()

    padrao_nome = re.compile("^[\S][a-zA-Z\s\D]+")

    if re.fullmatch(padrao_nome, nome) == None:
        res_nome['text'] = "Nome inválido! Digite-o novamente!"
    else:
        num_eleitores += 1

    cpf = input_cpf.get()

    if len(cpf) == 11 or len(cpf) == 14:
        if ("." in cpf) and ("-" in cpf):
            if cpf[0:3].isnumeric() and cpf[4:7].isnumeric() and cpf[8:11].isnumeric() and cpf[12:14].isnumeric():
                cpf = cpf[0:3] + cpf[4:7] + cpf[8:11] + cpf[12:14]
                
            else:
                input_cpf['text'] = "CPF inválido! Digite-o novamente!"
        else:
            if not(cpf.isnumeric()):
                input_cpf['text'] = "CPF inválido! Digite-o novamente!"
    else:
        input_cpf['text'] = "Esse CPF não atende a quantidade correta! Digite-o novamente!"
  
    for candidato in candidatos:

        nome_candidato, numero_candidato, votos_candidato = candidato.items()

        print(f"{nome_candidato} - {numero_candidato}".center(50))


    candidato_escolhido = input("Digite o número de seu candidato: ")

    for candidato in candidatos:

        nome_candidato, numero_candidato, votos_candidato = candidato.values()

        if candidato_escolhido == numero_candidato:
            exist_candidato = True
        else:
            continue

    if not(exist_candidato):
        res_num_cand['text'] = "O número desse candidato não consta no sistema! Digite-o novamente!"

    if num_eleitores == 1 and exist_candidato:

        votos_confirmados.append(candidato_escolhido)

        info_eleitores.append((cpf, nome, candidato_escolhido))

        res_confirmar['Text'] = "Voto Confirmado! Obrigado!"
        res_confirmar['Text'] += "Por favor, espere 10 segundos!"

        time.sleep(10)

        window_eleitores.destroy()
            
    else:

        if not(cpf in info_eleitores[0]):

            votos_confirmados.append(candidato_escolhido)

            info_eleitores.append((cpf, nome, candidato_escolhido))

            res_confirmar['Text'] = "Voto Confirmado! Obrigado!"
            res_confirmar['Text'] += "Por favor, espere 10 segundos!"

            time.sleep(10)

            window_eleitores.destroy()

        else:
            res_cpf['Text'] = "Esse CPF consta como já votado!"
            num_eleitores -= 1

while True:

    exist_candidato = False

    limpaTela()

    if isValidDay():

        if isValidTime():

        # Janela para realizar voto

            font_family = ("Arial 10")
            font_color = "#FFFFFF"
            background = "#1e1e1e"

            window_eleitores = tkinter.Tk()
            window_eleitores.title("Realizar Voto")
            window_eleitores.geometry("400x300")
            window_eleitores.configure(background="#1e1e1e")


            # Campo Nome
            txt_nome = tkinter.Label(master=window_eleitores, text="Nome do Eleitor", anchor='w', font=font_family , bg=background, fg=font_color)
            txt_nome.grid(row=0, column=0, padx=5, pady=10)

            input_nome = tkinter.Entry(master=window_eleitores, bg="#DADADA")
            input_nome.grid(row=1, column=0, padx=5, pady=5)

            res_nome = tkinter.Label(master=window_eleitores, bg=background, fg="FF0000", text="")
            res_nome.grid(row=2, column=0, padx=5, pady=5)


            # Campo CPF
            txt_cpf = tkinter.Label(master=window_eleitores, text="CPF", anchor='w', font=font_family, bg=background, fg=font_color)
            txt_cpf.grid(row=3, column=0, padx=5, pady=5)

            input_cpf = tkinter.Entry(master=window_eleitores, bg="#DADADA")
            input_cpf.grid(row=4, column=0, padx=5, pady=5)

            res_cpf = tkinter.Label(master=window_eleitores, fg="00FF00", text="", bg="FF0000")
            res_cpf.grid(row=5, column=0, padx=5, pady=5)


            # Campo Número do Candidato
            txt_num_cand = tkinter.Label(master=window_eleitores, text="Número do Candidato", anchor='w', font=font_family, bg=background, fg=font_color)
            txt_num_cand.grid(row=6, column=0, padx=5, pady=5)

            input_num_cand = tkinter.Entry(master=window_eleitores, bg="#DADADA", width="2", font=("Arial 25"))
            input_num_cand.grid(row=7, column=0, padx=5, pady=5)

            res_num_cand = tkinter.Label(master=window_eleitores, bg=background, fg="FF0000", text="")
            res_num_cand.grid(row=8, column=0, padx=5, pady=5)

            # Campo Cofirmar
            btn_confirmar = tkinter.Button(master=window_eleitores, text="Confirmar", command=validarInformacoes, borderwidth=5)
            btn_confirmar.grid(row=9, column=2)

            res_confirmar = tkinter.Label(master=window_eleitores, text="", bg=background, fg=font_color)

            window_eleitores.mainloop()

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

txt_rank = tkinter.Label(window_rank, text=f"Ao todo, tivemos {num_eleitores} eleitores\n")
txt_rank.grid(column=0, row=0)

mostrarRanking()

window_rank.mainloop()

criarArquivoEleitores()

criarArquivoCandidatos()

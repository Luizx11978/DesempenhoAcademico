import tkinter as tk

# variaveis
mediaDesejada = 0
disciplinas = []
labelsDinamicas = []

# aqui a gente fez a funçãop para adicionar a disciplina e a nota em uma label, no frame1
# dai o user pode ver o que ele adicionou

def adicionarDisciplina():
    disciplina = entradaDisciplina.get()
    nota = entradaNota.get()

    if disciplina != "" and nota != "":
        # aqui a gente jogou a disciplina e a nota ( como float )
        disciplinas.append((disciplina, float(nota)))
        # agora a gente cria a label que vai ter a nota e a disciplinas
        labelDados = tk.Label(frame1,width=100, text=f"{disciplina}   :   {nota}", bg="#111111", fg="white", font=("Arial", 13),bd=1,relief="sunken")
        labelDados.pack(side=tk.TOP, pady=2, padx=2)

        # no final limpa o campo de entrada
        entradaDisciplina.delete(0, tk.END)  
        entradaNota.delete(0, tk.END) 
        
        # Adicionar a label na lista de labels dinâmicas
        labelsDinamicas.append(labelDados)

        mediaFinal()
        

def adicionar_media():
    global mediaDesejada
    mediaDesejada = entradaMediaDesejada.get()
    mediaDesejada = float(mediaDesejada)
    labelMediaDesejada.configure(text=f"{mediaDesejada:.2f}")

    entradaMediaDesejada.delete(0, tk.END)

    mediaFinal()

# aqui vai ser a função para fazer a média final
def mediaFinal():
    soma = 0
    
    # aqui é a soma de todas as notas do array
    for disciplina, nota in disciplinas:
        soma += nota
    # dai aqui é a condição, se o tamanho do array disciplinas for maior que 0 ele executa a media final
    if len(disciplinas)>0:
        mediaF = soma/len(disciplinas)
    else:
        mediaF = 0
    
    if mediaF >= mediaDesejada:
        labelAprovado.config(text="APROVADO")
    else:
        labelAprovado.config(text="RECUPERAÇÃO")

    # a gente fez aqui a troca do texto da label, e colocou o :.2F para que as casas decimais depois da virgula seja apena 2
    labelMediaF.config(text=f"Media final : {mediaF:.2f}")

# funcao de limpar tudo :)
def limpar():
    global mediaDesejada,disciplinas
    disciplinas = []
    mediaDesejada = 0
    
    #for para remover labels da tela, usando o metdo destroy()
    for label in labelsDinamicas:
        label.destroy()

    #aqui a gente limpa a lista após remover as labels
    print(labelsDinamicas)
    labelsDinamicas.clear()

    labelMediaDesejada.config(text="Não inserido")  # Média inicial (pode ser alterada conforme necessário)
    labelMediaF.config(text="0.00")
    labelAprovado.config(text="")


janela = tk.Tk()

janela.title("Desempenho Academico")
janela.geometry("1000x700")
janela.configure(bg="#111111")

Titulo = tk.Label(janela, text="Calculadora Acadêmica",font=("Arial", 20),fg="#FF8383",bg="#111111")
Titulo.pack(pady=20)
Desc = tk.Label(janela, text="Aplicativo de desempenho acadêmico",font=("Arial", 12),fg="white",bg="#111111")
Desc.pack(pady=20)



# criamos esses frames para dividir os blocos 
# FRAME 1
frame1 = tk.Frame(janela,width=300, height=600, bg="#111111", relief="solid",bd=1, highlightbackground="white", highlightthickness=1)
frame1.pack(side=tk.LEFT, padx=10, pady=10, expand=True)
frame1.pack_propagate(False)

labelTabela = tk.Label(frame1, text="DISCIPLINAS", bg="#111111", fg="lightBlue", font=("Arial", 16))
labelTabela.pack(pady=20)


# FRAME 2
frame2 = tk.Frame(janela,width=300, height=600, bg="#111111", relief="solid",bd=1, highlightbackground="white", highlightthickness=1)
frame2.pack(side=tk.LEFT, padx=10, pady=10, expand=True)
frame2.pack_propagate(False)

labelResultado = tk.Label(frame2, text="RESULTADO", bg="#111111", fg="lightGreen", font=("Arial", 16))
labelResultado.pack(pady=20)

TituloMediaDesejada = tk.Label(frame2, text="Media Desejada",bg="#111111", fg="white", font=("Arial", 13, "bold"))
TituloMediaDesejada.pack(pady=5, padx=20)

labelMediaDesejada = tk.Label(frame2,width=20,height=2, text="Não inserido",  bg="green", fg="white", font=("Arial", 15, "bold"))
labelMediaDesejada.pack(pady=5, padx=20)

TituloMediaF = tk.Label(frame2, text="Media Final",bg="#111111", fg="white", font=("Arial", 13, "bold"))
TituloMediaF.pack(pady=5, padx=20)

labelMediaF = tk.Label(frame2,width=20,height=2, text="0",  bg="white", fg="green", font=("Arial", 15, "bold"))
labelMediaF.pack(pady=5, padx=20)

labelAprovado = tk.Label(frame2,width=20,height=2, text="APROVADO", bg="white", fg="green", font=("Arial", 15, "bold"))
labelAprovado.pack(pady=5, padx=20)

# divisor
divisor = tk.Frame(frame2,height=3, bg="#495457")
divisor.pack(pady=10,fill=tk.X)


botao = tk.Button(frame2, text="Limpar", command=limpar ,fg="black", bg="yellow", font=("Arial", 16),height=1, width=20)
botao.pack(pady=10,padx=10)






# FRAME 3
frame3 = tk.Frame(janela,width=300, height=600, bg="#111111", relief="solid",bd=1, highlightbackground="white", highlightthickness=1)
frame3.pack(side=tk.LEFT, padx=10, pady=10, expand=True)
frame3.pack_propagate(False)


labelAddNotas = tk.Label(frame3, text="Adicionar Notas", bg="#111111", fg="yellow", font=("Arial", 16))
labelAddNotas.pack(pady=20)

# entrada de disciplina
labelInputDisciplina = tk.Label(frame3, text="Adicionar Disciplina", bg="#111111", fg="white", font=("Arial", 12))
labelInputDisciplina.pack(pady=0)

entradaDisciplina = tk.Entry(frame3, font=("Arial", 16))
entradaDisciplina.pack(pady=10,padx=10)

# entrada de npta da disciplina
labelInputNota = tk.Label(frame3, text="Adicionar Nota", bg="#111111", fg="white", font=("Arial", 12))
labelInputNota.pack(pady=0)

entradaNota = tk.Entry(frame3, font=("Arial", 16))
entradaNota.pack(pady=10,padx=10)

# Botão 
botao = tk.Button(frame3, text="Adicionar", command=adicionarDisciplina,fg="black", bg="yellow", font=("Arial", 16),height=1, width=20)
botao.pack(pady=10,padx=10)


# divisor
divisor = tk.Frame(frame3,height=3, bg="#495457")
divisor.pack(pady=10,fill=tk.X)


TituloMediaDesejada = tk.Label(frame3, text="Média Desejada", bg="#111111", fg="yellow", font=("Arial", 16))
TituloMediaDesejada.pack(pady=20)

# aqui é aonde o usuaurio altera a media desejada

labelInputDisciplina = tk.Label(frame3, text="Adicionar Média", bg="#111111", fg="white", font=("Arial", 12))
labelInputDisciplina.pack(pady=0)

entradaMediaDesejada = tk.Entry(frame3, font=("Arial", 16))
entradaMediaDesejada.pack(pady=10,padx=10)
 
botao = tk.Button(frame3, text="Adicionar", command=adicionar_media,fg="black", bg="yellow", font=("Arial", 16),height=1, width=20)
botao.pack(pady=10,padx=10)
janela.mainloop()
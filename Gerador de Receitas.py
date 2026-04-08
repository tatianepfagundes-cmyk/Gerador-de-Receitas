import tkinter as tk
import random

# Banco de Receitas
Receitas_salgadas = {
    'ovo':["omelete", "ovo mexido","ovo cozido"],
    'arroz':["arroz branco","arroz a grega","arroz carreteiro"],
    'macarrão':["macarrão ao alho e óleo", "macarrão com molho branco","macarrão à bolonhesa"],
    'frango':["frango grelhado", "frango assado","frango ao curry"],
    'carne':["bife acebolado", "carne de panela","carne moída", "strogonoff de carne"],
    'batata':["batata frita", "purê de batata","batata assada"],
    'legumes':["legumes refogados", "legumes assados","sopa de legumes"],
    'salada':["salada verde", "salada tropical","salada tomate e cebola"],
    'peixe':["peixe grelhado", "peixe assado", "peixe frito"],
    'feijão':["feijão preto", "feijoada", "feijão tropeiro"],
    'tomate':["molho de tomate", "salada de tomate", "tomate recheado"],
    'cebola':["cebola caramelizada", "cebola frita", "sopa de cebola"],
    'alho':["alho assado", "pão com alho"],
    'cogumelo':["cogumelos refogados", "risoto de cogumelos", "sopa de cogumelos"],
    'abóbora':["abóbora assada", "sopa de abóbora", "purê de abóbora"],
    'cenoura':["cenoura refogada", "sopa de cenoura", "cenoura assada"],
    'espinafre':["espinafre refogado", "torta de espinafre", "pastel assado de espinafre com queijo"],
    'farinha':["bolo simples", "biscoito", "torta salgada", "pão caseiro"],
    'presunto':["sanduíche de presunto", "presunto com melão"],
    'atum':["atum assado", "salada de atum", "atum com maionese"],
    'milho':["milho cozido", "sopa de milho", "bolo de milho"],
    'berinjela':["berinjela assada", "berinjela à parmegiana", "berinjela refogada"],
    'pimentão':["pimentão recheado", "pimentão assado"],
    'brocolis':["brocolis ao vapor", "brocolis gratinado", "sopa de brocolis"],
    'couve':["couve refogada", "couve mineira", "salada de couve"],
    'lentilha':["sopa de lentilha", "lentilha com bacon", "salada de lentilha"],
    'quinoa':["quinoa cozida", "salada de quinoa", "quinoa com legumes"],
    'salmão':["salmão grelhado", "salmão assado"],
    'camarão':["camarão ao alho", "camarão refogado", "risoto de camarão"],
}

Receitas_doces = {
    'chocolate':["bolo de chocolate", "mousse de chocolate", "brownie"],
    'banana':["banana assada", "bolo de banana", "banana caramelizada"],
    'leite condensado':["pudim", "brigadeiro", "beijinho"],
    'coco':["bolo de coco", "pudim de coco"],
    'abacaxi':["bolo de abacaxi", "calda de abacaxi", "abacaxi caramelizado"],
    'limão':["bolo de limão", "mousse de limão", "pavê de limão"],
    'goiaba':["goiabada", "bolo de goiaba", "pasta de goiaba with queijo"],
    'maçã':["torta de maçã", "bolo de maçã", "maçã assada com sorvete"],
    'canela':["bolo de canela", "rosca doce de canela"],
    'café':["mousse de café", "tiramisú"],
    'mel':["pudim de mel", "bolo com mel", "maçã caramelizada com mel"],
    'biscoito':["pavê", "torta de bolacha"],
    'laranja':["bolo de laranja", "suco de laranja", "geleia de laranja"],
    'pera':["pera assada", "torta de pera", "compota de pera"],
    'pêssego':["pêssego em calda", "torta de pêssego", "pêssego assado"],
    'manga':["manga com leite condensado", "suco de manga", "mousse de manga"],
    'baunilha':["bolo de baunilha", "pudim de baunilha", "sorvete de baunilha"],
    'nozes':["bolo de nozes", "torta de nozes", "nozes caramelizadas"],
}

# Função gerar receitas
def gerar_receitas():
    ingredientes = campo.get().lower().split(",")
    sugestoes_salgadas = set()
    sugestoes_doces = set()
    invalidos = []

    for ingrediente in ingredientes:
        ingrediente = ingrediente.strip()

        if ingrediente in Receitas_salgadas:
            sugestoes_salgadas.add(random.choice(Receitas_salgadas[ingrediente]))
        elif ingrediente in Receitas_doces:
            sugestoes_doces.add(random.choice(Receitas_doces[ingrediente]))
        else:
            if ingrediente:
                invalidos.append(ingrediente)
    
    texto = ""
    if sugestoes_salgadas:
        texto += "🍖 PRATOS PRINCIPAIS:\n"
        texto += "-" * 40 + "\n"
        for s in sorted(sugestoes_salgadas):
            texto += "  ✓ " + s + "\n"
    
    if sugestoes_doces:
        if texto:
            texto += "\n"
        texto += "🍰 SOBREMESAS:\n"
        texto += "-" * 40 + "\n"
        for s in sorted(sugestoes_doces):
            texto += "  ✓ " + s + "\n"
    
    if not sugestoes_salgadas and not sugestoes_doces:
        texto = "❌ Nenhuma receita encontrada.\n\n"
        texto += "Clique em 'Ver Ingredientes' para ver as opções disponíveis."

    if invalidos:
        if texto:
            texto += "\n"
        texto += "⚠️  Ingredientes não encontrados:\n"
        texto += "-" * 40 + "\n"
        for i in invalidos:
            texto += "  ✗ " + i + "\n"
    
    resultado.config(state=tk.NORMAL)
    resultado.delete("1.0", tk.END)
    resultado.insert("1.0", texto)
    resultado.config(state=tk.DISABLED)

#Limpar campo
def limpar_campo():
     campo.delete(0, tk.END)
     resultado.config(state=tk.NORMAL)
     resultado.delete("1.0", tk.END)
     resultado.config(state=tk.DISABLED)

#Ver ingredientes disponíveis
def ver_ingredientes():
    resultado.config(state=tk.NORMAL)
    resultado.delete("1.0", tk.END)
    
    salgados = sorted(Receitas_salgadas.keys())
    doces = sorted(Receitas_doces.keys())
    
    texto = "INGREDIENTES DISPONÍVEIS\n"
    texto += "=" * 40 + "\n\n"
    texto += "PRATOS PRINCIPAIS:\n"
    for ing in salgados:
        texto += f"  • {ing}\n"
    
    texto += "\n" + "=" * 40 + "\n\n"
    texto += "SOBREMESAS:\n"
    for ing in doces:
        texto += f"  • {ing}\n"
    
    texto += "\n" + "=" * 40 + "\n"
    texto += "(Digite os ingredientes separados por vírgula)"
    
    resultado.insert("1.0", texto)
    resultado.config(state=tk.DISABLED)

# Criando Janela
janela = tk.Tk()
janela.title("Gerador de Receitas")
janela.geometry("600x700")
janela.configure(bg="#2c3e50")

# Header com fundo colorido
header = tk.Frame(janela, bg="#34495e", height=80)
header.pack(fill=tk.X, padx=0, pady=0)

# Linha decorativa superior
linha_superior = tk.Label(header, text="═" * 50, 
                         font=("Arial", 10), bg="#34495e", fg="#f39c12")
linha_superior.pack(pady=(5, 0))

# Título principal
frame_titulo = tk.Frame(header, bg="#34495e")
frame_titulo.pack(expand=True)

# Container centralizado
container = tk.Frame(frame_titulo, bg="#34495e")
container.pack(anchor="center")

emoji_esquerda = tk.Label(container, text="✨🍽️", bg="#34495e", fg="#f1c40f", font=("Segoe UI Emoji", 20))
emoji_esquerda.pack(side="left")

titulo = tk.Label(container, text="GERADOR DE RECEITAS", 
                  font=("Arial", 20, "bold"), bg="#34495e", fg="#f1c40f")
titulo.pack(side="left", padx=5)

emoji_direita = tk.Label(container, text="🍰✨", bg="#34495e", fg="#f1c40f", font=("Segoe UI Emoji", 20))
emoji_direita.pack(side="left")

# Linha decorativa inferior
linha_inferior = tk.Label(header, text="═" * 50, 
                         font=("Arial", 10), bg="#34495e", fg="#f39c12")
linha_inferior.pack(pady=(0, 5))

#Container principal (frame)
frame_principal = tk.Frame(janela, bg="#2c3e50")
frame_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Subtítulo
subtitulo = tk.Label(frame_principal, text="Digite seus ingredientes (separados por vírgula):", 
                     font=("Arial", 12, "bold"), bg="#2c3e50", fg="white")
subtitulo.pack(pady=(0, 10))

#Campo entrada
campo = tk.Entry(frame_principal, width=50, font=("Arial", 11), bg="#ecf0f1", fg="#2c3e50")
campo.pack(pady=10, ipady=6)
campo.focus()

# Frame para botões
frame_botoes = tk.Frame(frame_principal, bg="#2c3e50")
frame_botoes.pack(pady=15, fill=tk.X)

botao_gerar = tk.Button(frame_botoes, 
                        text="🔍 Gerar Receitas",
                        bg="#27ae60",
                        fg="white",
                        width=15,
                        font=("Arial", 10, "bold"),
                        command=gerar_receitas,
                        activebackground="#229954")
botao_gerar.pack(side=tk.LEFT, padx=5)

botao_ingredientes = tk.Button(frame_botoes,
                               text="📋 Ver Ingredientes",
                               bg="#2980b9",
                               fg="white",
                               width=15,
                               font=("Arial", 10, "bold"),
                               command=ver_ingredientes,
                               activebackground="#1f618d")
botao_ingredientes.pack(side=tk.LEFT, padx=5)

botao_limpar = tk.Button(frame_botoes, text="🗑️  Limpar",
                         bg="#e74c3c", fg="white",
                         width=15, 
                         font=("Arial", 10, "bold"),
                         command=limpar_campo,
                         activebackground="#c0392b")
botao_limpar.pack(side=tk.LEFT, padx=5)

# Label para Resultado
label_resultado = tk.Label(frame_principal, text="Resultados:", 
                          font=("Arial", 11, "bold"), bg="#2c3e50", fg="white")
label_resultado.pack(anchor=tk.W, pady=(15, 5))

# Frame para Text com Scrollbar
frame_resultado = tk.Frame(frame_principal, bg="#2c3e50")
frame_resultado.pack(fill=tk.BOTH, expand=True, pady=10)

scrollbar = tk.Scrollbar(frame_resultado, bg="#34495e")
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#Resultado (Text widget com scroll)
resultado = tk.Text(frame_resultado, 
                    height=20, 
                    width=70,
                    font=("Courier", 10),
                    bg="#ecf0f1",
                    fg="#2c3e50",
                    yscrollcommand=scrollbar.set,
                    state=tk.DISABLED,
                    relief=tk.SUNKEN,
                    borderwidth=2)
resultado.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=resultado.yview)

# Footer
footer = tk.Frame(janela, bg="#34495e", height=40)
footer.pack(fill=tk.X, side=tk.BOTTOM, padx=0, pady=0)
footer_text = tk.Label(footer, text="💡 Digite ingredientes e clique em 'Gerar Receitas'", 
                       font=("Arial", 9), bg="#34495e", fg="#bdc3c7")
footer_text.pack(pady=8)

#Rodar
janela.mainloop()


        
    

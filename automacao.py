import customtkinter
import pyautogui as pa

# Configurações gerais do CustomTkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Configuração do PyAutoGUI
pa.PAUSE = 1

def abrir_linkedin():
    pa.press('win')
    pa.write("edge")
    pa.press('ENTER')
    pa.write("linkedin")
    pa.press('ENTER')

def abrir_github():
    pa.press('win')
    pa.write("edge")
    pa.press('ENTER')
    pa.write("github")
    pa.press('ENTER')

def abrir_youtube():
    pa.press('win')
    pa.write("edge")
    pa.press('ENTER')
    pa.write("youtube")
    pa.press('ENTER')

def abrir_postman():
    pa.press('win')
    pa.write("edge")
    pa.press('ENTER')
    pa.write("postman")
    pa.press('ENTER')

def abrir_jwt():
    pa.press('win')
    pa.write("edge")
    pa.press('ENTER')
    pa.write("jwt.io")
    pa.press('ENTER')

def abrir_git_docs():
    pa.press('win')
    pa.write("edge")
    pa.press('ENTER')
    pa.write("git documentation")
    pa.press('ENTER')

# Função para manipular o evento de clique no botão de login
def clique_login():
    if email_entry.get() == "otavio" and senha_entry.get() == "123":
        abrir_tela_principal()
    else:
        erro_label.configure(text="Credenciais inválidas!", text_color="red")

# Função para abrir a nova janela com os botões
def abrir_tela_principal():
    janela.destroy()  # Fecha a janela de login

    # Nova janela principal
    tela_principal = customtkinter.CTk()
    tela_principal.geometry("600x400")
    tela_principal.title("Tela Principal")

    # Criação dos botões com funcionalidade
    botoes = [
        {"texto": "LinkedIn", "comando": abrir_linkedin},
        {"texto": "GitHub", "comando": abrir_github},
        {"texto": "YouTube", "comando": abrir_youtube},
        {"texto": "Postman", "comando": abrir_postman},
        {"texto": "JWT", "comando": abrir_jwt},
        {"texto": "Git Docs", "comando": abrir_git_docs},
    ]

    for botao_info in botoes:
        botao = customtkinter.CTkButton(
            tela_principal, 
            text=botao_info["texto"], 
            command=botao_info["comando"]
        )
        botao.pack(padx=10, pady=10)

    tela_principal.mainloop()

# Configuração inicial da janela de login
janela = customtkinter.CTk()
janela.geometry("500x300")
janela.title("Login")

# Elementos de interface para a janela de login
texto_label = customtkinter.CTkLabel(janela, text="Fazer login", font=("Arial", 18))
email_entry = customtkinter.CTkEntry(janela, placeholder_text="E-mail")
senha_entry = customtkinter.CTkEntry(janela, placeholder_text="Senha", show="*")
login_button = customtkinter.CTkButton(janela, text="Login", command=clique_login)
erro_label = customtkinter.CTkLabel(janela, text="", text_color="red")

# Layout dos elementos na janela
texto_label.pack(pady=12, padx=10)
email_entry.pack(pady=12, padx=10)
senha_entry.pack(pady=12, padx=10)
login_button.pack(pady=12, padx=10)
erro_label.pack(pady=12, padx=10)

janela.mainloop()

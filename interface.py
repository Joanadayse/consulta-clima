import customtkinter  as ctk
from app.clima import buscar_clima

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

janela = ctk.CTk()
janela.geometry("400x400")
janela.title("Consulta de clima")

frame_central= ctk.CTkFrame(janela, fg_color="transparent", width=200)
frame_central.pack(pady=20)

entrada_cidade= ctk.CTkEntry(frame_central,width=150, placeholder_text="Digite a cidade")
entrada_cidade.pack(pady=(20,10))

resultado= ctk.CTkLabel(frame_central, text="", justify="left", font=("Arial", 14))
resultado.pack(pady=10)

def consultar_clima():
    cidade = entrada_cidade.get()
    clima= buscar_clima(cidade)
    
    if clima:
        texto= (
            f"📍 {clima['cidade']}\n"
            f" 🌡 Temperatura: {clima['temperatura']}°C\n"
            f" 🌤 Descrição: {clima["descricao"]} \n"
            f" 💧 Umidade: {clima['umidade']} %\n"
            f" 💨 Vento: {clima['vento']} m/s"

        )
    else:
        texto= "❌ Cidade não encontrada"

    resultado.configure(text=texto)

def nova_consulta():
    entrada_cidade.delete(0,ctk.END)
    resultado.configure(text="")

btn_consultar=ctk.CTkButton(frame_central, text="Consulta Clima", command=consultar_clima)
btn_consultar.pack(pady=5)

btn_limpar = ctk.CTkButton(frame_central, text="Nova Consulta", command=nova_consulta)
btn_limpar.pack(pady=5)

janela.mainloop()




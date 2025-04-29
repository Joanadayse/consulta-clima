def exibir_clima(info_clima):
    print(f"\n Clima em {info_clima['cidade']}:")
    print(f" 🌡️ Temperatura: {info_clima['temperatura']}°C")
    print(f"☁️ Condição: {info_clima['descricao']}")
    print(f"💧 Umidade: {info_clima['umidade']}%")
    print(f"🌬️ Velocidade do vento: {info_clima['vento']}m/s\n")
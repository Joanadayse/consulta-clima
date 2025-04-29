from app.clima import buscar_clima
from app.utils import exibir_clima


def main():
    print("=== Consulta de Clima ===")
    while True:
        cidade= input ("Digite o nome da cidade (ou 'sair para encerrar'): ")
        if cidade.lower() == 'sair':
            print("Encerrando o programa. Até mais!")
            break
        info_clima= buscar_clima(cidade)

        if info_clima :
            exibir_clima(info_clima)
        else:
            print("\n Cidade não encontrada! Verificar o nome e tente novamente.\n")

if __name__== '__main__':
            main()
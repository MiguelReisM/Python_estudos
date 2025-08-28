#Crie um mini sistema que utilize o interactive Help do Python. o Usuario vai digitar o comando e o manual vai aparecer. Quando o usuario digitar a apalvra 'FIM' o programa se encerrará
# OBS use cores
def ajuda():
    while True:
        titulo = "SISTEMA DE AJUDA PyHELP"
        print("\033[1;30;42m" + "=" * (len(titulo) + 4))
        print(f"  {titulo}  ")
        print("=" * (len(titulo) + 4) + "\033[m")

        comando = input("\033[mDigite a função ou biblioteca (FIM para sair): \033[m ").strip()

        if comando.upper() == "FIM":
            msg = "ATÉ LOGO!"
            print("\033[1;37;41m" + "=" * (len(msg) + 4))
            print(f"  {msg}  ")
            print("=" * (len(msg) + 4) + "\033[m")
            break

        subtitulo = f'Acessando o manual do comando "{comando}"...'
        print("\033[0;30;44m" + "=" * (len(subtitulo) + 4))
        print(f"  {subtitulo}  ")
        print("=" * (len(subtitulo) + 4) + "\033[m")

        print("\033[0;97;40m", end="")
        help(comando)
        print("\033[m", end="")


ajuda()

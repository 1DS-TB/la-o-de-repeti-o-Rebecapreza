import random
import os
import time

# MENU PRINCIPAL
while True:
    print(" Duelo ")
    print("1. Iniciar Jogo")
    print("2. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == '2':
        print("Saindo do jogo...")
        break

    elif escolha == '1':
        # SORTEIO DE ATRIBUTOS
        hp = random.randint(1, 100)
        jogador_hp = hp
        jogador_atk = random.randint(1, 50)
        jogador_def = random.randint(1, 20)

        inimigo_hp = hp
        inimigo_atk = random.randint(1, 50)
        inimigo_def = random.randint(1, 20)

        turno = 1

        while jogador_hp > 0 and inimigo_hp > 0:
            print("\n DUELO DE HERÓIS ")
            print("Você            ")
            print(f"HP: {jogador_hp} \n ATQ: {jogador_atk}  DEF: {jogador_def}")
            print("\n Inimigo         ")
            print(f"HP: {inimigo_hp} \n ATQ: {inimigo_atk}  DEF: {inimigo_def}")
            print(f"\n--- Turno {turno} ---")
            print(f"Seu HP: {jogador_hp} | Inimigo HP: {inimigo_hp}")
            print("Sua vez: 1. Atacar | 2. Curar | 3. Cache Hit: ", end='')

            escolha = input()

            if escolha == '1':
                dano = max(0, jogador_atk - inimigo_def)
                inimigo_hp -= dano
                print(f"Você ataca! Inimigo perde {dano} HP.")
            elif escolha == '2':
                cura = random.randint(10, 30)
                jogador_hp += cura
                print(f"Você se cura em {cura} HP!")
            elif escolha == '3':
                if jogador_hp <= 0.25 * hp:
                    cura_cache_hit = int(0.30 * hp)
                    jogador_hp += cura_cache_hit
                    print(f"Você usou o Cache Hit e recuperou {cura_cache_hit} HP!")
                else:
                    print("Seu HP está acima de 25%, não é possível usar o Cache Hit.")
            else:
                print("Escolha inválida! Você perde o turno.")

            if inimigo_hp <= 0:
                print("Você venceu o duelo!")
                break

            acao_inimigo = random.choice(["atacar", "curar"])
            if acao_inimigo == "atacar":
                dano = max(0, inimigo_atk - jogador_def)
                jogador_hp -= dano
                print(f"Inimigo ataca! Você perde {dano} HP.")
            else:
                cura = random.randint(10, 30)
                inimigo_hp += cura
                print(f"Inimigo se cura em {cura} HP!")

            if jogador_hp <= 0:
                print("Você foi derrotado!")
                break

    else:
        print("Opção inválida. Tente novamente.")

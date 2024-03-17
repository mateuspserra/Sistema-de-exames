start = ('Seja bem-vindo à Clínica Saúde Vital')
print(start)
x = ('----------------')
print(x)

while True:
    nome = input('Informe seu nome completo: ')
    idade = int(input('Informe sua idade: '))
    endereco = input('Informe o seu endereço: ')
    telefone = int(input('Informe seu número de telefone: '))
    email = input('Informe seu email: ')
    sexo = input('Informe o seu sexo: ')
    x = ('----------------')
    print(x)

    resposta_correta = 'sim'

    continuar = input('Todas as informações estão corretas? (sim/não): ')
    if continuar.lower() == resposta_correta:
        print("Tudo certo, iremos prosseguir!")
        break
    elif continuar.lower() == 'não':
        print("Por favor, verifique as informações e corrija se necessaário.")
        continue
    else:
        print("Respota inválida. Por favor, responda 'sim' ou 'não'.")

x = ('----------------')
print(x)

xx = ('Por favor, informe qual exame você está interessado em realizar.')
print(xx)

lista_exames = ('\n 1. Anticorpos para hepatite A, B e C R$130,00 \n 2. Checkup completo R$300,00 \n 3. Densitometria óssea R$180,00 \n 4. Eletrocardiograma R$100,00 \n 5. Exame de fezes R$60,00 \n 6. Exame de urina R$50,00 \n 7. Glicemia R$75,00 \n 8. Glicemia e insulina R$90,00 \n 9. Hemograma completo R$80,00 \n 10. Lipidograma R$120,00 \n 11. Mamografia R$150,00 \n 12. Papanicolau R$70,00 \n 13. Parasitológico R$95,00 \n 14. PCR R$110,00 \n 15. PS4 e toque retal R$140,00 \n 16. Ressonância magnética R$600,00 \n 17. Teste ergométrico R$200,00 \n 18. Tomografia computadorizada R$500,00 \n 19. TSH e T4 R$85,00')
print(lista_exames)

x = ('----------------')
print(x)

escolha_de_exames = {'1': 'Anticorpos para hepaite A, B e C', '2': 'Checkup completo', '3': 'Densimotria óssea', '4': 'Eletrocardiograma', '5': 'Exame de fezes', '6': 'Exame de urina', '7': 'Glicemia', '8': 'Glicemia e insulina', '9': 'Hemograma completo', '10': 'Lipidograma', '11': 'Mamografia', '12': 'Papanicolau', '13': 'Parasitológico', '14': 'PCR', '15': 'PS4 e toque retal', '16': 'Ressonância magnética', '17': 'Teste ergonométrico', '18': 'Tomografia computadorizada', '19': 'THS e T4'}
print("Por gentileza, insira um número de 1 a 19: ")

x = ('----------------')
print(x)

def exames():
    print('Agenda de Exames')
    opcoes = []
    agenda = {}
    desconto_aplicado = False
    desconto_analises_clinicas = False
    dias_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira',
                   'Sábado']
    horarios_disponiveis = {
        'Segunda-feira': ['07:00', '07:30', '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30',
                          '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30',
                          '17:00', '17:30', '18:00'],
        'Terça-feira': ['07:00', '07:30', '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30',
                        '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30',
                        '17:00', '17:30', '18:00'],
        'Quarta-feira': ['07:00', '07:30', '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30',
                         '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30',
                         '17:00', '17:30', '18:00'],
        'Quinta-feira': ['07:00', '07:30', '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30',
                         '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30',
                         '17:00', '17:30', '18:00'],
        'Sexta-feira': ['07:00', '07:30', '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30',
                        '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30',
                        '17:00', '17:30', '18:00'],
        'Sábado': ['07:00', '07:30', '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00']
    }

    for dia in dias_semana:
        agenda[dia] = {horario: None for horario in
                       horarios_disponiveis[dia]}

    x = input('Deseja agendar um exame? [S] ou [N]:').lower()
    while x == 's':
        print('Dias da semana disponíveis para agendamento:')
        for dia in dias_semana:
            print(dia)

        dia_escolhido = input('Escolha um dia disponível: ')
        if dia_escolhido in dias_semana:
            print('Horários disponíveis para agendamento:')
            for horario, disponibilidade in agenda[dia_escolhido].items():
                if disponibilidade is None:
                    print(horario)

            horario_escolhido = input('Escolha um horário disponível (formato HH:MM): ')
            if horario_escolhido in agenda[dia_escolhido] and agenda[dia_escolhido][horario_escolhido] is None:

                y = int(input('Por gentileza, insira o tipo de exame: '))
                match y:
                    case 1:
                        print('Anticorpos para hepatite A, B e C')
                        opcoes.append((dia_escolhido, horario_escolhido, y,))
                        agenda[dia_escolhido][horario_escolhido] = y
                    case 2:
                        print('Checkup completo')
                        opcoes.append((dia_escolhido, horario_escolhido, y))
                        agenda[dia_escolhido][horario_escolhido] = y
                    case 3:
                        print('Densitometria óssea')
                        opcoes.append((dia_escolhido, horario_escolhido, y))
                        agenda[dia_escolhido][horario_escolhido] = y
                    case 4:
                        print('Eletrocardiograma')
                        opcoes.append((dia_escolhido, horario_escolhido, y))
                        agenda[dia_escolhido][horario_escolhido] = y
                    case 5:
                        print('Exame de fezes')
                        opcoes.append((dia_escolhido, horario_escolhido, y))
                        agenda[dia_escolhido][horario_escolhido] = y
                    case 6:
                        print('Exame de urina')
                        opcoes.append((dia_escolhido, horario_escolhido, y))
                        agenda[dia_escolhido][horario_escolhido] = y
                    case 7:
                        print('Glicemia')
                        opcoes.append((dia_escolhido, horario_escolhido, y))
                        agenda[dia_escolhido][horario_escolhido] = y
                    case 8:
                        print('Glicemia e insulina')
                        opcoes.append((dia_escolhido, horario_escolhido, y))
                        agenda[dia_escolhido][horario_escolhido] = y
                    case 9:
                        print('Hemograma completo')
                        opcoes.append((dia_escolhido, horario_escolhido, y))
                        agenda[dia_escolhido][horario_escolhido] = y
                    case 10:
                        print('Lipidograma')
                        opcoes.append((dia_escolhido, horario_escolhido, y))
                        agenda[dia_escolhido][horario_escolhido] = y
                    case 11:
                        print('Mamografia')
                        opcoes.append((dia_escolhido, horario_escolhido, y))
                        agenda[dia_escolhido][horario_escolhido] = y
                    case 12:
                        print('Papanicolau')
                        opcoes.append((dia_escolhido, horario_escolhido, y))
                        agenda[dia_escolhido][horario_escolhido] = y
                    case 13:
                        print('Parasitológico')
                        opcoes.append((dia_escolhido, horario_escolhido, y))
                        agenda[dia_escolhido][horario_escolhido] = y
                    case 14:
                        print('PCR')
                        opcoes.append((dia_escolhido, horario_escolhido, y))
                        agenda[dia_escolhido][horario_escolhido] = y
                    case 15:
                        print('PS4 e toque retal')
                        opcoes.append((dia_escolhido, horario_escolhido, y))
                        agenda[dia_escolhido][horario_escolhido] = y
                    case 16:
                        print('Ressonância magnética')
                        opcoes.append((dia_escolhido, horario_escolhido, y))
                        agenda[dia_escolhido][horario_escolhido] = y
                        desconto_analises_clinicas = True
                    case 17:
                        print('Teste ergométrico')
                        opcoes.append((dia_escolhido, horario_escolhido, y))
                        agenda[dia_escolhido][horario_escolhido] = y
                    case 18:
                        print('Tomografia computadorizada')
                        opcoes.append((dia_escolhido, horario_escolhido, y))
                        agenda[dia_escolhido][horario_escolhido] = y
                        desconto_analises_clinicas = True
                    case 19:
                        print('TSH e T4')
                        opcoes.append((dia_escolhido, horario_escolhido, y))
                        agenda[dia_escolhido][horario_escolhido] = y
                    case 20:
                        print('Hemograma completo')
                        dia_hemograma = input('Por favor, escolha o dia para o Hemograma completo: ')
                        horario_hemograma = input('Por favor, escolha o horário para o Hemograma completo (formato HH:MM): ')
                        opcoes.append((dia_hemograma, horario_hemograma, y))
                    case _:
                        print('Exame inválido.')

                if not desconto_aplicado and y in [2]:
                    desconto_aplicado = True

                if not desconto_analises_clinicas and y in [16, 18]:
                    desconto_analises_clinicas = True

            else:
                print('Horário indisponível ou formato inválido. Por favor, escolha outro horário.')
        else:
            print('Dia da semana inválido. Por favor, escolha um dos dias disponíveis.')

        x = input('Deseja agendar mais um exame? [S] ou [N]: ').lower()

        descricao_exame = {
            1: 'Anticorpos para hepatite A, B e C',
            2: 'Checkup completo',
            3: 'Densitometria óssea',
            4: 'Eletrocardiograma',
            5: 'Exame de fezes',
            6: 'Exame de urina',
            7: 'Glicemia',
            8: 'Glicemia e insulina',
            9: 'Hemograma completo',
            10: 'Lipidograma',
            11: 'Mamografia',
            12: 'Papanicolau',
            13: 'Parasitológico',
            14: 'PCR',
            15: 'PS4 e toque retal',
            16: 'Ressonância magnética',
            17: 'Teste ergométrico',
            18: 'Tomografia computadorizada',
            19: 'TSH e T4'
        }

    print("\nAgenda de exames finalizada.")
    print("Os exames agendados foram: ")
    for dia, horarios in agenda.items():
        for horario, codigo_exame in horarios.items():
            if codigo_exame is not None:
                descricao = descricao_exame.get(codigo_exame, 'Exame não encontrado')
                print(f"{dia}, {horario}: {descricao}")

    valor_total = sum([precos[exame[2]] * (0.9 if exame[2] == 2 and desconto_aplicado else 1) * (
        0.8 if exame[2] in [16, 18] and desconto_analises_clinicas else 1) for exame in opcoes])

    if valor_total >= 300 and not any(exame == 20 for _, _, exame in opcoes):
        print("Parabéns! Você ganhou um Hemograma completo.")
        opcoes.append(('Hemograma completo', 20))
        print("Hemograma completo adicionado")

    print('Valor total a pagar: R$', valor_total)


precos = {
    1: 130,  # Anticorpos para hepatite A, B e C
    2: 300,  # Checkup completo
    3: 180,  # Densitometria óssea
    4: 100,  # Eletrocardiograma
    5: 60,  # Exame de fezes
    6: 50,  # Exame de urina
    7: 75,  # Glicemia
    8: 90,  # Glicemia e insulina
    9: 80,  # Hemograma completo
    10: 120,  # Lipidograma
    11: 150,  # Mamografia
    12: 70,  # Papanicolau
    13: 95,  # Parasitológico
    14: 110,  # PCR
    15: 140,  # PS4 e toque retal
    16: 600,  # Ressonância magnética
    17: 200,  # Teste ergométrico
    18: 500,  # Tomografia computadorizada
    19: 85,  # TSH e T4
}

descricao_exame = {
    1: 'Anticorpos para hepatite A, B e C',
    2: 'Checkup completo',
    3: 'Densitometria óssea',
    4: 'Eletrocardiograma',
    5: 'Exame de fezes',
    6: 'Exame de urina',
    7: 'Glicemia',
    8: 'Glicemia e insulina',
    9: 'Hemograma completo',
    10: 'Lipidograma',
    11: 'Mamografia',
    12: 'Papanicolau',
    13: 'Parasitológico',
    14: 'PCR',
    15: 'PS4 e toque retal',
    16: 'Ressonância magnética',
    17: 'Teste ergométrico',
    18: 'Tomografia computadorizada',
    19: 'TSH e T4'
}

codigo_exame = 2

exames()

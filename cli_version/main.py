from crud import *
import time

def main() -> None:

    while True:

        print('\n        ⚙️---DATABASE---⚙️:\n'
              '1. Aggiungi articolo al database\n'
              '2. Elimina articolo da database\n\n'
              '       📦---MAGAZZINO---📦\n'
              '3. Togli quantità\n'
              '4. Aggiungi quantità\n'
              '5. Elimina articoli con giacenza 0\n'
              '6. Aggiungi articolo al magazzino\n'
              '7. Exit\n')
                        

        choice = input('>')

        match(choice):

            case '1':
                try:
                    print('Codice prodotto :')
                    codice = str(input('>')).upper()
                    print('Nome completo prodotto :')
                    nome = str(input('>')).lower()

                    if code_in_database(codice):
                        print(f'{codice} già presente nel database')
                    elif name_in_database(nome):
                        print(f'{nome} già prendente nel database')
                    else:
                        add_item(codice, nome)

                except Exception as e:
                    print(e)

            case '6':

                try:
                    print('Codice prodotto :')
                    codice = str(input('>')).upper()
                    print('Inserisci la quantità :')
                    quantità = int(input('>'))

                    if code_in_database(codice):
                        nome = find_name_by_code(codice)
                        add_to_magazzino(codice, nome, quantità)
                    else:
                        print(f'{codice} non presente nel database ufficiale.')

                except Exception as e:
                    print(e)

            case '3':

                try:
                    print('Codice prodotto :')
                    codice = str(input('>')).upper()

                    if item_in_magazzino(codice):
                        print('Inserisci la quantità da togliere :')
                        quantità = int(input('>'))
                        if single_item(codice).quantity >= quantità:
                            togli_quantità(codice, quantità)
                        else:
                            print(f'Quantità inserita non valida, quantità totale : {single_item(codice).quantity}')
                    else:
                        print(f'{codice} non disponibile in magazzino')

                except Exception as e:
                    print(e)

            case '4':

                try:
                    print('Codice prodotto')
                    codice = str(input('>')).upper()

                    if item_in_magazzino(codice):
                        print('Inserisci la quantità da aggiungere')
                        quantità = int(input('>'))
                        aggiungi_quantità(codice, quantità)
                    else:
                        print(f'{codice} non disponibile in magazzino')

                except Exception as e:
                    print(e)

            case '5':

                try:
                    print('Articoli con giacenza 0 :\n')
                    print(giacenza_zero())
                    print('Sei sicuro di volerli eliminare da Magazzino? y/n')
                    choice2 = str(input('>')).lower()
                    match(choice2):
                        case 'y':
                            delete_zero()
                        case 'n':
                            print('')
                        case _:
                            print('Scelta non valida')

                except Exception as e:
                    print(e)

            case '2':

                try:
                    print('Codice prodotto')
                    codice = str(input('>')).upper()

                    if code_in_database(codice):
                        print(f'Sei sicuro di voler eliminare definitivamente il prodotto con codice : {codice} dal database? y/n')
                        choice = str(input('>'))

                        match(choice):
                            case 'y':
                                delete_item_database(codice)
                            case 'n':
                                print('')
                            case _:
                                print('Scelta non valida')
                    else:
                        print(f'{codice} non trovato nel database')

                except Exception as e:
                    print(e)

            case '7':
                print('Exiting...')
                time.sleep(2)
                break

            case _:
                print('Opzione non valida..')

if __name__ == '__main__':
    main()

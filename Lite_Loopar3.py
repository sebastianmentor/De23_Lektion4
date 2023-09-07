# Stora meny-projektet

BILAR_TILL_SALU = ['bmw','mercedes','kia', 'toyota']

while True:
    print('Sebastians R & S!'.center(24,'-'))
    print('1. Reparera')
    print('2. Köp bil')
    print('3. Sälj bil')
    print('4. Avsluta')
    val = input('Välj menyval: ')
    if val == '1':
        bilmärke = input('Vad för bilmärke önskar du att vi reparera?: ').lower()
        är_stamkund = input('Är du stamkund?(j/n): ').lower()

        if bilmärke == 'volvo':
            print('Absolut, du får en tid nästa vecka!')
        elif bilmärke == 'bmw' and är_stamkund == 'j':
            print('Absolut, du får tid idag!')
        else:
            print('Tyvärr, vi reparerar endast Volvo!!')

    elif val == '2':
        print('Vi har följande bilar till salu!')
        for bil in BILAR_TILL_SALU:
            print(bil, end=' --- ')
        print()
        köp_bil = None
        while köp_bil==None:
            for bil in BILAR_TILL_SALU:
                bil_att_köpa = input(f'Vill du köpa bil {bil}? (y/n)')

                if bil_att_köpa == 'y':
                    köp_bil = bil
                    print(f'Grattis du är nu en stolt ägare till {köp_bil}')
                    break
            if köp_bil != None:
                break
            
            köp = input('Ångra du dig? Vill du inte köpa någon bil? (y/n)')
            if köp == 'n':
                break
            else:     
                pass

    elif val == '3':
        årsmodell = int(input('Skriv in årsmodell: '))
        if årsmodell < 2015:
            print('Tyvärr, vi köper inte in gammalt skrot!')
        else:
            bilmärke = input('Vilket bilmärke är det?: ').lower()
            if bilmärke in BILAR_TILL_SALU:
                print('Absolut, vi köper den till ett bra pris!')
            else:
                print('Tyvärr, inte intresserad!')

    elif val == '4':
        break
    else:
        pass
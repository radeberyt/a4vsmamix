from random import randint
from time import sleep

print("[-] Генерируем силы...")
mHitStrn = randint(3, 40)
mHitCrit = randint(12, 79)
mWSpeed = randint(1, 30)
mHP = 100

aHitStrn = randint(3, 40)
aHitCrit = randint(12, 79)
aWSpeed = randint(1, 30)
aHP = 99

print("[-] Началась битва!")
print(f"[-] Статистика Мамикса:\n - Сила удара: {mHitStrn}\n - Крит. урон: {mHitCrit}\n - Скорость ходьбы: {mWSpeed}\n\n[-] Статистика АНАЛА 4:\n - Сила удара: {aHitStrn}\n - Крит. урон: {aHitCrit}\n - Скорость ходьбы: {aWSpeed}")
print("[-] Подождите...")

while True:
    sleep(1)
    if mHP >= 1 and aHP >= 1:
            if randint(1, 500) >= 250:
                if randint(1, 500) >= 420:
                    print("[-] АНАЛ 4  снес МАМЕГСУ " + str(aHitCrit / 2) + "! Новое хп : " + str(mHP))
                    mHP = mHP - aHitCrit / 2
                else:
                    print("[-] АНАЛ 4  снес МАМЕГСУ " + str(aHitStrn / 2) + "! Новое хп : " + str(mHP))
                    mHP = mHP - aHitStrn / 2

            if randint(1, 500) >= 250:
                if randint(1, 500) >= 420:
                    print("[-] МАМЕГС  снес АНАЛУ 4 " + str(mHitCrit / 2) + "! Новое хп : " + str(aHP))
                    aHP = aHP - mHitCrit / 2
                else:
                    print("[-] МАМЕГС  снес АНАЛУ 4 " + str(mHitStrn / 2) + "! Новое хп : " + str(aHP))
                    aHP = aHP - mHitStrn / 2
    elif mHP >= 1:
        print('[-] Мамикс сдох((')
    else:
        print("[-] АНАЛ4 сдох))")

import struct
import matplotlib.pyplot as plt
import numpy as np



with open('Rat.wdq', 'rb') as f:

    f.seek(2 * ('номер_отведения'-1))


    измерения = struct.unpack('>100h', f.read(200))


    with open('Rat_отведение{номер_отведения}.txt', 'w') as g:

        for измерение in измерения:
            g.write(str(измерение) + '\n')


with open('rat_01_02ml.wdq', 'rb') as f:
    f.seek(5296)


    данные = struct.unpack('>{}h'.format(int(f.getsize()/4 - 5296 / 2)), f.read())


    время = np.arange(0, len(данные)/4) * 0.00195

    канал1 = данные[0::4]
    канал2 = данные[1::4]
    канал3 = данные[2::4]
    канал4 = данные[3::4]


    plt.figure(figsize=(12, 8))
    plt.subplot(4, 1, 1)
    plt.plot(время, канал1, color='red')
    plt.ylabel('Канал 1')
    plt.subplot(4, 1, 2)
    plt.plot(время, канал2, color='green')
    plt.ylabel('Канал 2')
    plt.subplot(4, 1, 3)
    plt.plot(время, канал3, color='blue')
    plt.ylabel('Канал 3')
    plt.subplot(4, 1, 4)
    plt.plot(время, канал4, color='black')
    plt.ylabel('Канал 4')
    plt.xlabel('Время (с)')
    plt.tight_layout()
    plt.show()
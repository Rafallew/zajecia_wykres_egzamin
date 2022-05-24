import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image



def zadanie1():
    print('Zadanie 1')

    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro:")
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'bo')
    plt.ylabel('tutaj y')

    plt.axis([0, 6, 0, 20])

    plt.show()

def zadanie2():
    x = np.arange(0, 5.2, 0.2)
    plt.plot(x, x, 'r-', x, x**2, 'bs', x, x**3, 'g^')

    plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'])

    plt.ylabel('y')
    plt.xlabel('x')

    plt.plot(x, x, 'r--', label='liniowa')
    plt.plot(x, x**2, 'bs', label='kwadratowa')
    plt.plot(x, x**3, 'g^', label='szescienna')

    plt.legend(loc='upper left')
    plt.title('Wykres 3 linii')

    plt.savefig('plot2.png')

    plt.show()

    im = Image.open('plot2.png')
    im = im.convert('RGB')
    im.save('plot2.jpg')

def zadanie3():
    x = np.arange(1, 20)
    y = 1 / x

    plt.plot(x, y, color='green', label='Linia 1')

    plt.text(x=1, y=0.2, s='Tekst')

    plt.ylabel('y cos')
    plt.xlabel('x cos')


    plt.title('Wykres')
    plt.legend()
    plt.show()

def zadanie4():
    x = np.arange(0, 10, 0.1)
    y = np.sin(x)

    plt.plot(x, y, color='green', label='Linia 1')

    plt.show()


def zadanie5():
    plt.subplot(2, 1, 1)
    x1 = np.arange(0, 2.02, 0.2)
    x2 = np.arange(0, 2.02, 0.2)

    y1 = np.sin(2 * np.pi * x1)
    y2 = np.cos(2 * np.pi * x2)

    plt.subplots_adjust(hspace=0.5)

    plt.subplot(2, 1, 1)
    plt.plot(x1, y1)

    plt.title('Tytul')

    plt.subplot(2, 1, 2)
    plt.plot(x2, y2)
    plt.ylabel('cos(x)')
    plt.xlabel('x')

    plt.show()

def zadanie6():
    fig, axs = plt.subplots(3, 2)
    print(type(fig))
    print(type(axs))

    x1 = np.arange(0, 2.02, 0.2)
    x2 = np.arange(0, 2.02, 0.2)

    y1 = np.sin(2 * np.pi * x1)
    y2 = np.cos(2 * np.pi * x2)

    i_x = 0
    i_y = 0
    axs[i_x, i_y].plot(x1, y1)
    axs[i_x, i_y].set_xlabel('x')
    axs[i_x, i_y].set_ylabel('sin(x)')
    axs[i_x, i_y].set_title('wykres sin(x)')

    i_x = 1
    i_y = 1
    axs[i_x, i_y].plot(x2, y2, 'r-')
    axs[i_x, i_y].set_xlabel('x')
    axs[i_x, i_y].set_ylabel('cos(x)')
    axs[i_x, i_y].set_title('wykres sin(x)')

    i_x = 2
    i_y = 0
    axs[i_x, i_y].plot(x2, y2, 'r-')
    axs[i_x, i_y].set_xlabel('x')
    axs[i_x, i_y].set_ylabel('cos(x)')
    axs[i_x, i_y].set_title('wykres sin(x)')

    fig.delaxes(axs[0, 1])
    fig.delaxes(axs[1, 0])
    fig.delaxes(axs[2, 1])

    plt.show()

def zadanie7():
    dane = {
        'a': np.arange(50),
        'c': np.random.randint(0, 51, 50),
        'd': np.random.randn(50)
    }

    dane['b'] = dane['a'] + 10 * np.random.randn(50)
    dane['d'] = np.abs(dane['d']) * 100

    plt.scatter(data=dane, x='a', y='b', c='c', s='d')

    plt.show()

def zadanie8():
    data = {
        'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delphi', 'Brasilia', 'Warszawa'],
        'Populacja': [11190846, 1303171035, 207847528, 38645467],
        'Kontynent': ['Europa', 'Azja', 'Ameryka', 'Europa']
    }

    df = pd.DataFrame(data)

    df_grouped = df.groupby('Kontynent')
    labels = list(df_grouped.groups.keys())
    values = list(df_grouped.agg('Populacja').sum())

    plt.bar(x=labels, height=values, color=['red', 'green', 'blue'])

    plt.xlabel('Kontynenty')
    plt.ylabel('Populacja na kontynentach')

    plt.show()

def zadanie9():
    x = np.random.randn(10000)
    plt.hist(x, bins=50, alpha=0.75, facecolor='g', density=True)

    plt.show()


if __name__ == '__main__':
    #zadanie1()

    #zadanie2()

    #zadanie3()

    #zadanie4()

    #zadanie5()

    #zadanie6()

    # kropki
    #zadanie7()

    # slupkowy
    #zadanie8()

    zadanie9()
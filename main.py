import csv
import re
DEBUG = True


def main():
    print("Start")

    servidores = csv2List('SalariosServidores2020.csv')

    for ser in servidores:
        nome = ser["Nome"]

        if not re.search(r'ZULEIDE', nome):
            continue

        # if "ZULEIDE" not in nome:
        #     continue
        # Nome, Cargo, CargaHoraria, Liquido
        # JOSE - PM (40) R$ 4,000
        res = "{Nome} - {Cargo} [{Mes}] R$ {Liquido}".format(**ser)
        print(res)


def csv2List(file_name):
    count = 0
    result_list = []
    with open(file_name) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')

        is_first = True
        attributes = []
        for row in spamreader:
            count = count + 1

            if is_first:
                attributes = row
                if DEBUG == True:
                    print("=========ATTR==========")
                    for att in attributes:
                        print(att)
                    print("=======================")

            else:
                bean = {}
                for att in attributes:
                    i = attributes.index(att)

                    try:
                        bean[att] = row[i]
                    except:
                        print("DEU RUIM, " + ', '.join(row))

                result_list.append(bean)
            is_first = False
            # if count == 5:
            #     break
    return result_list


if __name__ == "__main__":
    main()

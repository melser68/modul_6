path = r'C:\11.txt'
dict_animals = dict()
list_dict = list()


def get_cats_info(path):
    with open(path) as fh:
        list_animals = fh.readlines()
        count =0
        for i in list_animals:
            if '\n' in i:
                list_animals[count] = i[:-1]
                count +=1
        else:
            count +=1
        for y in list_animals:
            temp = y.split(',')
            dict_animals['id'] = temp[0]
            dict_animals['name'] = temp[1]
            dict_animals['age'] = temp[2]
            list_dict.append(dict_animals)

    print(dict_animals)
get_cats_info(path)
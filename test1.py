
def main(sen, elist):
    adict = {}
    for i in range(len(elist)):
        adict[elist[i]] = str(i)
    cha = [',', '.']
    result_list = []
    flag = 1        # flag=1代表在双引号外面，-1代表在里面
    for i in range(len(sen)):
        if sen[i] == '':
            result_list.append(' ')
            continue
        if sen[i] == '"':
            flag = -flag
            result_list.append('"')
            continue
        if flag == -1:
            result_list.append(sen[i])
            continue
        if sen[i][-1] in cha:
            if sen[i][:-1].lower() in adict:
                result_list.append(adict[sen[i][:-1].lower()] + sen[i][0])
            else:
                result_list.append(sen[i])
        else:
            if sen[i].lower() in adict:
                result_list.append(adict[sen[i].lower()])
            else:
                result_list.append(sen[i])

    result_str = ''
    for i in range(len(result_list)):
        result_str += result_list[i] + ' '
    return result_str[:-1]


if __name__ == '__main__':
    Ewords = 'An introduction is " the first paragraph " of your paper.'
    Elist = 'what say first Second IS introduction IS end'
    # Ewords = input().strip()
    # Elist = input().strip()
    # Ewords = Ewords.lower()
    Ewords = Ewords.split(' ')
    Elist = Elist.lower()
    Elist = Elist.split(' ')
    result = main(Ewords, Elist)
    print(result)
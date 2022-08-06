import time
import re
def precleaning(code):
    return [i.split(' ')[::-1] for i in code.split('\n')]
def machine(code):
    global forcode
    global memory
    forcode=code
    global line
    global data
    memory={}
    functions={'복':input_,'편':print_,'살':get_,'복세':ifstart,'편살':ifend,'복세편살':goto,'복잡한세상편하살자':sleep,'퇴사':end,'편하':print_a}
    line=0
    p=re.compile('세+')
    n=re.compile('([!]+)([?]*)|([!]*)([?]+)')
    data=0
    while line<len(code):
        text=0
        while text<len(code[line]):
            j=code[line][text]
            if p.match(j):
                #memory[len(j)]=data
                if len(j) in memory.keys():
                    memory[len(j)]+=data
                else:
                    memory[len(j)]=data
            elif n.match(j):
                k=n.match(j).groups()
                data=len(k[0])-len(k[1])
            elif j in functions.keys():
                functions[j]()
            else:
                print("Error!")
                end()
            text+=1
        line+=1
def input_():
    global data
    data=int(input())
def print_():
    global data
    print(data,end='')
def get_():
    global data
    global memory
    if data in memory.keys():
        data=memory[data]
    else:
        data=0
def goto():
    global line
    global data
    line=data-1
    data=0
def sleep():
    global data
    time.sleep(data)
def end():
    global data
    return data
def print_a():
    global data
    print(chr(data),end='')
def ifstart():
    global data
    global line
    global forcode
    code=forcode
    st=line
    fs=1
    fe=0
    line+=1
    while (line<len(code) and fs!=fe):
        if '복세' in code[line]:
            fs+=1
        elif '편살' in code[line]:
            fe+=1
        line+=1
    if_end_line=line
    line=st
    if data!=0:
        line=if_end_line-1
        text=0-1
    else:
        pass
def ifend():
    pass
if __name__ == '__main__':
    while True:
        filelink=input('file location:')
        with open(filelink, 'r',encoding='utf-8') as file_data:
            file=file_data.read()
        machine(precleaning(file))
        print()

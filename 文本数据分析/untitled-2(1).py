import uuid
def range1(num):
    id_list= []
    for i in range(num):
        id=str(uuid.uuid4()).replace('-','').upper()
        #id.replace('-', '')
        while id in id_list:
                id=str(uuid.uuid4()).replace('-','').upper()
        print(id)
        id_list.append(id)

if __name__ == '__main__':
    range1(100)
    
        


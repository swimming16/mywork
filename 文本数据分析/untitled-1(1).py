import uuid
from itertools import dropwhile

def generateActivationCode(num):
    codeList = []
    for i in range(num):
        code = str(uuid.uuid4()).replace('-','').upper()
        while code in codeList:
            code = str(uuid.uuid4()).replace('-','').upper()
        codeList.append(code)

    for code in codeList:
        print(code)

if __name__ == '__main__':
    generateActivationCode(200)
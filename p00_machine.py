import re
program = input("p0;0 Cipher Machine\nEncipher: 1, Decipher: 2\n")
if program == "1":
    encipher = input("Enter text to encipher\n")
    sub_dict = {
    #uppercase
        'A':'PQ','B':'PW','C':'PE',
        'D':'PR','E':'PT','F':'PY',
        'G':'PU','H':'PI','I':'PO',
        'J':'QP','K':'QQ','L':'QW',
        'M':'QE','N':'QR','O':'QT',
        'P':'QY','Q':'QU','R':'QI',
        'S':'QO','T':'WP','U':'WQ',
        'V':'WW','W':'WE','X':'WR',
        'Y':'WT','Z':'WY',
    #lowercase
        'a':';A','b':';S','c':';D',
        'd':';F','e':';G','f':';H',
        'g':';J','h':';K','i':';L',
        'j':'A;','k':'AA','l':'AS',
        'm':'AD','n':'AF','o':'AG',
        'p':'AH','q':'AJ','r':'AK',
        's':'AL','t':'S;','u':'SA',
        'v':'SS','w':'SD','x':'SF',
        'y':'SG','z':'SH',
    #special characters
        ' ':';;','!':'/Z','.':'/>',
        ',':'/<',
#problems with ? and $ enciphering
        '\?':'//',
        '\$':'/C'
        }
    regex = '|'.join(sub_dict)
    print(re.sub(regex, lambda m: sub_dict[m.group()], encipher))
    input("Press any key to continue")

elif program == "2":
    decipher = input("Enter text to decipher\n")
    sub_dict = {
    #uppercase
        'PQ':'A','PW':'B','PE':'C',
        'PR':'D','PT':'E','PY':'F',
        'PU':'G','PI':'H','PO':'I',
        'QP':'J','QQ':'K','QW':'L',
        'QE':'M','QR':'N','QT':'O',
        'QY':'P','QU':'Q','QI':'R',
        'QO':'S','WP':'T','WQ':'U',
        'WW':'V','WE':'W','WR':'X',
        'WT':'Y','WY':'Z',
    #lowercase
        ';A':'a',';S':'b',';D':'c',
        ';F':'d',';G':'e',';H':'f',
        ';J':'g',';K':'h',';L':'i',
        'A;':'j','AA':'k','AS':'l',
        'AD':'m','AF':'n','AG':'o',
        'AH':'p','AJ':'q','AK':'r',
        'AL':'s','S;':'t','SA':'u',
        'SS':'v','SD':'w','SF':'x',
        'SG':'y','SH':'z',
    #special characters
        ';;':' ','/Z':'!','/>':'.',
        '/<':',',
        '//':'?',
        '/C':'$'
        }
    regex = '|'.join(sub_dict)
    print(re.sub(regex, lambda m: sub_dict[m.group()], decipher))
    input("Press any key to continue")
else: 
    print("You broke it.\n")
    input("Press any key to continue")

#written by derpywashere on 2019/09/30
#"fuck"


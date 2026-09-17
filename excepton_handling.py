'''
try:
    3code that causes error
except:
    3code that handles error
'''
'''
#a,b=map(int,input("Enter values").split())
try:
    a,b=map(int,input("Enter values: ").split(","))
    result=a/b
    print(result)
except ValueError:
    print("chusi ivvu ra ❤️ day ke pal only integers")
except ZeroDivisionError:
    print("Zero tho divide ela chestha ra denominator lo zero kanna ekkuva ivvu")
except AttributeError:
    print("attributes chudu....chusi sarriga ivvu")
except NameError:
    print("nuvu python nerchukuni bokka ra syntax nerchuko")
finally:
    print("Inka em vundhi le paduko 🛌")
'''
try:
    a=[12,3,4]
    print(a[5])
    a.append("COdegnan")
    print(a)
except(IndexError,NameError,AttributeError) as e:
    if e==IndexError:
        print("Idhi index error")
    elif e==NameError:
        print("Idhi name error")
    elif e==AttributeError:
        print("Idhi Attribute error")
finally:
    print("Odhu ra po ra rey !!!!!")
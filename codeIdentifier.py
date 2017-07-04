pyKeyWords1=['def','elif','del','global','lambda','nonlocal','raise','import','assert','class','continue']

pyKeyWords2=['False','None','True','else','except','finally','for','pass','return','try','while','yield','with','and','as','from','if','or','in','is','not','break']

javaKeyWords1=['abstract', 'assert', 'boolean','byte', 'char', 'class', 'const',  'default',  'double',  'enum', 'extends','float','import', 'instanceof', 'int', 'interface', 'long', 'package', 'private', 'protected', 'public', 'short', 'static', 'strictfp', 'super', 'switch','synchronized', 'throw', 'throws', 'transient','void']

javaKeyWords2=['while','volatile','try','break','case', 'catch','continue','this','do','else','finally','final','for','goto', 'if','implements','native','new','return']

cppKeyWords1=['alignas', 'alignof', 'and_eq', 'asm', 'atomic_cancel', 'atomic_commit', 'atomic_noexcept','auto', 'bitand', 'bitor', 'bool', 'char', 'char16_t', 'char32_t', 'class', 'compl', 'const', 'constexpr', 'const_cast','continue', 'decltype', 'default',  'double','dynamic_cast', 'enum', 'export', 'extern', 'float',  'goto', 'import', 'inline', 'int', 'long', 'module ', 'mutable', 'namespace',  'noexcept','not_eq', 'nullptr','operator', 'or_eq', 'private', 'protected', 'public',  'reinterpret_cast',  'signed', 'sizeof', 'static', 'static_assert', 'static_cast', 'struct', 'switch','synchronized','template', 'thread_local', 'throw', 'true',  'typedef', 'typeid', 'typename', 'unsigned', 'virtual', 'void', 'volatile', 'wchar_t', 'xor', 'xor_eq']

cppKeyWords2=['and','break', 'case', 'catch', 'concept','delete', 'do', 'else','explicit',  'false','for',
'friend','if','new','not', 'or','return','short', 'register','requires','this','try', 'union','using', 'while']

pyOperators=['+','-','*','/','%','>','<','!=','&','|','^','>','<','=','~']

def count_substring(string, sub_string):
    length = len(string)
    counter = 0
    for i in range(length):
        for j in range(length):
            if string[i:j+1] == sub_string:
                counter +=1
    return counter

def isCodeSnippet(code):
    if(count_substring(code,"```")>=2):
        return True
    return False

def pyCnt(code):
    lst=code.split("\n")
    newlst=list()
    for item in lst:
        newlst.append(item.strip(" "))
    code="".join(newlst)
    ck1=0;ck2=0;op=0;openCnt=0;closeCnt=0;    
    for word in pyKeyWords1:
        ck1+=len(word)*count_substring(code,word)
    for word in pyKeyWords2:
        ck2+=len(word)*count_substring(code,word)
    for operator in pyOperators:
        op+=len(operator)*count_substring(code,operator)
    openCnt+=count_substring(code,"(")
    openCnt+count_substring(code,"{")
    openCnt+=count_substring(code,"[")
    closeCnt+=count_substring(code,")")
    closeCnt+=count_substring(code,"}")
    closeCnt+=count_substring(code,"]")
    sum=ck1+ck2+op+openCnt+closeCnt 
    r1=float(ck2)/len(code)
    r2=float(sum)/len(code)
    if r2>=0.1 and (r1/r2)<=0.8:
        return (True,r2)
    return (False,r2)

def javaCnt(code):
    lst=code.split("\n")
    newlst=list()
    for item in lst:
        newlst.append(item.strip(" "))
    code="".join(newlst)
    #print code
    ck1=0;ck2=0;op=0;openCnt=0;closeCnt=0;semicolon=0;    
    for word in javaKeyWords1:
        ck1+=len(word)*count_substring(code,word)
    for word in javaKeyWords2:
        ck2+=len(word)*count_substring(code,word)
    for operator in pyOperators:
        op+=len(operator)*count_substring(code,operator)
    openCnt+=count_substring(code,"(")
    openCnt+count_substring(code,"{")
    openCnt+=count_substring(code,"[")
    closeCnt+=count_substring(code,")")
    closeCnt+=count_substring(code,"}")
    closeCnt+=count_substring(code,"]")
    semicolon+=count_substring(code,";")
    sum=ck1+ck2+op+openCnt+closeCnt 
    r1=float(ck2)/len(code)
    r2=float(sum)/len(code)
    if semicolon>=2:
        return (True,0.9)
    if r2>=0.1 and (r1/r2)<=0.8:
        return (True,r2)
    return (False,r2)

def cppCnt(code):
    lst=code.split("\n")
    newlst=list()
    for item in lst:
        newlst.append(item.strip(" "))
    code="".join(newlst)
    ck1=0;ck2=0;op=0;openCnt=0;closeCnt=0;semicolon=0;     
    for word in cppKeyWords1:
        ck1+=len(word)*count_substring(code,word)
    for word in cppKeyWords2:
        ck2+=len(word)*count_substring(code,word)
    for operator in pyOperators:
        op+=len(operator)*count_substring(code,operator)
    openCnt+=count_substring(code,"(")
    openCnt+count_substring(code,"{")
    openCnt+=count_substring(code,"[")
    closeCnt+=count_substring(code,")")
    closeCnt+=count_substring(code,"}")
    closeCnt+=count_substring(code,"]")
    semicolon+=count_substring(code,";")
    sum=ck1+ck2+op+openCnt+closeCnt 
    r1=float(ck2)/len(code)
    r2=float(sum)/len(code)
    if semicolon>=2 or count_substring(code,"#include")>=1:
        return (True,0.9)
    if r2>=0.1 and (r1/r2)<=0.8:
        return (True,r2)
    return (False,r2)

infile=open("testing","rt")
code=infile.read()

if isCodeSnippet(code):
    print "It is a code snippet"
else:
    print "Python ", pyCnt(code)
    print "Cpp ", cppCnt(code)
    print "Java ",javaCnt(code)

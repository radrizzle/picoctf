from decimal import *
from sympy import *

e = 123334412422100200073724293397814444133055948432660394894575537196644655590911975216597225369533291665546450682873771461121931297334750574833076266929264725659227058033916622749912643253158471374706962420216987517740513085132327782751601333433891622511268018937213463428433812468005029253256928427054941722303
n = 146253632466659229545931832210606781017673754148548846652967890991264894353639817676327761676711108700602299133509688168737217069870676207995858374566281857316385231788968783545970398612749691913676396172349079356653542275338870183774730138136767213981730743176884268539210105387912977774230304388981927307817
c = 92682324890931156197303551960743503242154735972064114394871712623256301206325652271572640107788592564810538673114157805600273936023815797277019134552025986695641500618554506414962763364268383596303864030056557563135149051265709853475362943791480870951103829279250612347684157924087126107740144001038159029398


#Continued fraction expansion for rationals
def cf_expansion(n, d):
    e = []

    q = n // d
    r = n % d
    e.append(q)

    while r != 0:
        n, d = d, r
        q = n // d
        r = n % d
        e.append(q)

    return e

#Get convergents for all continued fraction expansions of original
def find_convergents(e):
    n = [] # Nominators
    d = [] # Denominators
    for i in range(len(e)):
        if i == 0:
            ni = e[i]
            di = 1
        elif i == 1:
            ni = e[i]*e[i-1] + 1
            di = e[i]
        else: # i > 1
            ni = e[i]*n[i-1] + n[i-2]
            di = e[i]*d[i-1] + d[i-2]
        n.append(ni)
        d.append(di)
    return n, d


def main():
    continued_fraction_expansion = cf_expansion(e, n)
    convergents = find_convergents(continued_fraction_expansion)

    k = convergents[0]
    d = convergents[1]

    #Iterating through convergents looking for correct pair of ki and di for phi(N)
    for i in range(0, len(k) - 1):
        if k[i] == 0:
            continue;

        phi_i = (e*d[i] - 1)//k[i]

        p = Symbol('p', integer=True)
        roots = solve(p**2 + (phi_i - n - 1)*p + n, p)
        if len(roots) == 2:
            p, q = roots
            if p*q == n:
                print("Factored N!")
                m = pow(c, d[i], n)
                print("Decrypted flag: " + str(hex(m)))
                return 0
    print("Could not factor N :(")
    return 0



main()
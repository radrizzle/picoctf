from Crypto.Util.number import inverse, long_to_bytes

n = 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
e = 65537
p = 2434792384523484381583634042478415057961
q = 650809615742055581459820253356987396346063

c = 964354128913912393938480857590969826308054462950561875638492039363373779803642185

phi = n - (p + q - 1)

def egcd(a, b):
	if a == 0:
		return (b,0,1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x-(b//a)*y, y)

def modinv(a, m):
	g, x, y = egcd(a, m)
	if g != 1:
		raise Exception('Modular inverse does not exist')
	else:
		return x % m

d = modinv(e, phi)

m = pow(c, d, n)
print(long_to_bytes(m))
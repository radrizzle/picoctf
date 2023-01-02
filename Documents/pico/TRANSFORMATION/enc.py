# 灩捯 == pico

flag = 'pico'

# encoder = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
print("################## ENCODING STEP #############################")
for i in range(0, len(flag), 2):
	print("Original: " + str(ord(flag[i])) + '\t' + str(ord(flag[i+1])))
	print("Step 1: " + flag[i] + '\t' + flag[i+1])
	print("Step 2: " + str((ord(flag[i]) << 8)) + '\t' + str(ord(flag[i+1])))

	char = chr((ord(flag[i]) << 8) + ord(flag[i+1]))
	print(char)








print("################### REVERSE ENGINEERING STEP ################################")
flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽'
decoded = ''
for i in range(0, len(flag)):
	print("Original: " + flag[i] + '\t' + str(ord(flag[i])))
	char1 = ord(flag[i]) >> 8
	char2 = ord(flag[i]) - (ord(chr(char1)) << 8)
	decoded += (chr(char1) + chr(char2))
print(decoded)
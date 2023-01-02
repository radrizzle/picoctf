# %p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p

flag = 'ocip{FTC0l_I4_t5m_ll0m_y_y3n2fc10a10ÿË.}'
new = ''

for i in range(0, len(flag), 4):
	new += flag[i+3]
	new += flag[i+2]
	new += flag[i+1]
	new += flag[i]

print(new)
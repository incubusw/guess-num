import random
num = random.randint(1, 100)

while True:
	ans = input('Please guess a number: ')
	ans = int(ans)
	if ans == num:
		print('Finally get the right answer!!')
		break
	elif ans > num:
		print('Too big, lower your answer...')
	elif ans < num:
		print('Too small, increase the number..')



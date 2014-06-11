
import random, time, sys
 
# Unicode: 9601, 9602, 9603, 9604, 9605, 9606, 9607, 9608
def spark(input, stats=False):

	bar=map(unichr, range(9601,9608))

	barcount = len(bar) - 1
	# numbers = [float(n) for n in re.split(r'[\s,]+', line.strip())]
	numbers=map(float, input)
	mn, mx = min(numbers), max(numbers)
	extent = mx - mn
	sparkline = ''.join(bar[int( (n - mn) / extent * barcount)]
	                    for n in numbers)
	if stats: print('min: %5f; max: %5f' % (mn, mx))
	return sparkline

a=range(1,50)
while True:
	a.pop(0)
	a.append(random.randint(1,8))
	print '\r',spark(a),
	time.sleep(0.25)
	sys.stdout.flush()
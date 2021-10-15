from random import randint
def random_quick_sort(A):
	if len(A) <= 1: return A
	X = randint(0, len(A)-1)
	L, R, M = [], [], []
	for a in A:
		if a == A[X]: M.append(a)
		elif a < A[X]: L.append(a)
		else: R.append(a)
	L = random_quick_sort(L)
	R = random_quick_sort(R)
	return L + M + R 
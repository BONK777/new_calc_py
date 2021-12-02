from calculator import Calculator

cal = Calculator()

def test_multiply_POS():
	x = 3
	y = 3
	res = 9
	assert cal.multiply(x, y) == res, f"Проверка умножения не пройдена {x} * {y} не равно {res}"

def test_multiply_NEG():
	cal = Calculator()
	assert cal.multiply(3, 3) != 8

def test_share_POS():
	x = 3
	y = 3
	res = 1
	assert cal.share(x, y) == res, f"Проверка деления не пройдена {x} / {y} не равно {res}"

def test_share_NEG():
	cal = Calculator()
	assert cal.share(3, 3) != 0

def test_plus_POS():
	x = 3
	y = 3
	res = 6
	assert cal.plus(x, y) == res, f"Проверка сложения не пройдена {x} / {y} не равно {res}"

def test_plus_NEG():
	cal = Calculator()
	assert cal.plus(3, 3) != 0

def test_minus_POS():
	x = 3
	y = 3
	res = 0
	assert cal.minus(x, y) == res, f"Проверка вычитания не пройдена {x} / {y} не равно {res}"

def test_minus_NEG():
	cal = Calculator()
	assert cal.minus(3, 3) != 1
import calc


while True:
    abc = input('выберите операцию +,-,/,*,^,random,mod,!,arccos:')

    if abc in ("mod", "!", "arccos"):

        calc.Calculator.improved(abc)
    elif abc == "random":

        calc.Calculator.random()
    elif abc in ('+', '-', '*', '^', '/'):

        calc.Calculator.ordinary(abc)
    break

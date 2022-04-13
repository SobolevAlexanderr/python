
import calc


while True:
    abc = input('выберите операцию +,-,/,*,^,random,mod,!,arccos:')

    if abc in ("mod", "!", "arccos"):
        operation = calc
        operation.Calculator.improved(abc)
    elif abc == "random":
        operation = calc
        operation.Calculator.random()
    elif abc in ('+', '-', '*', '^', '/'):
        operation = calc
        operation.Calculator.ordinary(abc)
    break


def fibbonaci(before, beforeBefore, iteration):
    new = before + beforeBefore
    iteration += 1
    print(iteration, new)
    fibbonaci(new, before, iteration)

fibbonaci(1, 1, 0)


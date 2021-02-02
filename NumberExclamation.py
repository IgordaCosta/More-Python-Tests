


def NumberExclamation(ExclaNum):
    ExpNumberMult=1
    for i in range(ExclaNum):
        num = i+1
        # print(str(num))
        ExpNumberMult = ExpNumberMult * num

    # print('ExpNumberMult: ', str(ExpNumberMult))
    return ExpNumberMult



ExclaNum1 = 16

ExclaNum2 = 15
ExpNumberMult1 = NumberExclamation(ExclaNum1)


ExpNumberMult2 = NumberExclamation(ExclaNum2)

print(ExpNumberMult1/ExpNumberMult2)
    
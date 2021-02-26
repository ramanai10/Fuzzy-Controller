import json

class Temperature:
    VERY_COOL = "very-cool"
    COOL = "cool"
    VERY_MODERATE = "very-moderate"
    MODERATE = "moderate"
    MODERATELY_HOT = "moderate-hot"
    HOT = "hot"
    VERY_HOT = "very-hot"

class Mode:
    MICRO = "micro"
    GRILL = "grill"
    CONVECTION = "convection"

def fuzzifier_temp(t):
    if t >=107 and t <= 121:
        return Temperature.VERY_COOL
    elif t >= 135 and t <= 149:
        return Temperature.COOL
    elif t == 163:
        return Temperature.VERY_MODERATE
    elif t >= 177 and t <= 191:
        return Temperature.MODERATE
    elif t == 205:
        return Temperature.MODERATELY_HOT
    elif t >= 218 and t <= 233:
        return Temperature.HOT
    else:
        return Temperature.VERY_HOT

def fuzzifier_mode(m):
    if m == 1:
        return Mode.MICRO
    elif m == 2:
        return Mode.GRILL
    else:
        return Mode.CONVECTION

def defuzzify_op(f):
    if f == Temperature.VERY_COOL:
        return 20
    elif f == Temperature.COOL:
        return 50
    elif f == Temperature.VERY_MODERATE:
        return 80
    elif f == Temperature.MODERATE:
        return 110
    elif f == Temperature.MODERATELY_HOT:
        return 140
    elif f == Temperature.HOT:
        return 170
    else:
        return 200

def compute(a, b):
    flag = True
    if a < 107 or a > 246:
        flag = False
        
    if b < 1 or b > 3:
        flag = False
    if flag == True:
        a_fuzzy = fuzzifier_temp(a)
        b_fuzzy = fuzzifier_mode(b)
    else:
        a_fuzzy = None
        b_fuzzy = None
    print(a_fuzzy,b_fuzzy)
    rule_base = dict()
    rule_base = {(Temperature.COOL,Mode.MICRO): Temperature.COOL,
                 (Temperature.HOT,Mode.MICRO): Temperature.HOT,
                 (Temperature.MODERATE,Mode.MICRO): Temperature.MODERATE,
                 (Temperature.VERY_MODERATE,Mode.GRILL): Temperature.VERY_MODERATE,
                 (Temperature.MODERATELY_HOT,Mode.GRILL): Temperature.MODERATELY_HOT,
                 (Temperature.MODERATE,Mode.GRILL): Temperature.MODERATE,
                 (Temperature.HOT,Mode.GRILL): Temperature.HOT,
                 (Temperature.VERY_COOL,Mode.CONVECTION): Temperature.VERY_COOL,
                 (Temperature.COOL,Mode.CONVECTION): Temperature.COOL,
                 (Temperature.MODERATE,Mode.CONVECTION): Temperature.MODERATE,
                 (Temperature.VERY_MODERATE,Mode.CONVECTION): Temperature.VERY_MODERATE}
    ip_params = (a_fuzzy,b_fuzzy)
    fuzzy_op = rule_base.get(ip_params, None)
    if fuzzy_op is None:
        flag = False
        return 0
    else:
        return fuzzy_op
        
i = int(0)

for i in range(4):
    temp = int(input("Enter the temperature for the oven(107 - 246 degree celcius): "))
    m = int(input("Enter the mode(1-3) for the oven: "))
    res = compute(temp, m)
    print(res)
    if res != 0:
        d = defuzzify_op(res)
    else:
        d = 0
    print("Final output:{}, {}, {}".format(temp,m,d))


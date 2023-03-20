from django.shortcuts import render
import random
import string
# Create your views here.


def password(request):
    # alf = 'zxcvbnmasdfghjklqwertyuiop'
    # num = '1234567890'
    # cim = '!@#$^%&*'
    # nc = '1234567890!@#$^%&*'
    # na = 'zxcvbnmasdfghjklqwertyuiop1234567890'
    # ac = 'zxcvbnmasdfghjklqwertyuiop!@#$^%&*'
    can = 'zxcvbnmasdfghjklqwertyuiop1234567890!@#$^%&*'
    a= list()
    x =int(random.randint(8,13))
    for i in range(x):
        a +=random.choice(can)
        # print(a)
    a = ''.join(a)
    context = {'a':a}
    return render(request, 'index.html', context)

# password('1')

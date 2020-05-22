import subprocess
import random
import time
import logging
import os
import argparse
import sys
from progress.bar import Bar
parser = argparse.ArgumentParser()
parser.add_argument('-p',help="Path to your implentation file")
parser.add_argument('-n',default=100,help="Number of tests (3 times more will be performed)")
args = parser.parse_args(sys.argv[1:])
dir_path = os.path.dirname(os.path.realpath(__file__))

os.makedirs(os.path.join(dir_path,'log'),exist_ok=True)
logger = logging.getLogger("test")
logging.basicConfig(level=logging.INFO, filename=os.path.join(dir_path,'log',str(time.time())), filemode='w')

dir_path = os.path.dirname(os.path.realpath(__file__))

def compile(path):
    cmd = f"gcc -g -I{dir_path} {dir_path}/test.c {path} -o {dir_path}/impl"
    c =subprocess.Popen(cmd,shell=True)
    c.communicate()

def load_proc():
    global p
    p= subprocess.Popen(
            f"{dir_path}/impl", 
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1)

compile(args.p)
load_proc()

N = int(args.n)
M=int(str(1)+"0"*500)
      
class AddTest:
    def __init__(self,bound_l=0,bound_r=M):
        self.bound_l = bound_l
        self.bound_r = bound_r
        self.name="add"

    def run(self):
        d1 = random.randint(self.bound_l,self.bound_r)
        d2 = random.randint(self.bound_l,self.bound_r)
        return[
        self.res(d1,d2),
        self.res(d1,0),
        self.res(0,d1),
        ]
    def res(self, d1, d2):
        ans = str(d1+d2)
        try:
            p.stdin.write("1\n")
            p.stdin.write(str(d1)+'\n')
            p.stdin.write(str(d2)+'\n')
            ret = p.stdout.readline()
            if ret[:-1]==ans:
                return True
            else:
                logger.error(f'{self.name}: {d1} {d2} Expected: {ans}, Recieved: {ret[:-1]}')
                return False
        except BrokenPipeError:
            logger.error(f'{self.name}: {d1} {d2} Seg Fault')
            load_proc()
            return False

        except Exception as e:
            logger.error(f'{self.name}: {d1} {d2} {e}')
            load_proc()
            return False
        
class DiffTest:
    def __init__(self,bound_l=0,bound_r=M):
        self.bound_l = bound_l
        self.bound_r = bound_r
        self.name="diff"

    def run(self):
        d1 = random.randint(self.bound_l,self.bound_r)
        d2 = random.randint(self.bound_l,self.bound_r)
        return  [
        self.res(d1,d2),
        self.res(d1,0),
        self.res(0,d1)]

    def res(self, d1, d2):
        ans = str(abs(d1-d2))
        try:
            p.stdin.write("2\n")
            p.stdin.write(str(d1)+'\n')
            p.stdin.write(str(d2)+'\n')
            ret = p.stdout.readline()
            if ret[:-1]==ans:
                return True
            else:
                logger.errorbug(f'{self.name}: {d1} {d2} Expected: {ans}, Recieved: {ret[:-1]}')
                return False
        except BrokenPipeError:
            logger.error(f'{self.name}: {d1} {d2} Seg Fault')
            load_proc()
            return False
        except Exception as e:
            logger.error(f'{self.name}: {d1} {d2} {e}')
            load_proc()
            return False

class CmpTest:
    def __init__(self,bound_l=0,bound_r=M):
        self.bound_l = bound_l
        self.bound_r = bound_r
        self.name="cmp"
    def run(self):
        d1 = random.randint(self.bound_l,self.bound_r)
        d2 = random.randint(self.bound_l,self.bound_r)
        return [self.res(d1,d2),
        self.res(d1,0),
        self.res(0,d1),
        self.res(d1,d1)]

    def res(self, d1, d2):
        ans =str(0 if d1==d2 else 1 if d1>d2 else -1)
        try:
            p.stdin.write("3\n")
            p.stdin.write(str(d1)+'\n'+str(d2)+'\n')
            ret = p.stdout.readline()
            if ret[:-1]==ans:
                return True
            else:
                logger.error(f'{self.name}: {d1} {d2} Expected: {ans}, Recieved: {ret[:-1]}')
                return False
        except BrokenPipeError:
            logger.error(f'{self.name}: {d1} {d2} Seg Fault')
            load_proc()
            return False

        except Exception as e:
            logger.error(f'{self.name}: {d1} {d2} {e}')
            load_proc()
            return False

class MulTest:
    def __init__(self,bound_l=0,bound_r=M):
        self.bound_l = bound_l
        self.bound_r = bound_r
        self.name="mul"

    def run(self):
        d1 = random.randint(self.bound_l,self.bound_r)
        d2 = random.randint(self.bound_l,self.bound_r)
        return [self.res(d1,d2),
        self.res(d1,0),
        self.res(0,d1)]

    def res(self, d1, d2):
        ans =str(d1*d2)
        try:
            p.stdin.write("4\n")
            p.stdin.write(str(d1)+'\n'+str(d2)+'\n')
            ret = p.stdout.readline()
            if ret[:-1]==ans:
                return True
            else:
                logger.error(f'{self.name}: {d1} {d2} Expected: {ans}, Recieved: {ret[:-1]}')
                return False
        except BrokenPipeError:
            logger.error(f'{self.name}: {d1} {d2} Seg Fault')
            load_proc()
            return False
        
        except Exception as e:
            logger.error(f'{self.name}: {d1} {d2} {e}')
            load_proc()
            return False

class ModTest:
    def __init__(self,bound_l=1,bound_r=M):
        self.bound_l = bound_l
        self.bound_r = bound_r
        self.name="mod"

    def run(self):
        d1 = random.randint(self.bound_l,self.bound_r)
        d2 = random.randint(self.bound_l,self.bound_r)
        return [self.res(d1,d2),
        self.res(d1,d1),
        self.res(0,d1)]

    def res(self, d1, d2):
        ans =str(d1%d2)
        try:
            p.stdin.write("5\n")
            p.stdin.write(str(d1)+'\n'+str(d2)+'\n')
            ret = p.stdout.readline()
            if ret[:-1]==ans:
                return True
            else:
                logger.error(f'{self.name}: {d1} {d2} Expected: {ans}, Recieved: {ret[:-1]}')
                return False
        except BrokenPipeError:
            logger.error(f'{self.name}: {d1} {d2} Seg Fault')
            load_proc()
            return False

        except Exception as e:
            logger.error(f'{self.name}: {d1} {d2} {e}')
            load_proc()
            return False

class PowTest:
    def __init__(self,bound_l=0,bound_r=M):
        self.bound_l = bound_l
        self.bound_r = bound_r
        self.name="pow"
    def run(self):
        d1 = random.randint(self.bound_l,self.bound_r)
        d2 = random.randint(self.bound_l,self.bound_r)
        return [self.res(d1,d2),
        self.res(d1,0),
        self.res(0,d1)]

    def res(self, d1, d2):
        ans =str(d1**d2) if d1!=0 else "0"
        try:
            p.stdin.write("6\n")
            p.stdin.write(str(d1)+'\n'+str(d2)+'\n')
            ret = p.stdout.readline()
            if ret[:-1]==ans:
                return True
            else:
                logger.error(f'{self.name}: {d1} {d2} Expected: {ans}, Recieved: {ret[:-1]}')
                return False
            
        except BrokenPipeError:
            logger.error(f'{self.name}: {d1} {d2} Seg Fault')
            load_proc()
            return False

        except Exception as e:
            logger.error(f'{self.name}: {d1} {d2} {e}')
            load_proc()
            return False

class GcdTest:
    def __init__(self,bound_l=0,bound_r=M):
        self.bound_l = bound_l
        self.bound_r = bound_r
        self.name="gcd"

    def run(self):
        d1 = random.randint(self.bound_l,self.bound_r)
        d2 = random.randint(self.bound_l,self.bound_r)
        return [self.res(d1,d2),
        self.res(d1,0),
        self.res(0,d1)]

    def res(self, d1, d2):
        def g(d1,d2):
            if d1==0 and d2==0:
                return 0
            elif d1==0 or d2==0:
                return max(d1,d2)
            elif d1<d2:
                g(d2,d1)
            while d1%d2!=0:
                d1,d2=d2,d1%d2
            return d2
        
        try:
            ans = str(g(d1,d2))
            p.stdin.write("7\n")
            p.stdin.write(str(d1)+'\n'+str(d2)+'\n')
            ret = p.stdout.readline()
            if ret[:-1]==ans:
                return True
            else:
                logger.error(f'Gcd: {d1} {d2} Expected: {ans}, Recieved: {ret[:-1]}')
                return False

        except BrokenPipeError:
            logger.error(f'Gcd: {d1} {d2} Seg Fault')
            load_proc()
            return False
        
        except Exception as e:
            logger.error(f'Gcd: {d1} {d2} {e}')
            load_proc()
            return False

class FactorialTest:
    def __init__(self,bound_l=0,bound_r=M):
        self.bound_l = bound_l
        self.bound_r = bound_r
        self.name="fact"

    def run(self):
        n = random.randint(self.bound_l,self.bound_r)
        return [self.res(n)]

    def res(self, n):
        def g(n):
            c=1
            for i in range(2,n+1):
                c*=i
            return c
        try:
            ans = str(g(n))
            p.stdin.write("8\n")
            p.stdin.write(str(n)+'\n')
            ret = p.stdout.readline()
            if ret[:-1]==ans:
                return True
            else:
                logger.error(f'Fact: {n} Expected: {ans}, Recieved: {ret[:-1]}')
                return False

        except BrokenPipeError:
            logger.error(f'Fact: {n} Seg Fault')
            load_proc()
            return False
        
        except Exception as e:
            logger.error(f'Fact: {n} {e}')
            load_proc()
            return False

class FibonacciTest:
    def __init__(self,bound_l=0,bound_r=M):
        self.bound_l = bound_l
        self.bound_r = bound_r
        self.name="fibo"

    def run(self):
        n = random.randint(self.bound_l,self.bound_r)
        return [self.res(n)]

    def res(self, n):
        def g(n):
            if n<=1:
                return n
            a,b=0,1
            for i in range(2,n+1):
                a,b = b,a+b
            return b
        try:
            ans = str(g(n))
            p.stdin.write("9\n")
            p.stdin.write(str(n)+'\n')
            ret = p.stdout.readline()
            if ret[:-1]==ans:
                return True
            else:
                logger.error(f'Fib: {n} Expected: {ans}, Recieved: {ret[:-1]}')
                return False

        except BrokenPipeError:
            logger.error(f'Fib: {n} Seg Fault')
            load_proc()
            return False
        
        except Exception as e:
            logger.error(f'Fib: {n} {e}')
            load_proc()
            return False
        
class BinCoefTest:
    def __init__(self,bound_l=0,bound_r=M):
        self.bound_l = bound_l
        self.bound_r = bound_r
        self.name="bin_coef"

    def run(self):
        n = random.randint(self.bound_l,self.bound_r)
        k = random.randint(self.bound_l,n)
        return [self.res(n,k)]

    def res(self, n,k):
        def f(n):
            c=1
            for i in range(1,n+1):
                c*=i
            return c
        try:
            ans = str(int(f(n)//f(k)//f(n-k)))
            p.stdin.write("10\n")
            p.stdin.write(str(n)+'\n')
            p.stdin.write(str(k)+'\n')
            ret = p.stdout.readline()
            if ret[:-1]==ans:
                return True
            else:
                logger.error(f'{self.name}: {n} Expected: {ans}, Recieved: {ret[:-1]}')
                return False
        except BrokenPipeError:
            logger.error(f'{self.name}: {n} Seg Fault')
            load_proc()
            return False
        except Exception as e:
            logger.error(f'{self.name}: {n} {e}')
            load_proc()
            return False

class CoinRowTest:
    def __init__(self,bound_l=1000,bound_r=2000,max_val=M):
        self.bound_l = bound_l
        self.bound_r = bound_r
        self.max_val =max_val
        self.name="coin_row"

    def run(self):
        n = random.randint(self.bound_l,self.bound_r)
        coins =[random.randint(1,self.max_val) for i in range(n)]

        return [self.res(coins)]

    def res(self,coins):
        def f():
            table = [0]*(len(coins)+1)
            table[0] = 0;
            table[1] = coins[0];

            for i in range(2,len(coins)+1):
                table[i] = max(coins[i-1] + table[i - 2], table[i - 1])
            return table[len(coins)]
        try:
            ans = str(f())
            p.stdin.write("11\n")
            p.stdin.write(str(len(coins))+'\n')
            for i in coins:
                p.stdin.write(f'{i} ')
            p.stdin.write('\n')
            ret = p.stdout.readline()
            if ret[:-1]==ans:
                return True
            else:
                logger.error(f'{self.name}: {" ".join(map(str,coins))} Expected: {ans}, Recieved: {ret[:-1]}')
                return False

        except BrokenPipeError:
            logger.error(f'{self.name}: {" ".join(map(str,coins))} Seg Fault')
            load_proc()
            return False
        
        except Exception as e:
            logger.error(f'{self.name}: {" ".join(map(str,coins))} {e}')
            load_proc()
            return False


class SearchTest:
    def __init__(self,bound_l=1000,bound_r=2000,max_val=M,name='lin_search'):
        self.bound_l = bound_l
        self.bound_r = bound_r
        self.max_val =max_val
        self.name=name

    def run(self):
        n = random.randint(self.bound_l,self.bound_r)
        data =[random.randint(1,self.max_val) for i in range(n)]

        return [
            self.res(data,data[random.randrange(0,n)]),
            self.res(data,random.randrange(0,n))
            ]

    def res(self,data:list,key:int):
        def f():
            return  data.index(key) if key in data else -1

        if self.name.startswith("l"):
            t='12\n'
        else:
            t='13\n'
            data.sort()
        try:
            ans = str(f())
            p.stdin.write(t)
            p.stdin.write(str(len(data))+'\n')
            p.stdin.write(str(key)+'\n')
            for i in data:
                p.stdin.write(f'{i} ')
            p.stdin.write('\n')
            ret = p.stdout.readline()
            if (key not in data and ret[:-1]=="-1") or (data[int(ret[:-1])]==key):
                return True
            else:
                logger.error(f'{self.name}: Key: {key} Data: {" ".join(map(str,data))} Expected: {ans}, Recieved: {ret[:-1]}')
                return False
        except BrokenPipeError:
            logger.error(f'{self.name}: Key: {key} Data: {" ".join(map(str,data))} Seg Fault')
            load_proc()
            return False
        
        except Exception as e:
            logger.error(f'{self.name}: Key: {key} Data: {" ".join(map(str,data))} {e}')
            load_proc()
            return False

class MaxMinTest:
    def __init__(self,bound_l=1000,bound_r=2000,max_val=M,name='max'):
        self.bound_l = bound_l
        self.bound_r = bound_r
        self.max_val =max_val
        self.name=name

    def run(self):
        n = random.randint(self.bound_l,self.bound_r)
        data =[random.randint(1,self.max_val) for i in range(n)]

        return [
            self.res(data)
            ]

    def res(self,data):
        def f():
            if self.name=='max':
               return data.index(max(data))
            else:
                return data.index(min(data))
        try:
            ans = str(f())
            t = "14\n" if self.name.startswith("ma") else "15\n"
            # print(t)
            p.stdin.write(t)
            p.stdin.write(str(len(data))+'\n')
            for i in data:
                p.stdin.write(f'{i} ')
            p.stdin.write('\n')
            ret = p.stdout.readline()
            if ret[:-1]==ans:
                return True
            else:
                logger.error(f'{self.name}: {" ".join(map(str,data))} Expected: {ans}, Recieved: {ret[:-1]}')
                return False
        except BrokenPipeError:
            logger.error(f'{self.name}: {" ".join(map(str,data))} Seg Fault')
            load_proc()
            return False
        
        except Exception as e:
            logger.error(f'{self.name}: {" ".join(map(str,data))} {e}')
            load_proc()
            return False

class SortTest:
    def __init__(self,bound_l=1000,bound_r=2000,max_val=M):
        self.bound_l = bound_l
        self.bound_r = bound_r
        self.max_val =max_val
        self.name='sort_asc'

    def run(self):
        n = random.randint(self.bound_l,self.bound_r)
        data =[random.randint(1,self.max_val) for i in range(n)]

        return [
            self.res(data)
            ]

    def res(self,data):
        def f():
            return " ".join(map(str,sorted(data)))
        try:
            ans = f()
            p.stdin.write("16\n")
            p.stdin.write(str(len(data))+'\n')
            for i in data:
                p.stdin.write(f'{i} ')
            p.stdin.write('\n')
            ret = p.stdout.readline()
            if ret.strip()==ans.strip():
                return True
            else:
                logger.error(f'{self.name}: {" ".join(map(str,data))} Expected: {ans}, Recieved: {ret[:-1]}')
                return False

        except BrokenPipeError:
            logger.error(f'{self.name}: {" ".join(map(str,data))} Seg Fault')
            load_proc()
            return False
        
        except Exception as e:
            logger.error(f'{self.name}: {" ".join(map(str,data))} {e}')
            load_proc()
            return False


#For one/two number based
# bound_l = min_val of random number
# bound_r = max_val of random number
# by default bound_l=0, bound_r=10^500

# For array based tests
# bound_l = minimum number of elements
# bound_r = maximum number of elements
# max_val = maximal value of element (0, max_val)
# might take long if you give very high values
# max_val by default = 10^500
# by default bound_l=1000,bound_r=2000
# look at each class for more information
# array based tests can have a max bound_r of 10000, to change this change c_len defined in test.c
tests = [
    AddTest(bound_r=100),
    DiffTest(bound_r=100),
    MulTest(bound_r=100),
    ModTest(bound_r=100),
    PowTest(bound_r=100),
    GcdTest(bound_r=100),
    FactorialTest(bound_r=100),
    FibonacciTest(bound_r=1000),
    BinCoefTest(bound_r=500),
    MaxMinTest(bound_l=5,bound_r=10,name='max',max_val=20),
    MaxMinTest(bound_l=5,bound_r=10,name='min',max_val=20),
    SearchTest(bound_l=5,bound_r=10,name='lin_search',max_val=20),
    SearchTest(bound_l=5,bound_r=10,name='bin_search',max_val=20),
    SortTest(bound_l=10,bound_r=20,max_val=20),
    CoinRowTest(bound_l=300,bound_r=2500,max_val=100)
]

for t in tests:
    score = 0
    tot=0
    with Bar(t.name,max=N) as bar:
        max_time,min_time=-1,10000000000000
        avg_time =0
        for i in range(N):
            time_start = time.time()
            ret = t.run()
            time_taken = (time.time()-time_start)*1000
            if time_taken>max_time:
                max_time = time_taken
            if time_taken<min_time:
                min_time = time_taken
            avg_time+=time_taken
            tot+=len(ret)
            score += sum(ret)
            bar.next()
        bar.finish()
        score_data =f'{t.name}: {score} / {tot} correct'
        time_data = f'{t.name}: Time Taken Avg: {avg_time/tot}ms Min: {min_time}ms Max: {max_time}ms'
        logger.info(time_data)
        logger.info(score_data )
        print(score_data)
        print(time_data)
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

def get_impl(path):
    cmd = f"gcc -g -I{dir_path} {dir_path}/test.c {path} -o {dir_path}/impl"
    c =subprocess.Popen(cmd,shell=True)
    c.communicate()
    return subprocess.Popen(
            f"{dir_path}/impl", 
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1)
    
p =  get_impl(args.p)
N = int(args.n)
M=10000000000
      
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
        p.stdin.write("1\n")
        p.stdin.write(str(d1)+'\n')
        p.stdin.write(str(d2)+'\n')
        ret = p.stdout.readline()
        if ret[:-1]==ans:
            return True
        else:
            logger.errorbug(f'Add: {d1} {d2} Expected: {ans}, Recieved: {ret[:-1]}')
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
        p.stdin.write("2\n")
        p.stdin.write(str(d1)+'\n')
        p.stdin.write(str(d2)+'\n')
        ret = p.stdout.readline()
        if ret[:-1]==ans:
            return True
        else:
            logger.errorbug(f'Add: {d1} {d2} Expected: {ans}, Recieved: {ret[:-1]}')
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
        p.stdin.write("3\n")
        p.stdin.write(str(d1)+'\n'+str(d2)+'\n')
        ret = p.stdout.readline()
        if ret[:-1]==ans:
            return True
        else:
            logger.error(f'Cmp: {d1} {d2} Expected: {ans}, Recieved: {ret[:-1]}')
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
        p.stdin.write("4\n")
        p.stdin.write(str(d1)+'\n'+str(d2)+'\n')
        ret = p.stdout.readline()
        if ret[:-1]==ans:
            return True
        else:
            logger.error(f'Mul: {d1} {d2} Expected: {ans}, Recieved: {ret[:-1]}')
            return False

class ModTest:
    def __init__(self,bound_l=0,bound_r=M):
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
        p.stdin.write("5\n")
        p.stdin.write(str(d1)+'\n'+str(d2)+'\n')
        ret = p.stdout.readline()
        if ret[:-1]==ans:
            return True
        else:
            logger.error(f'Mod: {d1} {d2} Expected: {ans}, Recieved: {ret[:-1]}')
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
        ans =str(d1**d2)
        p.stdin.write("6\n")
        p.stdin.write(str(d1)+'\n'+str(d2)+'\n')
        ret = p.stdout.readline()
        if ret[:-1]==ans:
            return True
        else:
            logger.error(f'Pow: {d1} {d2} Expected: {ans}, Recieved: {ret[:-1]}')
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
            if d1==0 or d2==0:
                return 0
            if d1<d2:
                g(d2,d1)
            while d1%d2!=0:
                d1,d2=d2,d1%d2
                # print(d1,d2)
            return d2
        ans = str(g(d1,d2))
        p.stdin.write("7\n")
        p.stdin.write(str(d1)+'\n'+str(d2)+'\n')
        ret = p.stdout.readline()
        if ret[:-1]==ans:
            return True
        else:
            logger.error(f'Gcd: {d1} {d2} Expected: {ans}, Recieved: {ret[:-1]}')
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
        
        ans = str(g(n))
        p.stdin.write("8\n")
        p.stdin.write(str(n)+'\n')
        ret = p.stdout.readline()
        if ret[:-1]==ans:
            return True
        else:
            logger.error(f'Fact: {n} Expected: {ans}, Recieved: {ret[:-1]}')
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
            a,b=0,1
            for i in range(2,n+1):
                a,b = b,a+b
            return b
        
        ans = str(g(n))
        p.stdin.write("9\n")
        p.stdin.write(str(n)+'\n')
        ret = p.stdout.readline()
        if ret[:-1]==ans:
            return True
        else:
            logger.error(f'Fib: {n} Expected: {ans}, Recieved: {ret[:-1]}')
            return False

tests = [
    AddTest(),
    DiffTest(),
    MulTest(),
    ModTest(),
    PowTest(bound_r=1000),
    GcdTest(),
    FactorialTest(bound_r=100),
    FibonacciTest(bound_r=1000)
]

for t in tests:
    score = 0
    tot=0
    with Bar(t.name,max=N) as bar:
        for i in range(N):
            ret = t.run()
            tot+=len(ret)
            score += sum(ret)
            bar.next()
        bar.finish()
        logger.info(f'{t.name}: {score} / {tot} correct' )
        print(f"{t.name}: ",score,"/",tot,'correct')
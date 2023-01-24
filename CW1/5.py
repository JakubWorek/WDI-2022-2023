#program wyznaczający pierwiastek kwadratowy ze wzoru Newtona

def newton_sqrt(n):
    a = n/2
    e=0.0001

    while(abs((n/a)-a)>e):
        a=(a+(n/a))/2

    return a
	
def main():
    n=float(input("Podaj n: "))
    print(newton_sqrt(n))

if __name__ == "__main__": main()
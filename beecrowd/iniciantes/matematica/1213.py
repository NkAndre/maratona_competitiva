import sys

def resolver():
    for linha in sys.stdin:
        if not linha.strip():
            continue
            
        n = int(linha)
        
        valor = 1
        digitos = 1
        
        while valor % n != 0:
         
            valor = (valor * 10 + 1) % n
            digitos += 1
            
        
        print(digitos)

if __name__ == '__main__':
    resolver()

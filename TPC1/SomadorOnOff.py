import sys

def somador_on_off(text):
    soma = 0
    ativo = True  # O somador começa ativo
    
    palavras = text.split()
    
    for palavra in palavras:
        if palavra.lower() == "off":
            ativo = False
        elif palavra.lower() == "on":
            ativo = True
        elif "=" in palavra:
            print(soma)
        else:
            num = "".join(filter(str.isdigit, palavra))  # Extrai os dígitos da palavra
            if num.isdigit() and ativo:
                soma += int(num)

    print(soma)

if __name__ == "__main__":
    texto = sys.stdin.read()
    somador_on_off(texto)
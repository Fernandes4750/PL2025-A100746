import re 
from collections import defaultdict

def main():
    # Caminho do ficheiro CSV
    file_path = "obras.csv"

    # Expressão Regular para capturar apenas Título, Período e Compositor
    pattern = re.compile(r'([^;]+);("(?:[^"]*(?:"[^"]*)*)"|[^;]+);([^;]+);([^;]+);([^;]+);([^;]*)\n?')

    # Dicionários para armazenar os dados extraídos
    compositores = set()
    distribuicao_periodos = defaultdict(int)
    obras_por_periodo = defaultdict(list)

    # Ler e processar o ficheiro sem usar csv.reader()
    with open(file_path, 'r', encoding='utf-8') as obras:
        proxima_linha = False
        buffer = ""
        for linha in obras:
            if not proxima_linha:
                proxima_linha = True
                continue

            buffer += linha
            match = re.match(pattern, buffer)
            if match:
                nome = match.group(1)
                periodo = match.group(4)
                compositor = match.group(5)

                compositores.add(compositor)

                if periodo in distribuicao_periodos:
                    distribuicao_periodos[periodo] += 1
                else : distribuicao_periodos[periodo] = 0

                if periodo not in obras_por_periodo:
                    obras_por_periodo[periodo] = []
                obras_por_periodo[periodo].append(nome)
                buffer = ""

    # Ordenar os compositores e as obras dentro de cada período
    compositores = sorted(compositores)
    for periodo in obras_por_periodo:
        obras_por_periodo[periodo].sort()

    # Exibir os resultados
    print("\n### Lista de Compositores (Ordenada) ###")
    for compositor in compositores:
        print(compositor)

    print("\n### Distribuição de Obras por Período ###")
    for periodo, quantidade in distribuicao_periodos.items():
        print(f"{periodo}: {quantidade} obras")

    print("\n### Obras Organizadas por Período ###")
    for periodo, obras in obras_por_periodo.items():
        print(f"\n{periodo}:")
        for obra in obras:
            print(f"  - {obra}")



if __name__ == "__main__":
    main()


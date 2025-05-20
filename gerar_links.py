import csv

BASE_URL = "https://seuusuario.github.io/convite"
CSV_ENTRADA = "convidados.csv"
CSV_SAIDA = "links_gerados.csv"

links = []

with open(CSV_ENTRADA, mode="r", encoding="utf-8") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    for linha in leitor:
        nome = linha["Nome"].strip()
        codigo = linha["Código"].strip()
        link = f"{BASE_URL}/?nome={nome.replace(' ', '%20')}&codigo={codigo}"
        links.append([nome, codigo, link])

with open(CSV_SAIDA, mode="w", encoding="utf-8", newline="") as arquivo_saida:
    escritor = csv.writer(arquivo_saida)
    escritor.writerow(["Nome", "Código", "Link"])
    escritor.writerows(links)

print(f"{len(links)} links gerados com sucesso! Veja o arquivo '{CSV_SAIDA}'.")
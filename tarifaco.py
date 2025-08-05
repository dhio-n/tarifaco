import requests
from bs4 import BeautifulSoup
import csv
from deep_translator import GoogleTranslator
from tqdm import tqdm  # Barra de progresso

# URL da página
URL = "https://www.whitehouse.gov/presidential-actions/2025/07/addressing-threats-to-the-us/"
headers = {"User-Agent": "Mozilla/5.0"}

# Requisição da página
response = requests.get(URL, headers=headers)
response.raise_for_status()

# Parse HTML com BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Busca a tabela
table = soup.find("table", class_="has-fixed-layout")
if not table:
    raise ValueError("Tabela com classe 'has-fixed-layout' não encontrada.")

# Extrai cabeçalhos
headers = [th.get_text(strip=True) for th in table.find_all("th")]
headers.append("Descrição Traduzida")

# Extrai todas as linhas da tabela
raw_rows = [tr for tr in table.find_all("tr") if tr.find_all("td")]

# Barra de progresso usando tqdm
rows = []
for tr in tqdm(raw_rows, desc="Traduzindo linhas"):
    cols = [td.get_text(strip=True) for td in tr.find_all("td")]
    if cols:
        try:
            # Traduz a 3ª coluna (se existir)
            texto_original = cols[2] if len(cols) >= 3 else ""
            traducao = GoogleTranslator(source='en', target='pt').translate(texto_original) if texto_original else ""
        except Exception as e:
            traducao = f"Erro na tradução: {e}"
        cols.append(traducao)
        rows.append(cols)

# Salva o CSV com a nova coluna
csv_filename = "tabela_whitehouse_traduzida.csv"
with open(csv_filename, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"\n✅ Tradução finalizada! {len(rows)} linhas salvas em '{csv_filename}'.")

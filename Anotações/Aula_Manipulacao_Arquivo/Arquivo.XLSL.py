import openpyxl
from openpyxl.styles import Font, Border, Fill

# Cria a pasta de trabalho
workbook = openpyxl.Workbook()

# Seleciona a planilha ativa
worksheet = workbook.active

# Define o título da planilha
worksheet.title = "Minha Planilha"

# Escreve dados na planilha
worksheet["A1"] = "Nome"
worksheet["B1"] = "Idade"
worksheet["A2"] = "João"
worksheet["B2"] = 30
worksheet["A3"] = "Maria"
worksheet["B3"] = 25

# Aplica formatação
font = Font(name='Arial', size=12, bold=True)
worksheet["A1"].font = font
worksheet["A1"].border = Border(left=None, right=None, top=None, bottom=None)

# Define o estilo da célula
cell_style = Fill()
worksheet["A1"].fill = cell_style

# Salva o arquivo XLSX
workbook.save("minha_planilha.xlsx")
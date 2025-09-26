# 📁 Organizador de Arquivos por Extensão

Este script em Python organiza automaticamente os arquivos de uma pasta selecionada pelo usuário, movendo-os para subpastas de acordo com suas extensões (como imagens, documentos, planilhas, etc.). É ideal para manter diretórios limpos e organizados com apenas um clique.

---

## ✅ Funcionalidades

- Interface gráfica para seleção da pasta (via `tkinter`).
- Criação automática de subpastas conforme o tipo de arquivo.
- Organização baseada em extensões de arquivos.
- Compatível com Windows, macOS e Linux.

---

## 🧠 Como Funciona

1. **Seleção da Pasta**:  
   O script abre uma janela para o usuário escolher a pasta que deseja organizar.

2. **Listagem de Arquivos**:  
   Ele lê todos os arquivos presentes na pasta selecionada.

3. **Mapeamento de Extensões**:  
   Possui um dicionário chamado `locais` que define quais extensões pertencem a quais categorias:
   
   ```python
   locais = {
       "imagens": [".png", ".jpg"],
       "planilhas": [".xlsx", ".csv"],
       "pdfs": [".pdf"],
       "zips": [".zip", ".rar"],
       "programas": [".exe", ".msi"],
       "anotações": [".txt", ".docx"]
   }
   ```

4. **Organização dos Arquivos**:
   - Para cada arquivo, ele verifica sua extensão.
   - Se a extensão estiver em alguma das categorias, move o arquivo para a subpasta correspondente.
   - Se a subpasta ainda não existir, ela será criada automaticamente.

---

## 🚀 Como Usar

1. **Requisitos**:
   - Python 3.x instalado.
   - Biblioteca `tkinter` (geralmente já vem com o Python).

2. **Executando o Script**:
   Salve o código em um arquivo chamado `organizer.py` e execute com:

   ```bash
   python organizer.py
   ```

3. **Selecione a pasta**:
   - Uma janela se abrirá pedindo para você escolher a pasta que deseja organizar.
   - O script fará a organização automaticamente após a seleção.

---

## 🧩 Exemplo de Resultado

**Antes:**
```
Downloads/
├── imagem1.jpg
├── documento.pdf
├── planilha.xlsx
├── instalador.exe
```

**Depois:**
```
Downloads/
├── imagens/
│   └── imagem1.jpg
├── pdfs/
│   └── documento.pdf
├── planilhas/
│   └── planilha.xlsx
├── programas/
│   └── instalador.exe
```


---


Você pode modificar e adaptar este código conforme suas necessidades!

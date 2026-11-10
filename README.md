[System.IO.File]::WriteAllText("$PWD\README.md", @'
# 🚀 Missão Marte: ECLSS - Automação de Testes

[![ECLSS Test Automation Pipeline](https://github.com/Jadson-Porto/ATS13/actions/workflows/pipeline.yml/badge.svg)](https://github.com/Jadson-Porto/ATS13/actions/workflows/pipeline.yml)

Este repositório contém a suíte de testes automatizados para o sistema de suporte de vida (ECLSS) do Habitat de Marte.

## 🛠️ Tecnologias Utilizadas
- **Python 3.10+**
- **Pytest** (Testes Unitários e de Integração)
- **Pytest-Mock** (Isolamento de dependências com Dublês)
- **Selenium WebDriver** (Testes E2E Web Headless)
- **Pytest-BDD** (Cenários em Gherkin)
- **GitHub Actions** (Integração Contínua)

## 🚀 Execução Local dos Testes

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Jadson-Porto/ATS13.git](https://github.com/Jadson-Porto/ATS13.git)
   cd ATS13
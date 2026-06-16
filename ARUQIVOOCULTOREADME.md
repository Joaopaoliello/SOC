 Windows Persistence & Startup Analyzer (Python)

Este projeto em Python analisa entradas de inicialização do Windows através do Registro do sistema, com foco educacional em cibersegurança e análise de persistência de programas no sistema operacional.

Ele permite visualizar programas configurados para iniciar automaticamente com o Windows e realiza verificações básicas sobre os arquivos associados.

---

 Funcionalidades

- Acessa a chave de inicialização do Windows:
HKCU\Software\Microsoft\Windows\CurrentVersion\Run

- Lista todos os programas configurados para inicialização automática
- Exibe nome e caminho dos executáveis
- Verifica se o arquivo existe no sistema
- Detecta se o arquivo está marcado como oculto
- Itera corretamente sobre todas as entradas do Registro
- Trata erros quando não há mais valores disponíveis

---

Conceitos de Cibersegurança

Este projeto aborda fundamentos importantes usados em análise de sistemas e malware:

 Persistência no Windows
Muitos programas maliciosos utilizam chaves como `Run` e `RunOnce` para garantir execução automática ao iniciar o sistema.

---

 Windows Registry
O Registro do Windows é um banco de dados interno que armazena configurações do sistema, usuários e aplicações.

---

 Enumeração de entradas
Uso de `winreg.EnumValue()` para percorrer valores dentro de uma chave do Registro.

---

 Análise de arquivos
Uso do módulo `os` para:

- Verificar existência de arquivos
- Confirmar se é um arquivo válido
- Detectar atributos como “Hidden”

---

Análise básica de comportamento suspeito
O script identifica possíveis sinais de ocultação de arquivos associados à inicialização do sistema.

---

Tecnologias utilizadas

- Python 3.x
- Módulo padrão `winreg`
- Módulo padrão `os`

---



Este projeto deve ser executado em sistema Windows.


🔐 Gerenciador de Senhas com Interface Gráfica

Este é um projeto de Gerenciador de Senhas feito em Python com interface gráfica usando tkinter. Ele permite gerar senhas fortes, armazená-las por serviço (ex: Google, YouTube, Telegram), visualizar ou ocultar senhas salvas, e tudo isso com um design agradável.

🛠️ Tecnologias Utilizadas

Python 3

Tkinter (GUI)

JSON (para armazenamento local)

String, Random (para geração de senhas)

🎨 Funcionalidades



🚀 Como Executar

Tenha o Python 3 instalado

Salve o código principal como gerenciador_senhas.py

Execute com:

python gerenciador_senhas.py

📁 Estrutura de Arquivos

📦Projeto
 ┣ 📄 gerenciador_senhas.py
 ┗ 📄 senhas.json  ← criado automaticamente após salvar uma senha

🧠 Exemplos de Uso

Você quer salvar uma senha gerada para o Google: digite "Google" no campo de serviço e clique em gerar. Depois é só salvar.

Para ver as senhas salvas, marque a caixa "Mostrar senhas salvas"

🔒 Segurança

Este projeto salva as senhas localmente em um arquivo JSON. Para produção, recomenda-se usar criptografia ou armazenar em banco de dados seguro.

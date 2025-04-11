# ai-assisted-learn
 Repositório que faz a análise dos dados do repositório do laplin relacionado ao projeto de pesquisa de aprendizagem assistida por IA


# Como configurar o ambiente e ver as células corretamente

### 1. **Clonar o Repositório**:
- Use o Github Desktop ou então a CLI do git bash para poder clonar o repositório, através do comando simples:

  `git clone https:github.com/athavus/ai-assisted-learn.git` ou use a conexão por ssh.

### 2. Iniciar o **Ambiente Virtual**
- É interessante que se crie uma venv para o projeto, então basta criar uma com qualquer nome, no projeto original eu chamei a minha de pyepye.

  `python -m venv pyepye` o nome da sua venv iria no lugar de "pyepye"
- Depois de criar a venv, é preciso ativar a mesma.
  - Estando no diretório do projeto (não o da venv) basta digitar no terminal:
  `pyepye\Scripts\activate` **no Windows**
  `source pyepye/bin/activate` **no Linux** (dependendo do seu shell pode ser um pouco diferente).

### 3. Instalar as **Dependências**
- Instalar as bibliotecas utilizadas no projeto.

  `pip install -r requirements.txt`

### Com tudo feito, o projeto deve funcionar normalmente 
# Chat Bot com Strealit e LangChain

Fiz um chatbot que te responde baseado nos dados que estão no PDF que você escolher.
Usei o framework **LangChain**.
Esse framework é voltado a LLM's e nos ajuda a produzir softwares com IA's.

---

## REQUISITOS:
- Possuir o Python instalado.
- Ter uma API_KEY da OpenAI, ou alguma outra LLM (se for outra LLM, vai ter que mexer um pouco no código).
- Ter uma API_KEY do LangChain.

---

## INSTRUÇÕES:

1. Crie um ambiente virtual na pasta do projeto e entre nele.
2. No arquivo chamado `.env` e coloque suas API_KEYS nele.
3. Execute o comando: `pip install -r requirements.txt`.

   Se der algum problema na execução do `pip install`:
   - Baixe o [Visual Studio Build Tools](https://visualstudio.microsoft.com/pt-br/visual-cpp-build-tools/).
   - Clique no executável e procure "Desenvolvimento para desktop com C++".
   - Tente executar o comando `pip install` novamente.

4. Com tudo feito, ligue o projeto com o comando `streamlit run streamlit_app.py`.

---

## PARA RODAR OS EXECUTÁVEIS:

## MACOS:

1. Digite no prompt: chmod +x setup_env.sh run_streamlit.sh
2. Rode os executáveis pelo prompt, 1° o Setup, 2° o Run.

## WINDOWS:

1. Digite no PowerShell: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
2. Rode os executáveis pelo prompt, 1° o Setup, 2° o Run.



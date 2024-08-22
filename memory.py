from carregar_pdf import load_pdf


def enviar_mensagem(mensagem_enviada, filename):
    mensagem = load_pdf(filename).invoke({"input": mensagem_enviada},)
    return mensagem['answer']




def render_message(chat):
    """Renderiza uma única mensagem de chat no formato HTML."""
    alignment_class = '' if chat.origin == 'ai' else 'row-reverse'
    bubble_class = 'ai-bubble' if chat.origin == 'ai' else 'human-bubble'
    icon_src = 'ai_icon.png' if chat.origin == 'ai' else 'user_icon.png'
    
    return f"""<div class="chat-row {alignment_class}">
            <img class="chat-icon" src="app/static/{icon_src}" width=32 height=32>
            <div class="chat-bubble {bubble_class}">
                {chat.message}
            </div>
        </div>
    """

def render_chat(history):
    """Renderiza todo o histórico de chat como um único bloco de HTML."""
    wrapper = "<div class='chat-wrapper'>"
    for index, chat in enumerate(history):
        wrapper += render_message(chat)
    wrapper += "</div>"
    return wrapper
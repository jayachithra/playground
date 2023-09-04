import tiktoken

# ref: token limit for history https://github.com/Azure/openai-samples/blob/main/Basic_Samples/Chat/chatGPT_managing_conversation.ipynb
def get_tokens_from_message(history: str, model="gpt-3.5-turbo"):
    """Get the number of tokens in a message"""
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = 0
    for message in history:
        num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":  # if there's a name, the role is omitted
                num_tokens += -1  # role is always required and always 1 token
    num_tokens += 2  # every reply is primed with <im_start>assistant
    return num_tokens
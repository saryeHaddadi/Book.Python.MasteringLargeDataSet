
web_answers = [
    {
        "headers": ("01/19/2018", "Mozilla", "300"),
        "response": {"text": "Hello world!","encoding": "utf-8"}
    },
    {
        "headers": ("01/19/2018", "Chrome", "404"),
        "response": {"text":"No page found", "encoding":"ascii"}
    },
    {
        "headers": ("01/20/2018", "Mozilla", "300"),
        "response": {"text":"Yet another web page.", "encoding":"utf-8"}}
]

def get_page_text(list_answer):
    return list_answer['response']['text']

# for answer in web_answers:
#     print(get_page_text(answer))

print(list(map(get_page_text, web_answers)))

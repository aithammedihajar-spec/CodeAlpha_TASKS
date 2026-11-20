from deep_translator import MyMemoryTranslator
while True:

    text = input('the text you want to translate (or "exit" to quit): ')
    if text.lower() == 'exit':
     print("Goodbye")
     break
    source_lang = input('the language of text \'english , french , arabic ,.... \':')
    target_lang = input('the language to translate \'english , french , arabic ,.... \':')

    resultat = MyMemoryTranslator(source=source_lang, target=target_lang ).translate(text)

    print("translation:",resultat)      
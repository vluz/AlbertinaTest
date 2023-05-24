# Teste rápido e simples do modelo Albertina PT-PT por Victor Luz
# Modelo: https://huggingface.co/PORTULAN/albertina-ptpt
# Publicação: https://arxiv.org/abs/2305.06721
# Python ligeiramente modificado para teste geral
# Não usar em produção, não testado

from transformers import pipeline

unmasker = pipeline('fill-mask', model='PORTULAN/albertina-ptpt')

print("Modelo: PORTULAN/albertina-ptpt")
print("Entre uma frase com [MASK] em vez de uma palavra para obter uma predição do modelo,")
print("ou pressione ENTER para correr com a frase de exemplo.")

frase = input('>')
if frase == "":
    frase = "A culinária portuguesa é rica em sabores e [MASK], tornando-se um dos maiores tesouros do país."

resultado = unmasker(frase)

print(frase)
print("Pontuação   Palavra            Resultado")

for i in resultado:
    print(str(i["score"]*100)[:4],'%     ', i["token_str"].ljust(18), i["sequence"])
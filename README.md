# Albertina Test
### Teste rápido e simples do modelo Albertina pt-PT

<hr>

**Modelo:** https://huggingface.co/PORTULAN/albertina-ptpt
<br>
**Publicação:** https://arxiv.org/abs/2305.06721

Python ligeiramente modificado para teste com qualquer frase

**Atenção:** Não usar em produção, não testado

Requerimentos: `transformers`

Para instalar basta apenas correr `git clone https://github.com/vluz/Albertina-Test.git`
<br>
De seguida correr `pip install -r requirements.txt`
<br>
Depois correr `python test.py` para executar

Resultado esperado e exemplos:

```
A culinária portuguesa é rica em sabores e [MASK], tornando-se um dos maiores tesouros do país.
Pontuação   Palavra            Resultado
91.6 %      aromas             A culinária portuguesa é rica em sabores e aromas, tornando-se um dos maiores tesouros do país.
2.29 %      costumes           A culinária portuguesa é rica em sabores e costumes, tornando-se um dos maiores tesouros do país.
1.39 %      cores              A culinária portuguesa é rica em sabores e cores, tornando-se um dos maiores tesouros do país.
0.98 %      nuances            A culinária portuguesa é rica em sabores e nuances, tornando-se um dos maiores tesouros do país.
0.72 %      aroma              A culinária portuguesa é rica em sabores e aroma, tornando-se um dos maiores tesouros do país.
```

<br>

```
Quero ver o [MASK] da casa
Pontuação   Palavra            Resultado
18.2 %      layout             Quero ver o layout da casa
12.7 %      valor              Quero ver o valor da casa
7.10 %      interior           Quero ver o interior da casa
5.75 %      site               Quero ver o site da casa
5.17 %      estado             Quero ver o estado da casa
```

<br>

```
A [MASK] é inimiga da perfeição
Pontuação   Palavra            Resultado
36.7 %      vida               A vida é inimiga da perfeição
10.7 %      culpa              A culpa é inimiga da perfeição
5.40 %      Primavera          A Primavera é inimiga da perfeição
4.37 %      Alma               A Alma é inimiga da perfeição
3.43 %      alma               A alma é inimiga da perfeição
```

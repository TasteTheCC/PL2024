TPC4 \
**Título**: Analisador Léxico \
**Autor**: Carlos Costa, 88551

##Excerto da blackboard:

**Analisador Léxico:**

Construir um analisador léxico para uma liguagem de *query* com a qual se podem escrever frases do género:

`Select id, nome, salario From empregados Where salario >= 820`



##Abordagem:
- Definir expressoes reservadas (Select...From...Where)
- Definir lista de regex para os tokens
- Definir tratamento de erro
- Criaçao do analisador lex

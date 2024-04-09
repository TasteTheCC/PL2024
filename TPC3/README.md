#TPC3
**Título**: Somador On/Off \
**Autor**: Carlos Costa, 88551

##Excerto da blackboard:

**Somador on/off: criar o programa em Python**

#Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
    1.Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
    2.Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
    3.Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.

##Abordagem:
- Leitura por STDIN.
- Uso de expressão regular para identificar flags.
- Inicialização do estado a True, considerando a ordem dos requisitos do programa.
- Reset da contagem ao desligar o comportamento e ao imprimir o resultado.
# Explicação do código em Python
O script apresentado é um programa em Python que implementa uma calculadora interativa no terminal. Aqui está uma explicação detalhada de cada parte:


# 1. Definição da função calculadora:
A função calculadora é criada para realizar operações matemáticas básicas como soma, subtração, multiplicação e divisão.


# 2. Loop infinito (while True):
O programa entra em um loop que só será interrompido se o usuário decidir não continuar. Isso permite realizar várias operações consecutivas.


# 3. Entrada de dados:
O usuário é solicitado a:
Digitar dois números (num1 e num2) que serão usados na operação.
Escolher a operação matemática a ser realizada entre soma (+), subtração (-), multiplicação (*) ou divisão (/).


# 4. Estrutura de decisão (if/elif/else):
Com base na operação escolhida:
Soma (+): os dois números são somados.
Subtração (-): o segundo número é subtraído do primeiro.
Multiplicação (*): os dois números são multiplicados.
Divisão (/): verifica se o segundo número é zero antes de dividir, para evitar erro.
Se o operador fornecido for inválido, o programa exibe uma mensagem e volta ao início do loop.


# 5. Tratamento de divisão por zero:
Um controle especial é incluído para evitar a divisão por zero, exibindo uma mensagem de erro ao invés de gerar uma exceção.


# 6. Exibição do resultado:
Após realizar a operação, o resultado é mostrado no terminal.


# 7. Pergunta de continuidade:
O usuário é perguntado se deseja continuar usando a calculadora. Caso responda com "n" (não), o loop é encerrado e a função termina.


# Execução do arquivo sh

cd modulo1/linux/exercicio

Este comando direciona até o diretorio onde o arquivo foi salvo(caso não tenha os mesmos diretórios, atribua iguais ao o seu)

chmod +x exercicio_ebac.sh

Este comando atribui permissão de execução ao arquivo exercicio_ebac.sh. Isso significa que o arquivo pode ser executado como um programa/script no sistema operacional.

chmod 644 exercicio_ebac.sh

Este comando altera as permissões do arquivo para 644, o que significa:
Dono do arquivo: Leitura e escrita.
Grupo: Apenas leitura.
Outros usuários: Apenas leitura.

python3 exercicio_ebac.sh 

Este comando executa o arquivo em python

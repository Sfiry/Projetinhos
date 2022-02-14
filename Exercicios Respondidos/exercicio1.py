# Um e-commerce de livros está fazendo uma promoção para pagamento à vista, no boleto, em que é aplicado,
# pelo sistema, um entre os três critérios de desconto: • Critério A: R$ 0,25 por livro + R$ 7,50 fixo; • Critério B:
# R$ 0,50 por livro + R$ 2,50 fixo; • Critério C: R$ 0,65 por livro + R$ 1,50 fixo. Escreva um algoritmo em VisualG
# em que o usuário informe a quantidade de livros que deseja comprar, e oalgoritmo informa qual é a melhor opção de
# desconto (desconsidere que há opções iguais).

# Solução:

var = int(input('Por favor digite a quantidade de livros: '))
ca = 0.25 * var + 7.50
cb = 0.50 * var + 2.50
cc = 0.65 * var + 1.50
if ca < cb:
    print('O Cupom A é a melhor opção R$:', ca)
elif cb < cc:
    print('O Cupom B é a melhor opção R$:', cb)
elif cc < cb:
    print('O Cupom C é a melhor opção R$:', cc)
input('Obrigado por utilizar, pressione qualquer tecla para sair.')

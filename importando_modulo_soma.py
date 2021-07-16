
#esse programa mostra como reutilizar códigos já escritos, o módulo está sendo importado de uma classe;

from classe_soma import somar

entrada = somar(valor1=  int(input('valor1 : ')), valor2 = int(input('valor2 = ')))

entrada.mostra_soma()
entrada.mostra_div_frac()
entrada.mostrar_poten()

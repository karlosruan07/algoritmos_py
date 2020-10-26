#neste programa mostra como importar uma classe criada anteriormente.

from classe_medico import medico #aqui importamos o nome do arquivo que contém a classe, e o nome da classe que está no arquivo
from classe_hospital import hospital 

medico01 = medico(nome='Ruan', crm='12345')

hospital01 = hospital(nome='Regional', tipo='cirurgico', especialidade='coração', avaliacao='Boa')

medico01.mostrar_medico()
hospital01.mostrar()


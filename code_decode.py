#Este programa demostra a funcionalidade dos médotos encode e decode de strings

import base64
nome = 'Ruan'

codificacao = base64.b64encode(b'Ruan')

decode = base64.b64decode(codificacao)

print(decode)


'''codificação = base64.encodebytes(b'Ruann')
print(codificação)'''
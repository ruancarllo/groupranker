# [Groupranker](https://github.com/ruancarllo/winder) &middot; ![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square) ![Language](https://img.shields.io/badge/Language-Python-darkslateblue?style=flat-square)

Este programa escrito em [Python](https://www.python.org) tem a capacidade de analisar um *chat* em grupo de [WhatsApp](https://www.whatsapp.com) exportado para texto, tranformando-o em uma planilha CSV contendo a distribuição da quantidade de mensagens por pessoa, em determinados intervalos de tempo regulares.

É útil, portanto, para a feitura de gráficos animados ou rankings.

## Execução

Para rodar o script principal do software, siga as seguintes etapas:

1. Instale a última versão do Python em seu computador.

2. Abra a pasta [source](./source) deste projeto, e coloque nela o arquivo de exportação **_chat.txt**.

3. Execute o seguinte comando de shell:

```shell
python groupranker.py _chat.txt
```

De modo que outro caminho de arquivo também pode ser utilizado no lugar desse padrão mostrado.
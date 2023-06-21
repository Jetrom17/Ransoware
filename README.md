
<h1 align="center">
<br>
  <img src=https://static.timesofisrael.com/www/uploads/2021/07/iStock-1188482164-e1627299833752.jpg width=300></img><br>
<br>
</h1>

<p align="center">Exemplo de um ransomware que criptografa arquivos</p>
<br>

### Python Script  
[bot.py] | [decod.py]
> - Cria arquivo __Read.txt__ após criptografar
> - Define `key = b"1234567890123456"  # Chave de 16 bytes (128 bits)` ou use `key = os.urandom(16)`
> - Para decoder, use o arquivo [decod.py] - Não funciona com `key = os.urandom(16)` ativo.

_Uso educativo e para brincadeiras entre colegas. Além disso o código fonte foi baseado no [Al0nnso](https://github.com/Al0nnso/YOUTUB3/tree/main/BOB-Ransomware), a diferença está no decoder e forma de customização do código._

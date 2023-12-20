# Algoritmo LBHP
 <h2 Align="justify"><p>O Local Binary Histogram Pattern (LBHP) é um algoritmo utilizado para a se obter as características de textura nas imagens. Sua principal função é identificar onde ocorrem as variações locais das texturas dos pixels da imagem.<br>
<p>O conceito principal do LBHP é o Local Binary Pattern (LBHP), que compara o valor de um pixel central com o valor de seus vizinhos. Se o valor do pixel vizinho for maior que o valor do pixel central, o pixel vizinho terá seu valor alterado para 0 e caso seja maior, para 1. Uma vez que é obtido um padrão de binários, esses são colocados em um histograma que irá dizer o número de vezes que cada padrão aparece na imagem.<br>
<p>Ao final desse processo, tem-se algo que é chamado de “representação compacta das texturas locais na imagem”.
</h2>
<br>
<div Align="center">
<img src="https://updatedcode.files.wordpress.com/2017/11/1_j16_dkusrnah3wddqwkena.png" alt="Img_LBHP"  height="250" width="750">
</div>



# Algoritmo EigenFace
 <h2 Align="justify"><p>O EigenFace utiliza algumas características do rosto para detecção facial, como os aspectos faciais como o formato do rosto, olhos, boca e nariz.<br>
<p>Ele usa desse mecanismo para o reconhecimento facial, primeiramente o algoritmo reconhece as
principais características do rosto e posteriormente ele descarta as outras informações que não são relevantes para a detecção facial. Este processo é nomeado como Análise de Componentes Principais.<br>
<p>Após extrair as principais características das faces, o classificador irá gerar diversas EigenFace (Fotos fantasmas). A soma de todos os pesos fará que ele gere uma face média e com a computação linear será possível a reconstrução da face original.
</h2>
<br>
<div Align="center">
<img src="https://www.baeldung.com/wp-content/uploads/sites/4/2023/03/eigenface_example.png" alt="Img_eigen"  height="250" width="750">
</div>


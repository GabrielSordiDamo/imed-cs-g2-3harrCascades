<h6>IMED, G2, CV</h6>
                                       <h5 align="center">COMO PODE-SE TREINAR UMA REDE PARA SER USADA NO PYTHON COM O CV2?</h5>
  <ol>                    
 <li>
   <p align="justify">
 O primeiro item da nossa lista e perguntar, o que permite um computador, por exemplo, identificar um ser um determinado objeto em uma image?
 Uma das linhas de raciocinio que podemos seguir, e pensando que o computador pode memorizar o objeto que estamos tentando idenficar (vamos imaginar que queremos identificar          laranjas em uma imagem). Entao poriamos "servir" ao nosso computador uma serie de imagens de laranjas, para que ele as memorizasse e entao, sempre que servisimos uma imagem qualquer para o computador, ele nos disse se ha ou nao uma laranja na imagem. Bom, acontece que o computador conseguiria sim identificar laranjas em algumas imagens, quais imagens? As mesmas que fizemos ele memorizar as laranjas. Pois e, acontece que em todo esse processo o que estavamos fazendo era fazer nosso computador decorar algumas imagem que continham uma laranja. Nao percebemos que ao inves de fazer o computador decorar, deveriamos ter investido em uma abordagem que ensinase o computador a generalizar a laranja. Ihhhhhhh, parace com nosso proprio processo de aprendizagem nao parece? Quando decoramos algo, restringimos muito os casos onde podemos aplicar um conhecimento, mas quando aprendemos, e assim entendemos como generalizar algo, nossos casos de aplicacao aumentam e muito!!!!! Com o computador nao e diferente, e necessario fazer com que ele generalize a ideia de uma laranja ao inves de decorala. Ok eu ja escrevi um bocado de coisas, ta na hora de prosseguir em como podemos fazer isso.
   </p>
 </li>
<li>
  <p align="justify">
    En <a href="https://www.python.org/">Python</a> podemos utilizar uma biblioteca chamada <a href="https://opencv.org/">OpenCV</a>(Open Computer Vision). Devemos ter python e OpenCV instalados em nossa maquina.
    </p>
</li>
 <li>
   <p>
 Apos ambos estarem instalados em nossa maquina, devemos localizar uma pasta dentro do diretorio do OpenCV
     <p align="center"><b>
openCv\opencv\build\x64\vc14\bin ou openCv\opencv\build\x64\vc15\bin
       </b></p>
      <p align="justify">
Qualquer uma dessas pastas contem executaveis que vamos utilizar depois. Para tornar nossa vida mais facil podemos adicinar um dos dois paths como uma variavel de ambiente em nosso sistema, isso vai nos poupar de ter que digitar o path completo para termos acesso aos executaveis depois.
     </p>
   </p>
</li>
<li>
  <p align="justify">
Para permitir nosso computador generlizar algum objeto, temos que escolher um objeto. Feito isso, nos precisamos buscar por variassssss... imagens desse objeto na imagem. Pense em um adulto apontando para um objeto e dizendo para uma crianca o que e aquele objeto, nos temos que agir como esse adulto, buscar por varias imagens e apontar para o nossa crianca, computador, o que elas sao. Para nao ter que ter o servico de procuar imagem por imagem na internet e levar um tempao fazendo isso, podemo buscar por data sets de determinada objeto, que sao conjuntos bem grandes de imagens contentendo aquele objeto. Esse conjunto de imagens contendo o objeto que queremos mostrar ao nosso computador e chamado de imagens positivas.
  </p>
</li>
<li>
  <p align="justify">
Com as imagens positivas em maos, ta na hora de nos como adultos ensinarmos a nossa crianca, computador, o que nao e o objeto que desejamos identificar. E para isso nos presiamos de outro data set de imagens que nao contenham o objeto que desejamos que o computador identifique, esse conjunto de imagens formam nosso conjunto de imagens negativas para identificacao.
  </p>
</li>
<li>
  <p align="justify">
Vamos voltar a falar sobre nossas imagens postivas, e bem provavel que elas nao sejam compostas somente do objeto que desejamos identificar, certo? Pois e, isso nao e um problema, mas adicina um passo em nosso processo, temos que passar por cada uma das imagens positivas e marcar a(s) ocorrencia(s) de nosso objeto. Que trabalhao! Mas para facilitar um pouco nossa vida nesse processo vamos utilizar nosso primeiro executavel do OpenCV, vamos utilizar o <a href="https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html"><b>opencv_annotation</b></a>(que esta nos diretorios comentados antes) para passar por cada uma de nossas imagens positivas(sim, da trabalho mesmo!) e marcar a(s) ocorrencia(s) de nosso objeto. O <b>opencv_annotation</b> ira criar uma anotacao, como consta no proprio nome, a anotacao ira conter o nome da imagem a(s) ocorrencia(s) do nosso objeto e posicao dele na imagem, a anotacao sera gravada em um arquivo txt.
  </p>
</li>  
<li>
  <p align="justify">
 Agora nos vamos utilizar mais um executavel do OpenCV, o <a href="https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html"<b>opencv_createsamples</b></a> para finalmente ter nossa amostra positiva! Mas espera um pouco, a gente nao tinha feito isso no ultimo paso? Qual e a diferenca? Voce pode ter notado no passo anterior que algumas imagens continha mais do que uma ocorrencia do objeto desejado. Cada ocorrencia desse objeto e chamada de amostra, <b>opencv_createsamples</b> vai ler a anotacao criada por <b>opencv_annotation</b>, e quanto chegar em uma anotacao imagem_n_9234 9(ocorrencias do objeto) nas seguintes posicoes... <b>opencv_createsamples</b> vai pegar cada uma das ocorrencias na imagem de maneira individual e entao armazenar cada uma delas, uma por uma, em uma posicao unica em um vetor que e na verdade a saida do <b>opencv_createsamples</b>. Se voce observar quando rodar o <b>opencv_createsamples</b>, possivelmente vera que o numero de amostras e maior do que numero de imagens originais, por esse motivo mesmo, ele separa cada amostra individualmente e a aloca nesse vetor.
  </p>
</li>
<li>
  <p align="justify">
Ja passamos por bastante coisa, e ate agora, nos que tivemos grande trabalho, e trabalho repetitivo nao e mesmo! Ta na hora de deixar o computador fazer a parte dele! E para isso nos vamos utilzar de nosso terceiro e ultimo executavel do OpenCV <a href="https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html"><b>opencv_traincascade</b></a>. E ali que a "magica" acontece, nos vamos passar nosso vetor originado no passo anterior alem de indicar o diretorio das imagens negativas, juntamento com alguns outros argumentos para o <b>opencv_traincascade</b> para entao finalmente deixar com que o computador comece a generalizar o nosso objeto! E e isso mesmo que que o </b>opencv_traincascade</b> faz, gera um arquivo xml contendo a generalizacao do nosso objeto(pelo menos uma generalizacao na lingua do nosso computador).Quanto maior a quantidade de dados positivos, negativos e o tempo que deixarmos o nosso computador aprendendo a generalizar o nosso objeto, melhor serao os nossos resultados.
  </p>
</li>
<li>
  <p align="justify">
So mais umas coisinhas antes de finalizar, quando percebemos que as temos que servir nosso computador de mais de mil imagens de um determinado objeto para obter um resultado mais confiavel, e facil pensarmos que ele ira memorizar essas mil ou mais imagens. Mas nao! Mesmo que servissemos nosso computador com mil, cem mil... imagens se estivessemos apenas o fazendo memorizar o conteudo, ele nunca seria capaz de identificar alguma variacao mesmo que minima das imagens. O processo feito ate agora e feito para permitir o computador generalizar imagens, para que a partir das nossas imagens servidas ele consiga identificar varias variacoes delas em outras imagems. Entao isso significa que ele vai conseguir identificar todas variacoes? Nao! Mas significa que teremos um resultado muito mais eficiente do que uma decoreba bruta.
  </p>
</li>
</ol>
<span align="center"><b>Gabriel Sordi Damo</b></span>

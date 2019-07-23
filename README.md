
HTTP requests to the NASA Kennedy Space Center WWW server

Dataset oficial: https://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html

## Requisitos:

* O teste foi criado e executado em um ambiente Windows.

* É preciso para a execução com sucesso do script armazenar os logs na pasta 'Dataset' dentro do projeto. Segue os links:
    - [NASA_access_log_Jul95.gz] ([ftp://ita.ee.lbl.gov/traces/NASA_access_log_Jul95.gz])
    - [NASA_access_log_Aug95.gz] ([ftp://ita.ee.lbl.gov/traces/NASA_access_log_Aug95.gz])
    
## Questões 1:

* Q1.1) Qual o objetivo do comando cache em Spark?
    - O comando cache persiste (armazena) em memória (default – MEMORY_ONLY) o conjuntos de dados na primeira vez que foram processados, permitindo que sejam reutilizados em outras ações com uma rapidez 10x mais rápidos.


* Q1.2) O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em MapReduce. Por quê?
    - MapReduce é mais lento que o Spark na inicializaç?o das tarefas de operaç?es de leitura de entrada e fase de map. O Spark utiliza RDD, com o uso de cache em memória e reutilizaç?o dos dados nas fases do processamento. O Spark executa processamento em memória - sem utilizaç?o de escrita e leitura em disco rígido como no MapReduce.


* Q1.3) Qual é a função do SparkContext?
    - É o principal componente do ambiente de execuç?o do Spark. O SparkContext configura serviços internos e estabelece uma conex?o com um ambiente de execuç?o do Spark. Possui métodos e funç?es para processamento de dados, criaç?o de RDD's, processamento paralelo e outros serviços Spark.


* Q1.4) Explique com suas palavras o que é Resilient Distributed Datasets (RDD).
    - É a tecnologia que tem o conceito de processamento distribuído e paralelo em cluster, com alta velocidade de processamento e tolerancia a falhas.


* Q1.5) GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê?
    - O reduceByKey trabalha com funç?o de chave única, combinando e reduzindo dados para cada chave. Sendo assim minimizando os dados trafegados em rede e tendo uma eficiencia melhor.
    - O groupByKey trabalha com chave e lista de valores, gerando troca de dados em excesso podendo gerar algumas falhas, como memória insuficiente ou disco cheio.

* Q1.6) Explique o que o código Scala abaixo faz.
```
// Abre o arquivo no caminho informado no método textFile do SparkContext
val textFile = sc.textFile("hdfs://...")______

//  Cria uma única lista com todas as palavras encontradas no texto
val counts = textFile.flatMap(line => line.split(" ")) // quebra linha por " " 
	.map(word => (word, 1)) // Avalia uma funç?o sobre cada elemento na lista
	.reduceByKey(_ + _) // processa o conteúdo do arquivo em memória

// Salva a lista em arquivo particionado, ex.: part-0000, PART-00001, ...
counts.saveAsTextFile("hdfs://...")
```

## Questões 2:

* Q2.1) Número de hosts únicos:
    - 137979

* Q2.2) O total de erros 404:
    - 20901

* Q2.3) Os 5 URLs que mais causaram erro 404:
```
/pub/winvn/readme.txt retornou: 2004 erros.
/pub/winvn/release.txt retornou: 1732 erros.
/shuttle/missions/STS-69/mission-STS-69.html retornou: 682 erros.
/shuttle/missions/sts-68/ksc-upclose.gif retornou: 426 erros.
/history/apollo/a-001/a-001-patch-small.gif retornou: 384 erros.
```

* Q2.4) Quantidade de erros 404 por dia:
```
01/Aug/1995 retornou: 243 erros.
01/Jul/1995 retornou: 316 erros.
02/Jul/1995 retornou: 291 erros.
03/Aug/1995 retornou: 304 erros.
03/Jul/1995 retornou: 474 erros.
04/Aug/1995 retornou: 346 erros.
04/Jul/1995 retornou: 359 erros.
05/Aug/1995 retornou: 236 erros.
05/Jul/1995 retornou: 497 erros.
06/Aug/1995 retornou: 373 erros.
06/Jul/1995 retornou: 640 erros.
07/Aug/1995 retornou: 537 erros.
07/Jul/1995 retornou: 570 erros.
08/Aug/1995 retornou: 391 erros.
08/Jul/1995 retornou: 302 erros.
09/Aug/1995 retornou: 279 erros.
09/Jul/1995 retornou: 348 erros.
10/Aug/1995 retornou: 315 erros.
10/Jul/1995 retornou: 398 erros.
11/Aug/1995 retornou: 263 erros.
11/Jul/1995 retornou: 471 erros.
12/Aug/1995 retornou: 196 erros.
12/Jul/1995 retornou: 471 erros.
13/Aug/1995 retornou: 216 erros.
13/Jul/1995 retornou: 532 erros.
14/Aug/1995 retornou: 287 erros.
14/Jul/1995 retornou: 413 erros.
15/Aug/1995 retornou: 327 erros.
15/Jul/1995 retornou: 254 erros.
16/Aug/1995 retornou: 259 erros.
16/Jul/1995 retornou: 257 erros.
17/Aug/1995 retornou: 271 erros.
17/Jul/1995 retornou: 406 erros.
18/Aug/1995 retornou: 256 erros.
18/Jul/1995 retornou: 465 erros.
19/Aug/1995 retornou: 209 erros.
19/Jul/1995 retornou: 639 erros.
20/Aug/1995 retornou: 312 erros.
20/Jul/1995 retornou: 428 erros.
21/Aug/1995 retornou: 305 erros.
21/Jul/1995 retornou: 334 erros.
22/Aug/1995 retornou: 288 erros.
22/Jul/1995 retornou: 192 erros.
23/Aug/1995 retornou: 345 erros.
23/Jul/1995 retornou: 233 erros.
24/Aug/1995 retornou: 420 erros.
24/Jul/1995 retornou: 328 erros.
25/Aug/1995 retornou: 415 erros.
25/Jul/1995 retornou: 461 erros.
26/Aug/1995 retornou: 366 erros.
26/Jul/1995 retornou: 336 erros.
27/Aug/1995 retornou: 370 erros.
27/Jul/1995 retornou: 336 erros.
28/Aug/1995 retornou: 410 erros.
28/Jul/1995 retornou: 94 erros.
29/Aug/1995 retornou: 420 erros.
30/Aug/1995 retornou: 571 erros.
31/Aug/1995 retornou: 526 erros.
```
* Q2.5) O total de bytes retornados:
    - 65524314915 B


## Referências
http://spark.apache.org/docs/latest/rdd-programming-guide.html#rdd-persistence
https://medium.com/@GalarnykMichael/install-spark-on-windows-pyspark-4498a5d8d66c
http://spark.apache.org/docs/2.2.2/api/java/org/apache/spark/SparkContext.html
https://spark.apache.org/docs/latest/rdd-programming-guide.html#overview
https://www.infoq.com/br/articles/mapreduce-vs-spark
https://data-flair.training/blogs/learn-apache-spark-sparkcontext/
http://etlcode.com/index.php/blog/info/Bigdata/Apache-Spark-Difference-between-reduceByKey-groupByKey-and-combineByKey

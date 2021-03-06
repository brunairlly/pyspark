#para trtansformar o arquivo em ut8
#iconv -f ISO-8859-1 -t UTF-8 exemploarquivo.csv > exemploarquivo.utf8.csv
#head exemploarquivo.utf8.csv

#lista todos os atributos e metodos de um objeto
dir(spark)

#array de tuplas
data = [("Friedrich Engels", 1820),("Margaret Heafiels", 1936),("Eliza Zamfirescu", 1887)]

#criando dataframe e nomeando o cabeçaho das colunas
df= spark.createDataFrame(data, ["name", "birth"]) or ["chave", "valor"]

#printando o schema
df.printSchema()

#exibindo o conteudo do dataframe
df.show()

#transformando arquivo em ut8 csv
iconv -f ISO-8859-1 -t UTF-8 arquivoexemplo.csv > arquivoexemplo.utf8.csv


#carregando csv
df = spark.read.load("arquivoexemplo.utf8.csv", format="csv")
df = spark.read.format("com.databricks.spark.csv").option("header", "true").option("delimiter", "\t").option("inferSchema", "true").load("arquivoexemplo.utf8.csv")


#printando o schema
df.printSchema()

#conta quantas registros
df.count()

#exibindo o conteudo do dataframe
df.show()

#exibindo primeira linha
df.show(1, truncate =False)

#exibindo primeira linha completa
df.show(1, truncate =False)


#exibindo campos
df.select("campo1", "campo2").show()

#exibindo campos completos
df.select("campo1", "campo2").show(trucante = False)




#filtrando
df.filter(df["campo"]=="exemplo1").count()


#contando somente 1 orgão certo
df.filter(df["campo"]=="exemplo2).count()

#selecionar todos os tipos registros diferentes na coluna
df.select(df["campo"]).distinct().show(100, truncate=False)

#Agrupo a quantidade
df.groupBy("campo").count().show()

#Agrupo a quantidade de maneira decrescente
df.groupBy("Nome Órgão Superior").count().orderBy("count", ascending= False).show()

#criando função para transformar virgula em  ponto
#trnsforma em float
to_value = lambda v: float( v.replace(",","."))

#testando a função
to_value("2,3")

#import para usar a udf
from pyspark.sql import functions as F

#importar para usar types
from pyspark.sql import types as t

#essa função recebe a função to_value e o tipo de retorno é float
udf_to_value = F.udf(to_value, t.FloatType())

 #transformar  o dataframe para receber esse tipo de dado
df2 =  df.withColumn("value", udf_to_value(df["exemplo3]))

#printando o schema
df2.printSchema()

#agrupando e somando os valores
df2.groupBy("exemplo4").sum("value").show()


#exibe média, valor máximo, valor minimo, desvio padrão, quantidade de entradas,
df2.describe("value").show()

#agrupa valores, pega o maior valor, soma, faz a média e conta
df2.groupBy("exemplo5").agg(F.max(df2.value), F.sum("value"), F.avg(df2.value), F.count(df2.value)).show()

#agrupa valores, pega o maior valor, soma, faz a média e conta ordenadamente, do maior para o menor
df2.groupBy("exemplo6").agg(F.max(df2.value), F.sum(df2.value), F.avg("value"), F.count(df2.value)).orderBy("sum(value)", descending=False).show(100, truncate= False)

u = df2.groupBy("exemplo7).agg(F.max(df2.value), F.sum(df2.value), F.avg("value"), F.count(df2.value)).orderBy("sum(value)", descending=False)

u.write.format("json").save("exemplodearquivo.json")

r = df5.select("campo")

r = r.withColumnRenamed("campo", "c")

r.write.format("parquet").save("exemploarquivo/r.parquet")

r.write.format("json").save("exemploarquivo/r.json")
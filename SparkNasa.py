import os

try:
    from pyspark import SparkContext, SparkConf
    from pyspark.sql import SQLContext
    from pyspark.sql.functions import regexp_extract
    from pyspark.sql.functions import col
except ImportError as e:
    os.system('pip install pyspark')


class LogAnalysis(object):
    def __init__(self):
        """Initiate."""
        self.__conf = SparkConf().setMaster('local[*]')
        self.__files = 'Dataset/*'

    def run(self) -> int:
        """Extracting the data for analysis."""
        sc = SparkContext().getOrCreate(self.__conf)
        sqlContext = SQLContext(sc)

        log = sqlContext.read.text(self.__files)

        # Extraction and mapping of data
        log_format = log.select(regexp_extract('value', r'^([^\s]+\s)', 1).alias('host'),
                                           regexp_extract('value', r'^.*\[(\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} -\d{4})]',
                                                          1).alias('timestamp'),
                                           regexp_extract('value', r'^.*"\w+\s+([^\s]+)\s+HTTP.*"', 1).alias('URL'),
                                           regexp_extract('value', r'^.*"\s+([^\s]+)', 1).cast('integer').alias(
                                               'codeHTTP'),
                                           regexp_extract('value', r'^.*\s+(\d+)$', 1).cast('integer').alias('byte'))


        # Unique hosts
        unique_host = log_format.select(log_format['host']).distinct().count()
        # Total error 404
        total_error = log_format.select(log_format['codeHTTP']).filter(log_format['codeHTTP'] == '404').count()
        # Top hosts error 404
        top_five = ''
        for u,c in log_format.filter(log_format['codeHTTP'] == '404').groupBy('URL').count(). \
                sort(col("count").desc()).limit(5).collect():
            # print(u,c)
            top_five += '{} retornou: {} erros.\n'.format(u,c)
        # Error by day
        error_day = ''
        for d, c in log_format.filter('codeHTTP = "404"').groupBy(
                log_format.timestamp.substr(1, 11).alias('day')).count().sort(
            col('day'), ascending=True).collect():
            # print(d,c)
            error_day += '{} retornou: {} erros.\n'.format(d, c)
        # Total byte
        byte = ''
        for bytes in log_format.select('byte').groupBy().sum().collect():
            for b in bytes:
                # print(b)
                byte = b

        print("1) Número de hosts únicos:\n{}\n".format(unique_host))
        print("2) O total de erros 404:\n{}\n".format(total_error))
        print("3) Os 5 URLs que mais causaram erro 404:\n{}".format(top_five))
        print("4) Quantidade de erros 404 por dia:\n{}".format(error_day))
        print("5) O total de bytes retornados:\n{} B".format(byte))

def main() -> int:
    return LogAnalysis().run()


if __name__ == '__main__':
    main()
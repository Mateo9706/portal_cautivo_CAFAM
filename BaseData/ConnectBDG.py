from google.cloud import bigquery
import os

dataset="cafamwf.cafam.portalCautivoData"
<<<<<<< Updated upstream
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './key/cafamwf-ebece760cbc0.json'#'/home/site/wwwroot/key/cafamwf-ebece760cbc0.json'
=======
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/cmb585103/Documents/GitHub/portal_cautivo_CAFAM/key/cafamwf-ebece760cbc0.json'#'/home/site/wwwroot/key/cafamwf-ebece760cbc0.json'
>>>>>>> Stashed changes
client = bigquery.Client()


def DataCaptive(valores):
	consulta = "insert into "+ dataset + "(Usuario, Email, Celular, Genero, Motivo, IP_Client, MAC_Client) values(""'"+ valores[0]+"'"",""'"+valores[1]+"'"",""'"+valores[2]	+"'"",""'"+valores[3]+"'"",""'"+valores[4]+"'"",""'"+str(valores[5])+"'"",""'"+str(valores[6])+"'"")"    
	print("Inicia Carga a Bq")
	print(consulta)
	QUERY = (consulta)
	query_job = client.query(QUERY)  # API request
	rows = query_job.result()  # Waits for query to finish
	print(rows)


#print(client)

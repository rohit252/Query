# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:34:52 2022

@author: GuptaR
"""

# -*- coding: utf-8 -*-

# import libraries

from SPARQLWrapper import SPARQLWrapper, XML, JSON, TURTLE, CSV
import requests
import time
import pandas as pd


''' query1 '''

start = time.time()


sparql = SPARQLWrapper("http://localhost:7200/repositories/Hybrid")


# sparql.setMethod(POST)

 
sparql.setQuery("""PREFIX hybrid3: <https://materials.hybrid3.duke.edu/materials/> 
PREFIX matonto: <http://matonto.org/ontology/matonto#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX sosa: <http://www.w3.org/ns/sosa/> 
PREFIX ssn: <http://www.w3.org/ns/ssn/> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rml: <http://semweb.mmlab.be/ns/rml#>
PREFIX ql: <http://semweb.mmlab.be/ns/ql#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 

SELECT ?id ?created_time

where{
    ?id a sosa:Sample;
        hybrid3:has_created ?created_time.
    
}

""")

results = sparql.query()
# print(results)
sparql.setReturnFormat(JSON)
results_query1 = sparql.query().convert()


end = time.time()

print('time taken to execute the query',end -   start)



''' storing results locally '''
query1=[]
for result in results_query1["results"]["bindings"]:
    query1.append((result["id"]["value"],result["created_time"]["value"]))
    with open('query1.txt', 'w') as f:
        for s in query1:
            f.write(str(s)[1:-1]+'\n')
    
    
    
    
# with open('query1.txt', 'w') as f:
#     for s in query1:
#         f.write(str(s)[1:-1]+'\n')   



    
        



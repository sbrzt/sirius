# Formal Competency Questions
## CQ_7.1
What are the steps that are part of the workflow for the risk assessment of the museum? What is their duration? What are the activities they were executed in?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/07/schema/>
PREFIX abox: <https://w3id.org/sirius/ontology/development/07/data/>

SELECT DISTINCT ?step ?duration_value ?activity
WHERE {
  ?workflow tbox:hasStep ?step .
  ?step tbox:hasDuration ?duration ;
    tbox:isExecutedIn ?activity .
  ?duration tbox:hasDays ?duration_value .
}
```

***

## CQ_7.2
What are the activities involved in the event executing the workflow? What are the time interval in which they respectively are executed?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/07/schema/>
PREFIX abox: <https://w3id.org/sirius/ontology/development/07/data/>

SELECT DISTINCT ?activity ?start_date ?end_date
WHERE {
    ?workflow_execution tbox:involvesActivity ?activity .
    ?activity tbox:atTime ?time_interval .
    ?time_interval tbox:hasStartDate ?start_date ;
      tbox:hasEndDate ?end_date .
}
```

***

## CQ_7.3
What does each assessment activity target? What does it assess?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/07/schema/>
PREFIX abox: <https://w3id.org/sirius/ontology/development/07/data/>

SELECT ?activity ?heritage_asset ?element
WHERE {
    ?activity tbox:targets ?heritage_asset ;
      tbox:assesses ?element .
}
```

***

## CQ_7.4
Who participated in each assessment activity? When? What did it target? What did it assess? What is it documented by?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/07/schema/>
PREFIX abox: <https://w3id.org/sirius/ontology/development/07/data/>

SELECT ?activity ?agent ?start_date ?end_date ?heritage_asset ?element ?source
WHERE {
    ?activity tbox:hasParticipant ?agent ;
      tbox:atTime ?time_interval ;
      tbox:targets ?heritage_asset ;
      tbox:assesses ?element .
    ?time_interval tbox:hasStartDate ?start_date ;
      tbox:hasEndDate ?end_date .
    OPTIONAL {
      ?activity tbox:isDocumentedBy ?source .
    }
}
```
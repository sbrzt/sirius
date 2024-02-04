# Formal Competency Questions
## CQ_7.1
What are the steps that are part of the workflow for the risk assessment of the museum? What is their duration? What are the activities they were executed in?

```SPARQL
PREFIX param: <http://www.ontologydesignpatterns.org/cp/owl/parameter.owl#>
PREFIX pwo: <http://purl.org/spar/pwo/>
PREFIX taskex: <http://www.ontologydesignpatterns.org/cp/owl/taskexecution.owl#>
PREFIX time: <http://www.w3.org/2006/time#>

SELECT DISTINCT ?step ?duration_value ?activity
WHERE {
  ?workflow pwo:hasStep ?step .
  ?step param:hasParameter ?duration ;
    taskex:isExecutedIn ?activity .
  ?duration time:days ?duration_value .
}
```

***

## CQ_7.2
What are the activities involved in the event executing the workflow? What are the time interval in which they respectively are executed?

```SPARQL
PREFIX pwo: <http://purl.org/spar/pwo/>
PREFIX tisit: <http://www.ontologydesignpatterns.org/cp/owl/timeindexedsituation.owl#>
PREFIX ti: <http://www.ontologydesignpatterns.org/cp/owl/timeinterval.owl#>

SELECT DISTINCT ?activity ?start_date ?end_date
WHERE {
    ?workflow_execution pwo:involvesActivity ?activity .
    ?activity tisit:atTime ?time_interval .
    ?time_interval ti:hasIntervalStartDate ?start_date ;
      ti:hasIntervalEndDate ?end_date .
}
```

***

## CQ_7.3
What does each assessment activity target? What does it assess?

```SPARQL
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>

SELECT ?activity ?heritage_asset ?element
WHERE {
    ?activity hero:targets ?heritage_asset ;
      hero:assesses ?element .
}
```

***

## CQ_7.4
Who participated in each assessment activity? When? What did it target? What did it assess? What is it documented by?

```SPARQL
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>
PREFIX partic: <http://www.ontologydesignpatterns.org/cp/owl/participation.owl#>
PREFIX tisit: <http://www.ontologydesignpatterns.org/cp/owl/timeindexedsituation.owl#>
PREFIX ti: <http://www.ontologydesignpatterns.org/cp/owl/timeinterval.owl#>


SELECT ?activity ?agent ?start_date ?end_date ?heritage_asset ?element ?source
WHERE {
    ?activity partic:hasParticipant ?agent ;
      tisit:atTime ?time_interval ;
      hero:targets ?heritage_asset ;
      hero:assesses ?element .
    ?time_interval ti:hasIntervalStartDate ?start_date ;
      ti:hasIntervalEndDate ?end_date .
    OPTIONAL {
      ?activity hero:isDocumentedBy ?source .
    }
}
```
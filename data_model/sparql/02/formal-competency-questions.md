# Formal Competency Questions
## CQ_2.1
Return the textual descriptions assigned to the risks, the agents of deterioration that classify them, and their types.

```SPARQL
PREFIX hero: <http://purl.org/sirius/ontology/hero/>

SELECT ?risk ?agent_of_deterioration ?risk_type ?risk_summary
WHERE {
    ?risk_assessment a hero:IdentificationDescription ;
                    hero:identifies ?risk .
    ?risk a hero:Risk ;
        hero:isClassifiedByAgent ?agent_of_deterioration ;
        hero:isClassifiedByType ?risk_type .
    OPTIONAL {
        ?risk_assessment hero:hasNote ?risk_summary .
    }
}
```

***

## CQ_2.2
Return the risks identified within the layers `site` or `region`, their types, the documents documenting them, and the start and end dates of the time intervals they have been identified in.

```SPARQL
PREFIX hero: <http://purl.org/sirius/ontology/hero/>
PREFIX ti: <http://www.ontologydesignpatterns.org/cp/owl/timeinterval.owl#>
PREFIX tis: <http://ontologydesignpatterns.org/cp/owl/timeindexedsituation.owl#>

SELECT ?risk ?risk_type ?document ?start_date ?end_date
WHERE {
    ?risk_assessment a hero:IdentificationDescription ;
                    hero:isDocumentedBy ?document ;
                    tis:atTime ?time_interval ;
                    hero:identifies ?risk .
    ?time_interval ti:hasIntervalStartDate ?start_date ;
                    ti:hasIntervalEndDate ?end_date .
    ?risk a hero:Risk ;
            hero:isClassifiedByType ?risk_type ;
            hero:isClassifiedByLayer ?layer .
    FILTER (
        ?layer = hero:site ||
        ?layer = hero:region
    )
}
```

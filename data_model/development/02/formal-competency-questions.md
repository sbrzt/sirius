# Formal Competency Questions
## CQ_2.1
What are the textual descriptions assigned to the risks, the agents of deterioration classifying them, and their types?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/02/schema/>
PREFIX abox: <https://w3id.org/sirius/ontology/development/02/data/>

SELECT ?risk ?agent_of_deterioration ?risk_type ?risk_summary
WHERE {
    ?risk_assessment a tbox:IdentificationDescription ;
                    tbox:identifies ?risk .
    ?risk a tbox:Risk ;
        tbox:isClassifiedByAgent ?agent_of_deterioration ;
        tbox:isClassifiedByType ?risk_type .
    OPTIONAL {
        ?risk_assessment tbox:hasNote ?risk_summary .
    }
}
```

***

## CQ_2.2
Which risks are identified within the "site" or "region" layers, along with their types, the documents documenting them, and the start and end dates of the time intervals in which they have been identified?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/02/schema/>
PREFIX abox: <https://w3id.org/sirius/ontology/development/02/data/>

SELECT ?risk ?risk_type ?document ?start_date ?end_date
WHERE {
    ?risk_assessment a tbox:IdentificationDescription ;
                    tbox:isDocumentedBy ?document ;
                    tbox:atTime ?time_interval ;
                    tbox:identifies ?risk .
    ?time_interval tbox:hasStartDate ?start_date ;
                    tbox:hasEndDate ?end_date .
    ?risk a tbox:Risk ;
            tbox:isClassifiedByType ?risk_type ;
            tbox:isClassifiedByLayer ?layer .
    FILTER (
        ?layer = tbox:site ||
        ?layer = tbox:region
    )
}
```

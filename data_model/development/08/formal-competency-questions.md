# Formal Competency Questions

## CQ_8.1
What are the contextual observations observing the heritage asset `:baptistery` that are part of the relative context description activity?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/07/schema/>
PREFIX : <https://w3id.org/sirius/ontology/development/07/data/>

SELECT ?observation ?note ?agent ?date ?document ?parameter ?parameter_type ?activity
WHERE {
    ?activity a tbox:AssessmentActivity ;
        tbox:hasPart ?observation .
    ?observation tbox:hasType tbox:context-observation ;
        tbox:observes :baptistery ;
        tbox:isCarriedOutBy ?agent ;
        tbox:atDate ?date ;
        tbox:usesParameter ?parameter .
    ?parameter tbox:hasType ?parameter_type .
    OPTIONAL {
        ?observation tbox:isDocumentedBy ?document ;
            tbox:hasNote ?note .
    }
}
```

## CQ_8.2
Which are the HAZARDs, the types of risk and the layers being used as parameters while observing the heritage asset `:baptistery` during the respective identification activities?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/07/schema/>
PREFIX : <https://w3id.org/sirius/ontology/development/07/data/>

SELECT ?activity ?note ?agent ?start_date ?end_date ?hazard_type ?risk_type ?layer_type
WHERE {
  ?activity a tbox:AssessmentActivity ;
            tbox:hasNote ?note ;
            tbox:isCarriedOutBy ?agent ;
            tbox:atTime [ tbox:hasStartDate ?start_date ;
                          tbox:hasEndDate ?end_date ] .
  OPTIONAL {
    ?activity tbox:hasPart [
      tbox:usesParameter [ tbox:hasType tbox:hazard-observation ;
                           tbox:hasType ?hazard_type ]
    ]
  }
  OPTIONAL {
    ?activity tbox:hasPart [
      tbox:usesParameter [ tbox:hasType tbox:risk-observation ;
                           tbox:hasType ?risk_type ]
    ]
  }
  OPTIONAL {
    ?activity tbox:hasPart [
      tbox:usesParameter [ tbox:hasType tbox:layer-observation ;
                           tbox:hasType ?layer_type ]
    ]
  }
}
```

## CQ_8.3
What are the low, probable and high estimates of the parameters observed in the measurement observations observing the heritage asset `:baptistery` during the respective analysis activities?

```SPARQL

```
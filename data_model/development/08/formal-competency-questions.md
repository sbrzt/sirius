# Formal Competency Questions

## CQ_8.1
What are the contextual observations observing the heritage asset `:baptistery` that are part of the relative context description activity?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/08/schema/>
PREFIX : <https://w3id.org/sirius/ontology/development/08/data/>

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
PREFIX tbox: <https://w3id.org/sirius/ontology/development/08/schema/>
PREFIX : <https://w3id.org/sirius/ontology/development/08/data/>

SELECT ?activity ?note ?agent ?start_date ?end_date ?hazard_type ?risk_type ?layer_type
WHERE {
  ?activity a tbox:AssessmentActivity ;
    tbox:hasNote ?note ;
    tbox:isCarriedOutBy ?agent ;
    tbox:atTime [ tbox:hasStartDate ?start_date ;
                  tbox:hasEndDate ?end_date ] ;
    tbox:hasPart [
      tbox:hasType tbox:hazard-observation ;
      tbox:usesParameter [
        tbox:hasType ?hazard_type .
      ] 
    ],
    [
      tbox:hasType tbox:risk-observation ;
      tbox:usesParameter [
        tbox:hasType ?risk_type .
      ]
    ],
    [
      tbox:hasType tbox:layer-observation ;
      tbox:usesParameter [
        tbox:hasType ?layer_type .
      ]
    ]
}
```

## CQ_8.3
What are the low, probable and high estimates of the parameters observed in the measurement observations observing the heritage asset `:baptistery` during the respective analysis activities?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/08/schema/>
PREFIX : <https://w3id.org/sirius/ontology/development/08/data/>

SELECT ?activity ?observation ?parameter_type ?low_estimate ?prob_estimate ?high_estimate
WHERE {
    ?activity a tbox:AssessmentActivity ;
      tbox:hasPart ?observation .
    ?observation tbox:hasType tbox:measurement-observation ;
      tbox:observes :baptistery ;
      tbox:usesParameter ?parameter .
    ?parameter tbox:hasType ?parameter_type ;
      tbox:hasLowEstimate ?low_estimate ;
      tbox:hasProbableEstimate ?prob_estimate ;
      tbox:hasHighEstimate ?high_estimate .
}
```

## CQ_8.4
What are the PRIORITY levels and ACCEPTANCE levels used as parameters while observing the heritage asset `:baptistery` during the respective evaluation activities?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/08/schema/>
PREFIX : <https://w3id.org/sirius/ontology/development/08/data/>

SELECT ?activity ?note ?priority_level ?acceptance_level
WHERE {
?activity a tbox:AssessmentActivity ;
             tbox:hasType tbox:risk-evaluation ;
             tbox:hasNote ?note ;
             tbox:hasPart [
                 tbox:hasType tbox:priority-observation ;
                 tbox:observes :baptistery ;
                 tbox:usesParameter [ tbox:hasType ?priority_level ]
             ] ,
             [
                 tbox:hasType tbox:acceptance-observation ;
                 tbox:observes :baptistery ;
                 tbox:usesParameter [ tbox:hasType ?acceptance_level ]
             ] .
}
```

## CQ_8.5
What are the control stages, layers and costs used as parameters while observing the heritage asset `:baptistery` during the respective treatment activities?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/08/schema/>
PREFIX : <https://w3id.org/sirius/ontology/development/08/data/>

SELECT ?activity ?note ?control_stage ?layer ?capital_cost ?maintenance_cost
WHERE {
?activity a tbox:AssessmentActivity ;
             tbox:hasType tbox:risk-treatment ;
             tbox:hasNote ?note ;
             tbox:hasPart [
                 tbox:hasType tbox:control-observation ;
                 tbox:observes :baptistery ;
                 tbox:usesParameter [ tbox:hasType ?control_stage ]
             ] ,
             [
                 tbox:hasType tbox:layer-observation ;
                 tbox:observes :baptistery ;
                 tbox:usesParameter [ tbox:hasType ?layer ]
             ] .

OPTIONAL {
  ?activity tbox:hasPart [
                 tbox:hasType tbox:cost-observation ;
                 tbox:observes :baptistery ;
                 tbox:usesParameter [ tbox:hasType ?capital_cost ]
             ] ,
             [
                 tbox:hasType tbox:cost-observation ;
                 tbox:observes :baptistery ;
                 tbox:usesParameter [ tbox:hasType ?maintenance_cost ]
             ] .
}
}
```
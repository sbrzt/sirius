# Formal Competency Questions

## CQ_8.1
What are the statements assigned to the CHO `:baptistery` that are part of the assessment activity describing its context?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/08/schema/>
PREFIX : <https://w3id.org/sirius/ontology/development/08/data/>

SELECT ?statement ?note ?agent ?document ?concept ?concept_type ?activity
WHERE {
    ?activity a tbox:AssessmentActivity ;
        tbox:hasType tbox:context-description ; 
        tbox:assigns ?statement ;
        tbox:assignsTo :baptistery ;
        tbox:isCarriedOutBy ?agent .
    ?statement tbox:hasContent ?note ;
        tbox:refersTo ?concept .
    ?concept tbox:hasType ?concept_type .
    OPTIONAL {
        ?statement tbox:isDocumentedBy ?document .
    }
}
```

## CQ_8.2
Which are the hazards, the types of risk occurence and the risk locations referred to by statements assigned to the CHO `:baptistery` by identification activities?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/08/schema/>
PREFIX : <https://w3id.org/sirius/ontology/development/08/data/>

SELECT ?activity ?agent ?start_date ?end_date ?hazard_type ?occurrence_type ?location_type
WHERE {
  ?activity a tbox:AssessmentActivity ;
    tbox:isCarriedOutBy ?agent ;
    tbox:hasType tbox:risk-identification ;
    tbox:atTime [ tbox:hasStartTime ?start_date ;
                  tbox:hasEndTime ?end_date ] ;
    tbox:assigns ?statement_1 ,
      ?statement_2 ,
      ?statement_3 .
  ?statement_1 tbox:hasType tbox:condition-description ;
    tbox:refersTo [
        tbox:hasType ?hazard_type 
      ] .
  ?statement_2 tbox:hasType tbox:dimensions-description ;
      tbox:refersTo [
        tbox:hasType ?occurrence_type 
      ] .
  ?statement_3 tbox:hasType tbox:location-description ;
      tbox:refersTo [
        tbox:hasType ?location_type 
      ] .
}
```

## CQ_8.3
What are the low, probable and high estimates of the measures that are referred to by statements assigned to the CHO `:baptistery` by analysis activities?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/08/schema/>
PREFIX : <https://w3id.org/sirius/ontology/development/08/data/>

SELECT ?activity ?statement ?type ?low_estimate_value ?prob_estimate_value ?high_estimate_value
WHERE {
  ?activity a tbox:AssessmentActivity ;
    tbox:hasType tbox:risk-analysis ;
    tbox:assignsTo :baptistery ;
    tbox:assigns ?statement .
  ?statement tbox:hasType tbox:dimensions-description ;
    tbox:refersTo ?concept .
  ?concept tbox:hasType ?type ;
    tbox:isComposedOf ?low_estimate ,
      ?prob_estimate , 
      ?high_estimate .
  ?low_estimate tbox:hasType tbox:low-estimate ;
    tbox:hasValue ?low_estimate_value .
  ?prob_estimate tbox:hasType tbox:probable-estimate ;
    tbox:hasValue ?prob_estimate_value .
  ?high_estimate tbox:hasType tbox:high-estimate ;
    tbox:hasValue ?high_estimate_value .
}
```

## CQ_8.4
What are the priority levels referred to by statements assigned to the CHO `:baptistery` by evaluation activities?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/08/schema/>
PREFIX : <https://w3id.org/sirius/ontology/development/08/data/>

SELECT ?activity ?note ?priority_level
WHERE {
?activity a tbox:AssessmentActivity ;
  tbox:hasType tbox:risk-evaluation ;
  tbox:hasNote ?note ;
  tbox:assignsTo :baptistery ;
  tbox:assigns [
      tbox:hasType tbox:diagnosis ;
      tbox:refersTo [ 
        tbox:hasType ?priority_level 
      ]
  ]
}
```

## CQ_8.5
What are the treatment actions, capital costs and maintenance costs being referred to by the statements assigned to the CHO `:baptistery` by treatment activities?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/08/schema/>
PREFIX : <https://w3id.org/sirius/ontology/development/08/data/>

SELECT ?activity ?note ?action ?capital_cost_value ?maintenance_cost_value
WHERE {
?activity a tbox:AssessmentActivity ;
  tbox:hasType tbox:risk-treatment ;
  tbox:hasNote ?note ;
  tbox:assignsTo :baptistery ;
  tbox:assigns ?statement_1 ,
    ?statement_2 ,
    ?statement_3 .
?statement_1 tbox:hasType tbox:plan ;
  tbox:refersTo ?concept_1 .
?concept_1 tbox:hasType ?action .
?statement_2 tbox:hasType tbox:budget ;
  tbox:refersTo ?capital_cost .
?capital_cost tbox:hasType tbox:capital-cost ;
    tbox:hasValue ?capital_cost_value .
?statement_3 tbox:hasType tbox:budget ;
  tbox:refersTo ?maintenance_cost .
?maintenance_cost tbox:hasType tbox:maintenance-cost ;
    tbox:hasValue ?maintenance_cost_value .
}
```
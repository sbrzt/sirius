# Formal Competency Questions

## CQ_8.1
What are the statements assigned to a CHO that are part of the assessment activity describing its context?

```SPARQL
PREFIX : <https://w3id.org/sirius/ontology/data/08/>
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>
PREFIX ti: <http://www.ontologydesignpatterns.org/cp/owl/timeinterval.owl#>
PREFIX wd: <http://www.wikidata.org/entity/>

SELECT ?statement ?note ?document ?concept ?concept_type ?activity ?agent ?place ?start_date ?end_date
WHERE {
    ?activity a hero:Activity ;
        hero:hasType wd:Q1137655 ; 
        hero:assigns ?statement ;
        hero:hasTimeInterval [ ti:hasIntervalStartDate ?start_date ;
            ti:hasIntervalEndDate ?end_date ] ;
        hero:hasLocation ?place ;
        hero:isCarriedOutBy ?agent .
    ?statement hero:hasContent ?note ;
        hero:refersTo ?concept .
    ?concept hero:hasType ?concept_type .
    OPTIONAL {
        ?statement hero:isDocumentedBy ?document .
    }
}
```

## CQ_8.2
Which are the hazards, the types of risk occurence and the risk locations referred to by statements assigned to a CHO by identification activities?

```SPARQL
PREFIX : <https://w3id.org/sirius/ontology/data/08/>
PREFIX aat: <http://vocab.getty.edu/page/aat/>
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>
PREFIX ti: <http://www.ontologydesignpatterns.org/cp/owl/timeinterval.owl#>
PREFIX wd: <http://www.wikidata.org/entity/>

SELECT ?activity ?hazard_type ?occurrence_type ?location_type ?agent ?place ?start_date ?end_date
WHERE {
  ?activity a hero:Activity ;
    hero:isCarriedOutBy ?agent ;
    hero:hasType wd:Q5687675 ;
    hero:hasTimeInterval [ ti:hasIntervalStartDate ?start_date ;
      ti:hasIntervalEndDate ?end_date ] ;
    hero:hasLocation ?place ;
    hero:assigns ?statement_1 ,
      ?statement_2 ,
      ?statement_3 .
  ?statement_1 hero:hasType aat:300435425 ;
    hero:refersTo [
        hero:hasType ?hazard_type 
      ] .
  ?statement_2 hero:hasType aat:300435430 ;
      hero:refersTo [
        hero:hasType ?occurrence_type 
      ] .
  ?statement_3 hero:hasType aat:300435449 ;
      hero:refersTo [
        hero:hasType ?location_type 
      ] .
}
```

## CQ_8.3
What are the low, probable and high estimates of the measures that are referred to by statements assigned to a CHO by analysis activities?

```SPARQL
PREFIX : <https://w3id.org/sirius/ontology/data/08/>
PREFIX aat: <http://vocab.getty.edu/page/aat/>
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>
PREFIX ti: <http://www.ontologydesignpatterns.org/cp/owl/timeinterval.owl#>
PREFIX wd: <http://www.wikidata.org/entity/>

SELECT DISTINCT ?activity ?statement ?type ?low_estimate_value ?prob_estimate_value ?high_estimate_value ?agent ?place ?start_date ?end_date
WHERE {
  ?activity a hero:Activity ;
    hero:hasType wd:Q217602 ;
    hero:isCarriedOutBy ?agent ;
    hero:hasTimeInterval [ ti:hasIntervalStartDate ?start_date ;
      ti:hasIntervalEndDate ?end_date ] ;
    hero:hasLocation ?place ;
    hero:assigns ?statement .
  ?statement hero:hasType aat:300435430 ;
    hero:refersTo ?concept .
  ?concept hero:hasType ?type ;
    hero:hasComponent ?low_estimate ,
      ?prob_estimate , 
      ?high_estimate .
  ?low_estimate hero:hasType wd:Q10585806 ;
    hero:hasContent ?low_estimate_value .
  ?prob_estimate hero:hasType wd:Q226995 ;
    hero:hasContent ?prob_estimate_value .
  ?high_estimate hero:hasType wd:Q10578722 ;
    hero:hasContent ?high_estimate_value .
}
```

## CQ_8.4
What are the priority levels referred to by statements assigned to a CHO by evaluation activities?

```SPARQL
PREFIX : <https://w3id.org/sirius/ontology/data/08/>
PREFIX aat: <http://vocab.getty.edu/page/aat/>
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>
PREFIX ti: <http://www.ontologydesignpatterns.org/cp/owl/timeinterval.owl#>
PREFIX wd: <http://www.wikidata.org/entity/>

SELECT ?activity ?note ?priority_level ?agent ?place ?start_date ?end_date
WHERE {
?activity a hero:Activity ;
  hero:hasType wd:Q1379672 ;
  hero:hasNote ?note ;
  hero:isCarriedOutBy ?agent ;
  hero:hasTimeInterval [ ti:hasIntervalStartDate ?start_date ;
      ti:hasIntervalEndDate ?end_date ] ;
  hero:hasLocation ?place ;
  hero:assigns [
      hero:hasType aat:300438433 ;
      hero:refersTo [ 
        hero:hasType ?priority_level 
      ]
  ]
}
```

## CQ_8.5
What are the treatment actions, capital costs and maintenance costs being referred to by the statements assigned to a CHO by treatment activities?

```SPARQL
PREFIX : <https://w3id.org/sirius/ontology/data/08/>
PREFIX aat: <http://vocab.getty.edu/page/aat/>
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>
PREFIX ti: <http://www.ontologydesignpatterns.org/cp/owl/timeinterval.owl#>
PREFIX wd: <http://www.wikidata.org/entity/>

SELECT DISTINCT ?activity ?note ?action ?capital_cost_value ?maintenance_cost_value ?agent ?place ?start_date ?end_date
WHERE {
  ?activity a hero:Activity ;
    hero:hasType wd:Q2251595 ;
    hero:hasNote ?note ;
    hero:isCarriedOutBy ?agent ;
    hero:hasTimeInterval [ ti:hasIntervalStartDate ?start_date ;
      ti:hasIntervalEndDate ?end_date ] ;
    hero:hasLocation ?place ;
    hero:assigns ?statement_1 ,
      ?statement_2 ,
      ?statement_3 .
  ?statement_1 hero:hasType wd:Q1371819 ;
    hero:refersTo ?concept_1 .
  ?concept_1 hero:hasType ?action .
  ?statement_2 hero:hasType aat:300027514 ;
    hero:refersTo ?capital_cost .
  ?capital_cost hero:hasType wd:Q302208 ;
    hero:hasContent ?capital_cost_value .
  ?statement_3 hero:hasType aat:300027514 ;
    hero:refersTo ?maintenance_cost .
  ?maintenance_cost hero:hasType wd:Q831940 ;
    hero:hasContent ?maintenance_cost_value .
}
```
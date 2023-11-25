# Formal Competency Questions
## CQ_3.1
Return all the risks with type "Cumulative process", the asset they are assiged to, the layers they exist within, and the documents that document them.

```SPARQL
PREFIX hero: <http://purl.org/sirius/ontology/hero/>

SELECT ?risk ?asset ?layer ?document
WHERE {
  ?risk_assessment a hero:RiskAssessment ;
                  hero:assignsRisk ?risk ;
                  hero:assignsRiskTo ?asset .
  ?risk hero:withType hero:cumulative ;
        hero:withinLayer ?layer ;
        hero:isDocumentedBy ?document .
}
```

***

## CQ_3.2
Return all the risks existing with the layers "Region" or "Site", the asset they are assiged to, their type, and the start and end dates of the time intervals they exist in.

```SPARQL
PREFIX hero: <http://purl.org/sirius/ontology/hero/>
PREFIX ti: <http://www.ontologydesignpatterns.org/cp/owl/timeinterval.owl#>
PREFIX tvc: <http://www.essepuntato.it/2012/04/tvc/>

SELECT ?risk ?asset ?type ?time_interval_start ?time_interval_end
WHERE {
    ?risk_assessment a hero:RiskAssessment ;
                    hero:assignsRisk ?risk ;
                    hero:assignsRiskTo ?asset .
    ?risk hero:withType ?type ;
          hero:withinLayer ?layer ;
          tvc:atTime ?time_interval .
    ?time_interval ti:hasIntervalStartDate ?time_interval_start ;
                  ti:hasIntervalEndDate ?time_interval_end . 
    FILTER ( ?layer = hero:region || ?layer = hero:site )
}
```

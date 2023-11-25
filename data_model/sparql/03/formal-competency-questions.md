# Formal Competency Questions
## CQ_3.1
Return all the risks with type "Cumulative process", the asset they are assiged to, the layers they exist within, and the documents that document them.

```SPARQL
PREFIX abox: <http://purl.org/sirius/ontology/development/03/data/>
PREFIX tbox: <http://purl.org/sirius/ontology/development/03/schema/>

SELECT ?risk ?asset ?layer ?document
WHERE {
  ?risk_assessment a tbox:RiskAssessment ;
                  tbox:assignsRisk ?risk ;
                  tbox:assignsRiskTo ?asset .
  ?risk tbox:withType tbox:cumulative ;
        tbox:withinLayer ?layer ;
        tbox:isDocumentedBy ?document .
}
```

***

## CQ_3.2
Return all the risks existing with the layers "Region" or "Site", the asset they are assiged to, their type, and the start and end dates of the time intervals they exist in.

```SPARQL
PREFIX abox: <http://purl.org/sirius/ontology/development/03/data/>
PREFIX tbox: <http://purl.org/sirius/ontology/development/03/schema/>

SELECT ?risk ?asset ?type ?time_interval_start ?time_interval_end
WHERE {
    ?risk_assessment a tbox:RiskAssessment ;
                    tbox:assignsRisk ?risk ;
                    tbox:assignsRiskTo ?asset .
    ?risk tbox:withType ?type ;
          tbox:withinLayer ?layer ;
          tbox:atTime ?time_interval .
    ?time_interval tbox:hasStartDate ?time_interval_start ;
                  tbox:hasEndDate ?time_interval_end . 
    FILTER ( ?layer = tbox:region || ?layer = tbox:site )
}
```

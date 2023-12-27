# Formal Competency Questions
## CQ_3.1
What are the probable estimates of the A-score, B-score, and C-score for each risk affecting each heritage asset, along with the documentation and textual content that record them?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/03/schema/>
PREFIX abox: <https://w3id.org/sirius/ontology/development/03/data/>

SELECT ?risk ?heritage_asset ?risk_component ?probable_estimate ?note ?knowledge_source
WHERE {
  ?risk_assessment tbox:describes ?heritage_asset ;
                    tbox:analyses ?risk ;
                    tbox:quantifies ?risk_component .
  ?risk_component a ?component_class ;
                  tbox:hasProbableEstimate ?probable_estimate ;
                  tbox:hasNote ?note .
  OPTIONAL {
    ?risk_component tbox:isDocumentedBy ?knowledge_source ;
  }
  FILTER (
    ?component_class = tbox:Frequency ||
    ?component_class = tbox:FractionalValueLoss ||
    ?component_class = tbox:Exposure 
  )
}
```

***

## CQ_3.2
What are the low, probable, and high estimates of the magnitudes of risk for each risk associated with each heritage asset?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/03/schema/>
PREFIX abox: <https://w3id.org/sirius/ontology/development/03/data/>

SELECT ?risk ?heritage_asset ?low_estimate ?probable_estimate ?high_estimate
WHERE {
  ?risk_assessment tbox:describes ?heritage_asset ;
                    tbox:analyses ?risk ;
                    tbox:quantifies ?risk_magnitude .
  ?risk_magnitude a tbox:Magnitude ;
                  tbox:hasLowEstimate ?low_estimate ;
                  tbox:hasProbableEstimate ?probable_estimate ;
                  tbox:hasHighEstimate ?high_estimate .
}
```
***

## CQ_3.3
What are the low, probable, and high estimates of the A-score, B-score, C-score, and magnitude of risk for each risk affecting each heritage asset?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/03/schema/>
PREFIX abox: <https://w3id.org/sirius/ontology/development/03/data/>

SELECT ?risk ?component_class ?low_estimate ?probable_estimate ?high_estimate ?knowledge_source ?note
WHERE {
  ?risk_assessment tbox:describes ?heritage_asset ;
                    tbox:analyses ?risk ;
                    tbox:quantifies ?risk_component .
  ?risk_component a ?component_class ;
                  tbox:hasLowEstimate ?low_estimate ;
                  tbox:hasHighEstimate ?high_estimate ;
                  tbox:hasProbableEstimate ?probable_estimate .
  FILTER (
    ?component_class = tbox:Frequency ||
    ?component_class = tbox:FractionalValueLoss ||
    ?component_class = tbox:Exposure ||
    ?component_class = tbox:Magnitude
  )
}
```
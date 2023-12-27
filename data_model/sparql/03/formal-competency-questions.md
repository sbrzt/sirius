# Formal Competency Questions
## CQ_3.1
What are the probable estimates of the A-score, B-score, and C-score for each risk affecting each heritage asset, and the documents and textual notes recording them?

```SPARQL
PREFIX : <https://w3id.org/sirius/ontology/data/03/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>

SELECT ?risk ?heritage_asset ?risk_component ?probable_estimate ?note ?knowledge_source
WHERE {
  ?risk_assessment hero:describes ?heritage_asset ;
                    hero:analyses ?risk ;
                    hero:quantifies ?risk_component . 
  ?risk_component a ?component_class ;
                  hero:hasProbableEstimate ?probable_estimate .
  OPTIONAL {
    ?risk_component hero:isDocumentedBy ?knowledge_source ;
                  hero:hasNote ?note .
  }
  FILTER (
    ?component_class = hero:Frequency ||
    ?component_class = hero:FractionalValueLoss ||
    ?component_class = hero:Exposure 
  )
}
```

***

## CQ_3.2
What are the low, probable, and high estimates of the magnitudes of risk for each risk associated with each heritage asset?

```SPARQL
PREFIX : <https://w3id.org/sirius/ontology/data/03/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>

SELECT ?risk ?heritage_asset ?low_estimate ?probable_estimate ?high_estimate
WHERE {
  ?risk_assessment hero:describes ?heritage_asset ;
                    hero:analyses ?risk ;
                    hero:quantifies ?risk_magnitude .
  ?risk_magnitude a hero:Magnitude ;
                  hero:hasLowEstimate ?low_estimate ;
                  hero:hasProbableEstimate ?probable_estimate ;
                  hero:hasHighEstimate ?high_estimate .
}
```
***

## CQ_3.3
What are the low, probable, and high estimates of the A-score, B-score, C-score, and magnitude of risk for each risk affecting each heritage asset?

```SPARQL
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>

SELECT ?risk ?component_class ?low_estimate ?probable_estimate ?high_estimate ?knowledge_source ?note
WHERE {
  ?risk_assessment hero:describes ?heritage_asset ;
                    hero:analyses ?risk ;
                    hero:quantifies ?risk_component .
  ?risk_component a ?component_class ;
                  hero:hasLowEstimate ?low_estimate ;
                  hero:hasHighEstimate ?high_estimate ;
                  hero:hasProbableEstimate ?probable_estimate .
  FILTER (
    ?component_class = hero:Frequency ||
    ?component_class = hero:FractionalValueLoss ||
    ?component_class = hero:Exposure ||
    ?component_class = hero:Magnitude
  )
}
```
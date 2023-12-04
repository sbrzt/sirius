# Formal Competency Questions
## CQ_3.1
Return the probable estimate of the A-score, B-score, C-score for each risk affecting each heritage asset, as well as the sources of knowledge that witness them.

```SPARQL
PREFIX : <http://purl.org/sirius/ontology/data/03/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX hero: <http://purl.org/sirius/ontology/hero/>

SELECT ?risk ?heritage_asset ?risk_component ?probable_estimate ?note ?knowledge_source
WHERE {
  ?risk_assessment hero:describes ?heritage_asset ;
                    hero:analyses ?risk ;
                    hero:quantifies ?risk_component . 
  ?risk_component a ?component_class ;
                  hero:hasProbableEstimate ?probable_estimate ;
                  hero:hasNote ?note .
  OPTIONAL {
    ?risk_component hero:isDocumentedBy ?knowledge_source ;
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
Return the low, probable, and high estimates of the magnitudes of risk for each risk of each heritage asset.

```SPARQL
PREFIX : <http://purl.org/sirius/ontology/data/03/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX hero: <http://purl.org/sirius/ontology/hero/>

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
Return the low, probable, and high estimates of the A-score, B-score, C-score, and magnitude of risk for each risk affecting each heritage asset, as well as their documentation.

```SPARQL
PREFIX hero: <http://purl.org/sirius/ontology/hero/>

SELECT ?risk ?component_class ?low_estimate ?probable_estimate ?high_estimate ?knowledge_source ?note
WHERE {
  ?risk_assessment hero:describes ?heritage_asset ;
                    hero:analyses ?risk ;
                    hero:quantifies ?risk_component .
  ?risk_component a ?component_class ;
                  hero:hasLowEstimate ?low_estimate ;
                  hero:hasHighEstimate ?high_estimate ;
                  hero:hasProbableEstimate ?probable_estimate .
  OPTIONAL {?risk_component hero:isDocumentedBy ?knowledge_source .}
  OPTIONAL {?risk_component hero:hasNote ?note .}
  FILTER (
    ?component_class = hero:Frequency ||
    ?component_class = hero:FractionalValueLoss ||
    ?component_class = hero:Exposure ||
    ?component_class = hero:Magnitude
  )
}
```
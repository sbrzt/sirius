# Formal Competency Questions
## CQ_4.1
Return the probable estimate of the A-score, B-score, C-score for each risk affecting each heritage asset, as well as the sources of knowledge that witness them.

```SPARQL
PREFIX : <http://purl.org/sirius/ontology/data/04/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX hero: <http://purl.org/sirius/ontology/hero/>

SELECT ?risk ?heritage_asset ?risk_component ?probable_estimate ?note ?knowledge_source
WHERE {
  ?risk_assessment hero:assignsRiskTo ?heritage_asset ;
                    hero:assignsRisk ?risk .
  ?risk hero:withComponent ?risk_component .
  ?risk_component hero:hasProbableEstimate ?probable_estimate ;
                  hero:hasNote ?note .
  OPTIONAL {
    ?risk_component hero:isDocumentedBy ?knowledge_source ;
  }
}
```

***

## CQ_4.2
Return the low, probable, and high estimates of the magnitudes of risk for each risk of each heritage asset.

```SPARQL
PREFIX : <http://purl.org/sirius/ontology/data/04/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX hero: <http://purl.org/sirius/ontology/hero/>

SELECT ?risk ?heritage_asset ?low_estimate ?probable_estimate ?high_estimate
WHERE {
  ?risk_assessment hero:assignsRiskTo ?heritage_asset ;
                    hero:assignsRisk ?risk .
  ?risk hero:withMagnitude ?risk_magnitude .
  ?risk_magnitude hero:hasLowEstimate ?low_estimate ;
                  hero:hasProbableEstimate ?probable_estimate ;
                  hero:hasHighEstimate ?high_estimate .
}
```

***

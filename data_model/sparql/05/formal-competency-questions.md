# Formal Competency Questions
## CQ_5.1
Return the assets that are part of the `house` asset and the asset percentage they represent, in descending order.

```SPARQL
PREFIX : <http://purl.org/sirius/ontology/data/05/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX hero: <http://purl.org/sirius/ontology/hero/>

SELECT ?asset ?asset_part ?percentage
WHERE {
  ?asset a crm:E24_Physical_Human-Made_Thing ;
        crm:P46_is_composed_of ?asset_part .
  ?asset_part hero:representsAssetPercentage ?percentage .
}
```

***

## CQ_5.2
Return the assets that are part of the `house` asset and the contributing values assigned to them, along with their score, dimension, aspect, note, documentation, and time interval.

```SPARQL
PREFIX : <http://purl.org/sirius/ontology/data/05/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX hero: <http://purl.org/sirius/ontology/hero/>
PREFIX ti: <http://www.ontologydesignpatterns.org/cp/owl/timeinterval.owl#>
PREFIX tvc: <http://www.essepuntato.it/2012/04/tvc/>

SELECT DISTINCT ?asset_part ?value ?score ?dimension ?aspect ?note ?document ?time_interval_start ?time_interval_end
WHERE {
    ?asset a crm:E24_Physical_Human-Made_Thing ;
            crm:P46_is_composed_of ?asset_part .
    ?value_assessment hero:assignsValueTo ?asset_part ;
                        hero:assignsValue ?value .
    ?value hero:hasScore ?score ;
            hero:withDimension ?dimension ;
            hero:withinAspect ?aspect ;
            hero:hasNote ?note ;
            hero:isDocumentedBy ?document ;
            tvc:atTime ?time_interval .
    ?time_interval ti:hasIntervalStartDate ?time_interval_start ;
                    ti:hasIntervalEndDate ?time_interval_end .
}
```

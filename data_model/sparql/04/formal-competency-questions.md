# Formal Competency Questions
## CQ_4.1
Which assets are part of the house asset, and what is the percentage each asset represents, ordered in descending order?

```SPARQL
PREFIX : <https://w3id.org/sirius/ontology/data/04/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>

SELECT DISTINCT ?asset ?asset_part ?percentage
WHERE {
  ?asset a crm:E24_Physical_Human-Made_Thing ;
        crm:P46_is_composed_of ?asset_part .
  ?value_assessment hero:describes ?asset_part ;
                    hero:assessesPercentage ?percentage .
}
```

***

## CQ_4.2
What are the contributing values assigned to an asset, and what is their associated score, dimension, aspect, note, documentation, and time interval?

```SPARQL
PREFIX : <https://w3id.org/sirius/ontology/data/04/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>
PREFIX ti: <http://www.ontologydesignpatterns.org/cp/owl/timeinterval.owl#>
PREFIX tis: <http://ontologydesignpatterns.org/cp/owl/timeindexedsituation.owl#>

SELECT DISTINCT ?asset_part ?value ?score ?dimension ?aspect ?note ?document ?time_interval_start ?time_interval_end
WHERE {
    ?asset a crm:E24_Physical_Human-Made_Thing ;
            crm:P46_is_composed_of ?asset_part .
    ?value_assessment hero:describes ?asset_part ;
                        hero:assigns ?value ;
            hero:withinDimension ?dimension ;
            hero:withinAspect ?aspect ;
            hero:hasNote ?note ;
            hero:isDocumentedBy ?document ;
            tis:atTime ?time_interval .
    ?value hero:hasScore ?score .
    ?time_interval ti:hasIntervalStartDate ?time_interval_start ;
                    ti:hasIntervalEndDate ?time_interval_end .
}
```

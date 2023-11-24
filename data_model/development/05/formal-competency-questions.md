# Formal Competency Questions
## CQ_5.1
Return the assets that are part of the `house` asset and the asset percentage they represent, in descending order.

```SPARQL
PREFIX tbox: <http://purl.org/sirius/ontology/development/05/schema/>
PREFIX abox: <http://purl.org/sirius/ontology/development/05/data/>

SELECT ?asset ?asset_part ?percentage
WHERE {
  ?asset a tbox:HeritageAsset ;
        tbox:hasPart ?asset_part .
  ?asset_part tbox:representsAssetPercentage ?percentage .
}
```

***

## CQ_5.2
Return the assets that are part of the `house` asset and the contributing values assigned to them, along with their score, dimension, aspect, note, documentation, and time interval.

```SPARQL
PREFIX tbox: <http://purl.org/sirius/ontology/development/05/schema/>
PREFIX abox: <http://purl.org/sirius/ontology/development/05/data/>

SELECT DISTINCT ?asset_part ?value ?score ?dimension ?aspect ?note ?document ?time_interval_start ?time_interval_end
WHERE {
    ?asset a tbox:HeritageAsset ;
            tbox:hasPart ?asset_part .
    ?value_assessment tbox:assignsValueTo ?asset_part ;
                        tbox:assignsValue ?value .
    ?value tbox:hasScore ?score ;
            tbox:withDimension ?dimension ;
            tbox:withinAspect ?aspect ;
            tbox:hasNote ?note ;
            tbox:isDocumentedBy ?document ;
            tbox:atTime ?time_interval .
    ?time_interval tbox:hasStartDate ?time_interval_start ;
                    tbox:hasEndDate ?time_interval_end .
}
```

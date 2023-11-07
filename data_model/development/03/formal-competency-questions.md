# Formal Competency Questions
## CQ_3.1
Return the total number of items in "Battistero degli Ariani", the assets it is composed of, the number of items in each asset, the percentage of total value for each asset, the percentage of total value per item for each asset.

```SPARQL
PREFIX tbox: <http://purl.org/sirius/ontology/development/03/schema/>
PREFIX abox: <http://purl.org/sirius/ontology/development/03/data/>

SELECT ?asset_part ?quantity ?perc_per_part ?perc_per_item ?total_items
WHERE {
  ?asset a tbox:HeritageAsset ;
         tbox:hasPart ?asset_part .
  ?value_assessment tbox:assignsValueTo ?asset_part ;
                   tbox:hasQuantity ?quantity ;
                   tbox:hasPercentageOfValue ?perc_per_part .
  BIND(?perc_per_part / ?quantity AS ?perc_per_item)

  {
    SELECT ?asset_part (SUM(?quantity) AS ?total_items)
    WHERE {
      ?asset a tbox:HeritageAsset ;
             tbox:hasPart ?asset_part .
      ?value_assessment tbox:assignsValueTo ?asset_part ;
                       tbox:hasQuantity ?quantity .
    }
    GROUP BY ?asset_part
  }
}
```

***

## CQ_3.2
Return the assets which have been assigned "Artistic" contributing values and risks which exist at the "building" layer of enclosure.

```SPARQL
PREFIX tbox: <http://purl.org/sirius/ontology/development/03/schema/>
PREFIX abox: <http://purl.org/sirius/ontology/development/03/data/>

SELECT DISTINCT ?asset_part ?perc_value
WHERE {
    ?asset a tbox:HeritageAsset ;
            tbox:hasPart ?asset_part .
    ?value_assessment tbox:assignsValueTo ?asset_part ;
                        tbox:assignsValue ?value ;
                        tbox:hasPercentageOfValue ?perc_value .
    ?value tbox:hasContributingValueType tbox:artistic .
    ?risk_assessment tbox:assignsRiskTo ?asset ;
                        tbox:assignsRisk ?risk .
    ?risk tbox:existsWithin tbox:building .
}
```

***

## CQ_3.3
Return all the contributing values assigned to the assets that constitute the asset "Battistero degli Ariani". For each value, return its type,  definition, weight, note, and degree of occurrence.

```SPARQL
PREFIX tbox: <http://purl.org/sirius/ontology/development/03/schema/>
PREFIX abox: <http://purl.org/sirius/ontology/development/03/data/>

SELECT ?asset ?value_type ?definition ?note ?weight ?occurrence
WHERE {
    abox:battistero-degli-ariani tbox:hasPart ?asset .
    ?value_assessment tbox:assignsValueTo ?asset ;
                        tbox:assignsValue ?value .
    ?value tbox:hasContributingValueType ?value_type ;
            tbox:hasWeight ?weight ;
            tbox:hasDefinition ?definition ;
            tbox:hasDegreeOfOccurrence ?occurrence .
    OPTIONAL {
        ?value tbox:hasNote ?note ;
    }
}
```

# Formal Competency Questions
## CQ_3.1
Return the total number of items in "Battistero degli Ariani", the assets it is composed of, the number of items in each asset, the percentage of total value for each asset, the percentage of total value per item for each asset.

```SPARQL
PREFIX : <http://purl.org/sirius/ontology/03/data/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX hero: <http://purl.org/sirius/ontology/hero/>

SELECT ?asset_part ?quantity ?perc_per_part ?perc_per_item ?total_items
WHERE {
  ?asset a crm:E24_Physical_Human-Made_Thing ;
         crm:P46_is_composed_of ?asset_part .
  ?value_assessment hero:assignsValueTo ?asset_part ;
                    hero:assignsValue ?value ;
                    hero:ratesItemQuantity ?quantity ;
                    hero:ratesOccurrenceDegree ?occurrence .
  ?value hero:hasRelativeWeight ?weight .
  
  BIND(?occurrence * ?weight AS ?points)



  BIND(?perc_per_part / ?quantity AS ?perc_per_item)

  {
    SELECT ?asset_part (SUM(?quantity) AS ?total_items)
    WHERE {
      ?asset a crm:E24_Physical_Human-Made_Thing ;
             crm:P46_is_composed_of ?asset_part .
      ?value_assessment hero:assignsValueTo ?asset_part ;
                       hero:ratesItemQuantity ?quantity .
    }
    GROUP BY ?asset_part
  }
  {

  }
}
```

***

## CQ_3.2
Return the assets which have been assigned "Artistic" contributing values and risks which exist at the "building" layer of enclosure.

```SPARQL
PREFIX : <http://purl.org/sirius/ontology/03/data/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX hero: <http://purl.org/sirius/ontology/hero/>

SELECT DISTINCT ?asset_part ?perc_value
WHERE {
    ?asset a crm:E24_Physical_Human-Made_Thing ;
            crm:P46_is_composed_of ?asset_part .
    ?value_assessment hero:assignsValueTo ?asset_part ;
                        hero:assignsValue ?value ;

                        

    ?value hero:withValueType hero:artistic .
    ?risk_assessment hero:assignsRiskTo ?asset ;
                        hero:assignsRisk ?risk .
    ?risk hero:existsWithin hero:building .
}
```

***

## CQ_3.3
Return all the contributing values assigned to the assets that constitute the asset "Battistero degli Ariani". For each value, return its type, definition, weight, note, and degree of occurrence.

```SPARQL
PREFIX : <http://purl.org/sirius/ontology/03/data/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX hero: <http://purl.org/sirius/ontology/hero/>

SELECT ?asset ?value_type ?definition ?note ?weight ?occurrence
WHERE {
    :battistero-degli-ariani crm:P46_is_composed_of ?asset .
    ?value_assessment hero:assignsValueTo ?asset ;
                        hero:ratesOccurrenceDegree ?occurrence .
                        hero:assignsValue ?value .
    ?value hero:withValueType ?value_type ;
            hero:hasRelativeWeight ?weight ;
            hero:hasDefinition ?definition ;
    OPTIONAL {
        ?value tbox:hasNote ?note ;
    }
}
```

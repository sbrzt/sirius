# Formal Competency Questions
## CQ_1.1
Return the information about the heritage asset, including its name, alternative name, its description, the place it is located in (as well as its coordinates), and the time-span temporal horizon that identifies the creation event it has been dated to.

```SPARQL
PREFIX tbox: <http://purl.org/sirius/ontology/development/01/schema/>
PREFIX abox: <http://purl.org/sirius/ontology/development/01/data/>

SELECT ?asset_name ?alt_name ?description ?place_name ?coordinates ?date
WHERE {
    ?heritage_asset a tbox:HeritageAsset ;
                    tbox:hasAssetName ?asset_name ;
                    tbox:hasAlternativeName ?alt_name ;
                    tbox:hasAssetDescription ?description ;
                    tbox:isLocatedIn ?place .
    ?place a tbox:Place ;
            tbox:hasPlaceName ?place_name ;
            tbox:hasCoordinates ?coordinates .
    ?creation_event a tbox:CreationEvent ;
                    tbox:creates ?heritage_asset ;
                    tbox:hasTimeSpan ?time_span .
    ?time_span a tbox:TimeSpan ;
                tbox:fallsWithin ?date .
}
```

***

## CQ_1.2
Return the contextual information of the heritage asset in terms of its type and description.

```SPARQL
PREFIX tbox: <http://purl.org/sirius/ontology/development/01/schema/>
PREFIX abox: <http://purl.org/sirius/ontology/development/01/data/>

SELECT ?heritage_asset ?context_type ?context_description
WHERE {
    ?heritage_asset a tbox:HeritageAsset ;
                    tbox:hasContext ?context .
    ?context a tbox:Context ;
                tbox:hasType ?context_type ;
                tbox:hasContextDescription ?context_description .
}
```

***

## CQ_1.3
Return the documents that document the contextual information of the heritage asset.

```SPARQL
PREFIX tbox: <http://purl.org/sirius/ontology/development/01/schema/>
PREFIX abox: <http://purl.org/sirius/ontology/development/01/data/>

SELECT ?heritage_asset ?context_type ?document ?document_link
WHERE {
    ?heritage_asset a tbox:HeritageAsset ;
                    tbox:hasContext ?context .
    ?context a tbox:Context ;
                tbox:hasType ?context_type .
    ?document a tbox:Document ;
                tbox:documents ?context ;
                tbox:hasLink ?document_link .
}
```

***

## CQ_1.4
Return the names of the stakeholders involved in the risk assessment activity regarding the heritage asset.

```SPARQL
PREFIX tbox: <http://purl.org/sirius/ontology/development/01/schema/>
PREFIX abox: <http://purl.org/sirius/ontology/development/01/data/>

SELECT ?heritage_asset ?stakeholder_name
WHERE {
    ?heritage_asset a tbox:HeritageAsset .
    ?risk_assessment_activity a tbox:RiskAssessmentActivity ;
                                tbox:assignsRiskTo ?heritage_asset ;
                                tbox:involves ?stakeholder .
    ?stakeholder a tbox:Stakeholder ;
                tbox:hasStakeholderName ?stakeholder_name .
}
```
# Formal Competency Questions
## CQ_1.1
What information should be returned about the heritage asset, including its name, alternative name, description, location (along with coordinates), and the temporal horizon specifying the creation event date?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/01/schema/>
PREFIX abox: <https://w3id.org/sirius/ontology/development/01/data/>

SELECT ?asset_name ?alt_name ?description ?place_name ?coordinates ?date
WHERE {
    ?heritage_asset a tbox:HeritageAsset ;
                    tbox:hasName ?asset_name ;
                    tbox:hasAlternativeName ?alt_name ;
                    tbox:hasDescription ?description ;
                    tbox:isLocatedIn ?place .
    ?place a tbox:Place ;
            tbox:hasName ?place_name ;
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
What is the contextual information of the heritage asset in terms of its type and description?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/01/schema/>
PREFIX abox: <https://w3id.org/sirius/ontology/development/01/data/>

SELECT ?heritage_asset ?context_type ?context_description
WHERE {
    ?heritage_asset a tbox:HeritageAsset .
    ?riskAssessment a tbox:ContextDescription ;
                    tbox:describes ?heritage_asset ;
                    tbox:hasObservation ?context .
    ?context a tbox:Observation ;
                tbox:hasParameter  ?context_type ;
                tbox:hasDescription ?context_description .
}
```

***

## CQ_1.3
Which documents provide information about the contextual details of the heritage asset?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/01/schema/>
PREFIX abox: <https://w3id.org/sirius/ontology/development/01/data/>

SELECT ?heritage_asset ?context_type ?document ?document_link
WHERE {
    ?heritage_asset a tbox:HeritageAsset .
    ?riskAssessment a tbox:ContextDescription ;
                    tbox:describes ?heritage_asset ;
                    tbox:hasObservation ?context .
    ?context a tbox:Observation ;
                tbox:hasParameter  ?context_type .
    ?document a tbox:Document ;
                tbox:documents ?context ;
                tbox:hasLink ?document_link .
}
```

***

## CQ_1.4
Who are the stakeholders involved in the risk assessment activity related to the heritage asset, and what are their names?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/01/schema/>
PREFIX abox: <https://w3id.org/sirius/ontology/development/01/data/>

SELECT ?heritage_asset ?stakeholder_name
WHERE {
    ?heritage_asset a tbox:HeritageAsset .
    ?risk_assessment_activity a tbox:ContextDescription ;
                                tbox:describes ?heritage_asset ;
                                tbox:hasParticipant ?stakeholder .
    ?stakeholder a tbox:Stakeholder ;
                tbox:hasName ?stakeholder_name .
}
```
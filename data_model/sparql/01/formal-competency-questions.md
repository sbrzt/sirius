# Formal Competency Questions
## CQ_1.1
What information should be returned about the heritage asset, including its name, alternative name, description, location (along with coordinates), and the temporal horizon specifying the creation event date?

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?asset_name ?alt_name ?description ?place_name ?coordinates ?date
WHERE {
    ?heritage_asset a crm:E24_Physical_Human-Made_Thing ;
                    dcterms:title ?asset_name ;
                    dcterms:alternative ?alt_name ;
                    hero:hasNote ?description ;
                    crm:P55_has_current_location ?place .
    ?place a crm:E53_Place ;
            rdfs:label ?place_name ;
            crm:P168_place_is_defined_by ?coordinates .
    ?creation_event a crm:E12_Production ;
                    crm:P108_has_produced ?heritage_asset ;
                    crm:P4_has_time-span ?time_span .
    ?time_span a crm:E52_Time-Span ;
                crm:P82_at_some_time_within ?date .
}
```

***

## CQ_1.2
What is the contextual information of the heritage asset in terms of its type and description?

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>

SELECT ?heritage_asset ?context_type ?context_description
WHERE {
    ?heritage_asset a crm:E24_Physical_Human-Made_Thing .
    ?riskAssessment a hero:ContextDescription ;
                    hero:describes ?heritage_asset ;
                    hero:hasObservation ?context .
    ?context a hero:Observation ;
                hero:hasParameter ?context_type ;
                hero:hasNote ?context_description .
}
```

***

## CQ_1.3
Which documents provide information about the contextual details of the heritage asset?

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?heritage_asset ?context_type ?document ?document_link
WHERE {
    ?heritage_asset a crm:E24_Physical_Human-Made_Thing .
    ?riskAssessment a hero:ContextDescription ;
                    hero:describes ?heritage_asset ;
                    hero:hasObservation ?context .
    ?context a hero:Observation ;
                hero:hasParameter ?context_type .
    ?document a foaf:Document ;
                hero:documents ?context ;
                rdfs:seeAlso ?document_link .
}
```

***

## CQ_1.4
Who are the stakeholders involved in the risk assessment activity related to the heritage asset, and what are their names?

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?heritage_asset ?stakeholder_name
WHERE {
    ?heritage_asset a crm:E24_Physical_Human-Made_Thing .
    ?risk_assessment_activity a hero:ContextDescription ;
                                hero:describes ?heritage_asset ;
                                hero:hasParticipant ?stakeholder .
    ?stakeholder a foaf:Agent ;
                foaf:name ?stakeholder_name .
}
```
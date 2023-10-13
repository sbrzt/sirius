# Formal Competency Questions
## CQ_1.1
Return the information about the heritage asset, including its name, alternative name, its description, the place it is located in (as well as its coordinates), and the time-span temporal horizon that identifies the creation event it has been dated to.

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?asset_name ?alt_name ?description ?place_name ?coordinates ?date
WHERE {
    ?heritage_asset a crm:E24_Physical_Human-Made_Thing ;
                    dcterms:title ?asset_name ;
                    dcterms:alternative ?alt_name ;
                    crm:P3_has_note ?description ;
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
Return the contextual information of the heritage asset in terms of its type and description.

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX hero: <http://purl.org/sirius/ontology/hero/>

SELECT ?heritage_asset ?context_type ?context_description
WHERE {
    ?heritage_asset a crm:E24_Physical_Human-Made_Thing .
    ?riskAssessment a hero:RiskAssessment ;
                    hero:assignsRiskTo ?heritage_asset ;
                    hero:isInformedBy ?context .
    ?context a hero:Observation ;
                hero:observes ?context_type ;
                hero:hasContent ?context_description .
}
```

***

## CQ_1.3
Return the documents that document the contextual information of the heritage asset.

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX hero: <http://purl.org/sirius/ontology/hero/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?heritage_asset ?context_type ?document ?document_link
WHERE {
    ?heritage_asset a crm:E24_Physical_Human-Made_Thing .
    ?riskAssessment a hero:RiskAssessment ;
                    hero:assignsRiskTo ?heritage_asset ;
                    hero:isInformedBy ?context .
    ?context a hero:Observation ;
                hero:observes ?context_type .
    ?document a crm:E31_Document ;
                crm:P70_documents ?context ;
                rdfs:seeAlso ?document_link .
}
```

***

## CQ_1.4
Return the names of the stakeholders involved in the risk assessment activity regarding the heritage asset.

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX hero: <http://purl.org/sirius/ontology/hero/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?heritage_asset ?stakeholder_name
WHERE {
    ?heritage_asset a crm:E24_Physical_Human-Made_Thing .
    ?risk_assessment_activity a hero:RiskAssessment ;
                                hero:assignsRiskTo ?heritage_asset ;
                                hero:relatesTo ?stakeholder .
    ?stakeholder a foaf:Agent ;
                foaf:name ?stakeholder_name .
}
```
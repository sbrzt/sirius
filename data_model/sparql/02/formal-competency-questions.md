# Formal Competency Questions
## CQ_2.1
Return the risk summaries and the agents of deterioration of the risks assigned to the "Battistero degli Ariani".

```SPARQL
PREFIX : <http://purl.org/sirius/ontology/data/02/>
PREFIX hero: <http://purl.org/sirius/ontology/hero/>

SELECT ?risk ?risk_summary ?agent_of_deterioration
WHERE {
    ?risk_assessment a hero:Identification ;
                    hero:identifiesRiskFor :baptistery ;
                    hero:identifies ?risk .
    ?risk a hero:Risk ;
        hero:hasNote ?risk_summary ;
        hero:isClassifiedBy ?agent_of_deterioration .
}
```

***

## CQ_2.2
Return the hazards originating the risk that are related to the agent of deterioration "Physical forces".

```SPARQL
PREFIX hero: <http://purl.org/sirius/ontology/hero/>

SELECT ?risk ?hazard_type
WHERE {
    ?risk a hero:Risk ;
            hero:resultsFrom ?hazard ;
            hero:isClassifiedBy hero:physical-forces .
    ?hazard a hero:Hazard ;
            hero:hasType ?hazard_type .
}
```

***

## CQ_2.3
Return the adverse effects of the risk that is related to the agents of deterioration "Pests", "Water" and "Fire".

```SPARQL
PREFIX hero: <http://purl.org/sirius/ontology/hero/>

SELECT ?risk ?agent_of_deterioration ?adverse_effect_type
WHERE {
    ?risk a hero:Risk ;
            hero:entails ?adverse_effect ;
            hero:isClassifiedBy ?agent_of_deterioration .
    ?adverse_effect a hero:AdverseEffect ;
                    hero:hasType ?adverse_effect_type .
    FILTER (
    ?agent_of_deterioration = hero:pests || 
    ?agent_of_deterioration = hero:water || 
    ?agent_of_deterioration = hero:fire
    )
}
```
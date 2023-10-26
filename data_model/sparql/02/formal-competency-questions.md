# Formal Competency Questions
## CQ_2.1
Return the risk summaries and the agents of deterioration of the risks assigned to the "Battistero degli Ariani".

```SPARQL
PREFIX : <http://purl.org/sirius/ontology/02/data/>
PREFIX hero: <http://purl.org/sirius/ontology/hero/>

SELECT ?risk ?risk_summary ?agent_of_deterioration
WHERE {
    ?risk_assessment a hero:RiskAssessment ;
                    hero:assignsRiskTo :battistero-degli-ariani ;
                    hero:assigns ?risk .
    ?risk a hero:Risk ;
        hero:hasDescription ?risk_summary ;
        hero:isDeterminedBy ?agent_of_deterioration .
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
            hero:isDeterminedBy hero:physical-forces .
    ?hazard a hero:Hazard ;
            hero:hasHazardType ?hazard_type .
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
            hero:isDeterminedBy ?agent_of_deterioration .
    ?adverse_effect a hero:AdverseEffect ;
                    hero:hasAdverseEffectType ?adverse_effect_type .
    FILTER (
    ?agent_of_deterioration = hero:pests || 
    ?agent_of_deterioration = hero:water || 
    ?agent_of_deterioration = hero:fire
    )
}
```
# Formal Competency Questions
## CQ_2.1
Return the risk summaries and the agents of deterioration of the risks assigned to the "Battistero degli Ariani".

```SPARQL
PREFIX tbox: <http://purl.org/sirius/ontology/development/02/schema/>
PREFIX abox: <http://purl.org/sirius/ontology/development/02/data/>

SELECT ?risk ?risk_summary ?agent_of_deterioration
WHERE {
    ?risk_assessment a tbox:RiskAssessment ;
                    tbox:assignsRiskTo abox:baptistery ;
                    tbox:assigns ?risk .
    ?risk a tbox:Risk ;
        tbox:hasSummary ?risk_summary ;
        tbox:isEmbodiedBy ?agent_of_deterioration .
}
```

***

## CQ_2.2
Return the hazards originating the risk that are related to the agent of deterioration "Physical forces".

```SPARQL
PREFIX tbox: <http://purl.org/sirius/ontology/development/02/schema/>
PREFIX abox: <http://purl.org/sirius/ontology/development/02/data/>

SELECT ?risk ?hazard
WHERE {
    ?risk a tbox:Risk ;
            tbox:originatesFrom ?hazard ;
            tbox:isEmbodiedBy tbox:physical-forces .
}
```

***

## CQ_2.3
Return the adverse effects of the risk that is related to the agents of deterioration "Pests", "Water" and "Fire".

```SPARQL
PREFIX tbox: <http://purl.org/sirius/ontology/development/02/schema/>
PREFIX abox: <http://purl.org/sirius/ontology/development/02/data/>

SELECT ?risk ?agent_of_deterioration ?adverse_effect
WHERE {
    ?risk a tbox:Risk ;
            tbox:causes ?adverse_effect ;
            tbox:isEmbodiedBy ?agent_of_deterioration .
    FILTER (
    ?agent_of_deterioration = tbox:pests || 
    ?agent_of_deterioration = tbox:water || 
    ?agent_of_deterioration = tbox:fire
    )
}
```

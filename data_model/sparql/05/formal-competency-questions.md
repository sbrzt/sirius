# Formal Competency Questions
## CQ_5.1
Return the risks with catastrophic (15-13.5), extreme (13-11.5) or high (11-9.5) priority.

```SPARQL
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>

SELECT DISTINCT ?risk ?priority
WHERE {
  ?evaluation hero:evaluates ?risk ;
              hero:hasPriorityLevel ?priority .
  FILTER ( 
      ?priority = hero:catastrophic || 
      ?priority = hero:extreme ||
      ?priority = hero:high
  )
}
```

***

## CQ_5.2
Return the risks, their priorities, the criterions (and their values) used to set the priorities, the conditions values on which the criterions have been set, and their acceptance levels.

```SPARQL
PREFIX ccs: <https://w3id.org/sirius/ontology/ccs/>
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>
PREFIX tm: <https://w3id.org/sirius/ontology/tm/>

SELECT DISTINCT ?risk ?priority ?criterion ?criterion_value ?condition_value ?acceptance
WHERE {
    ?evaluation hero:evaluates ?risk ;
              hero:hasPriorityLevel ?priority ;
              hero:hasAcceptanceLevel ?acceptance ;
              ccs:isDeterminedBy ?criterion_setter .
    ?criterion_setter ccs:setsCriterion ?criterion ;
                      ccs:withCondition ?condition .
    ?criterion ?value_property ?criterion_value .
    ?condition ccs:hasQuantitativeConditionValue ?condition_value .
    FILTER (
      ?value_property = hero:hasProbableEstimate ||
      ?value_property = hero:hasDegreeOfConfidence
    )
}
```

***

## CQ_5.3
Return the values of the magnitudes and the uncertainties used as criterions, the values of their conditions, the priorities assigned to their respective risks, and their acceptance levels.

```SPARQL
PREFIX ccs: <https://w3id.org/sirius/ontology/ccs/>
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>
PREFIX tm: <https://w3id.org/sirius/ontology/tm/>

SELECT DISTINCT ?risk ?magnitude_value ?magnitude_condition_value ?uncertainty_value ?uncertainty_condition_value ?priority ?acceptance
WHERE {
    ?evaluation hero:evaluates ?risk ;
              hero:hasPriorityLevel ?priority ;
              hero:hasAcceptanceLevel ?acceptance ;
              ccs:isDeterminedBy ?magnitude_setter , ?uncertainty_setter .
    ?magnitude_setter ccs:setsCriterion ?magnitude ;
                      ccs:withCondition ?magnitude_condition .
    ?magnitude a hero:Magnitude ;
               hero:hasProbableEstimate ?magnitude_value .
    ?magnitude_condition ccs:hasQuantitativeConditionValue ?magnitude_condition_value .
    ?uncertainty_setter ccs:setsCriterion ?uncertainty ;
                      ccs:withCondition ?uncertainty_condition .
    ?uncertainty a hero:Uncertainty ;
                 hero:hasDegreeOfConfidence ?uncertainty_value .
    ?uncertainty_condition ccs:hasQuantitativeConditionValue ?uncertainty_condition_value .
}
```
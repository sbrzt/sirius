# Formal Competency Questions
## CQ_5.1
Return the risks with catastrophic (15-13.5), extreme (13-11.5) or high (11-9.5) priority.

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/05/schema/>
PREFIX abox: <https://w3id.org/sirius/ontology/development/05/data/>

SELECT DISTINCT ?risk ?priority
WHERE {
  ?evaluation tbox:evaluates ?risk ;
              tbox:hasPriorityLevel ?priority .
  FILTER ( 
      ?priority = tbox:catastrophic || 
      ?priority = tbox:extreme ||
      ?priority = tbox:high
  )
}
```

***

## CQ_5.2
Return the risks, their priorities, the criterions (and their values) used to set the priorities, the conditions values on which the criterions have been set, and their acceptance levels.

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/05/schema/>
PREFIX abox: <https://w3id.org/sirius/ontology/development/05/data/>

SELECT DISTINCT ?risk ?priority ?criterion ?criterion_value ?condition_value ?acceptance
WHERE {
    ?evaluation tbox:evaluates ?risk ;
              tbox:hasPriorityLevel ?priority ;
              tbox:hasAcceptanceLevel ?acceptance ;
              tbox:hasCriterion ?criterion_setter .
    ?criterion_setter tbox:setsCriterion ?criterion ;
                      tbox:withCondition ?condition .
    ?criterion ?value_property ?criterion_value .
    ?condition tbox:hasQuantitativeConditionValue ?condition_value .
    FILTER (
      ?value_property = tbox:hasProbableEstimate ||
      ?value_property = tbox:hasDegreeOfConfidence
    )
}
```

***

## CQ_5.3
Return the values of the magnitudes and the uncertainties used as criterions, the values of their conditions, the priorities assigned to their respective risks, and their acceptance levels.

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/05/schema/>
PREFIX abox: <https://w3id.org/sirius/ontology/development/05/data/>

SELECT DISTINCT ?risk ?magnitude_value ?magnitude_condition_value ?uncertainty_value ?uncertainty_condition_value ?priority ?acceptance
WHERE {
    ?evaluation tbox:evaluates ?risk ;
              tbox:hasPriorityLevel ?priority ;
              tbox:hasAcceptanceLevel ?acceptance ;
              tbox:hasCriterion ?magnitude_setter , ?uncertainty_setter .
    ?magnitude_setter tbox:setsCriterion ?magnitude ;
                      tbox:withCondition ?magnitude_condition .
    ?magnitude a tbox:Magnitude ;
               tbox:hasProbableEstimate ?magnitude_value .
    ?magnitude_condition tbox:hasQuantitativeConditionValue ?magnitude_condition_value .
    ?uncertainty_setter tbox:setsCriterion ?uncertainty ;
                      tbox:withCondition ?uncertainty_condition .
    ?uncertainty a tbox:Uncertainty ;
                 tbox:hasDegreeOfConfidence ?uncertainty_value .
    ?uncertainty_condition tbox:hasQuantitativeConditionValue ?uncertainty_condition_value .
}
```
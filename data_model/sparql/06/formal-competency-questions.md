# Formal Competency Questions
## CQ_6.1
What are the treatment options developed for each risk? For each option, what are its layer of enclosure, stage of control, capital cost, annual cost, and notes?

```SPARQL
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>

SELECT DISTINCT ?option ?note ?layer ?stage ?capital_cost ?annual_cost
WHERE {
  ?treatment hero:develops ?option .
  ?option hero:hasNote ?note ;
          hero:isClassifiedByLayer ?layer ;
          hero:isClassifiedByControlStage ?stage ;
          hero:hasCapitalCost ?capital_cost ;
          hero:hasMaintenanceCost ?annual_cost .
}
```

***

## CQ_6.2
Which are the treatment options existing in the "fitting" layer and at the BLOCK stage of control?

```SPARQL
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>

SELECT DISTINCT ?option
WHERE {
    ?treatment hero:develops ?option .
    ?option hero:isClassifiedByLayer hero:fitting ;
            hero:isClassifiedByControlStage hero:block .
}
```

***

## CQ_6.3
Which are the treatment options with a capital cost higher than 1000 and an annual cost lower than 100?

```SPARQL
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>

SELECT ?option ?capital_cost ?annual_cost
WHERE {
    ?treatment hero:develops ?option .
    ?option hero:hasCapitalCost ?capital_cost ;
            hero:hasMaintenanceCost ?annual_cost .
    FILTER(
      ?capital_cost > 1000 &&
      ?annual_cost < 100
    )
}
```

***

## CQ_6.4
Which are the treatment options existing in the "building" or "room" layer and at the AVOID or DETECT stage of control, with a capital cost higher than 50 and an annual cost lower than 50?

```SPARQL
PREFIX hero: <https://w3id.org/sirius/ontology/hero/>

SELECT ?option ?note ?layer ?stage ?capital_cost ?annual_cost
WHERE {
    ?treatment hero:develops ?option .
    ?option hero:hasNote ?note ;
            hero:isClassifiedByLayer ?layer ;
            hero:isClassifiedByControlStage ?stage ;
            hero:hasCapitalCost ?capital_cost ;
            hero:hasMaintenanceCost ?annual_cost .
    FILTER(
      (
        ?layer = hero:building ||
        ?layer = hero:room
      ) &&
      (
        ?stage = hero:avoid ||
        ?stage = hero:detect
      ) &&
      (
        ?capital_cost > 50 &&
        ?annual_cost < 50
      )
    )
}
```
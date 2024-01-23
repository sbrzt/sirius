# Formal Competency Questions
## CQ_6.1
What are the treatment options developed for each risk? For each option, what are its layer of enclosure, stage of control, capital cost, annual cost, and notes?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/06/schema/>
PREFIX abox: <https://w3id.org/sirius/ontology/development/06/data/>

SELECT DISTINCT ?option ?note ?layer ?stage ?capital_cost ?annual_cost
WHERE {
  ?treatment tbox:develops ?option .
  ?option tbox:hasNote ?note ;
          tbox:isClassifiedByLayer ?layer ;
          tbox:isClassifiedByControlStage ?stage ;
          tbox:hasCapitalCost ?capital_cost ;
          tbox:hasAnnualCost ?annual_cost .
}
```

***

## CQ_6.2
Which are the treatment options existing in the "fitting" layer and at the BLOCK stage of control?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/06/schema/>
PREFIX abox: <https://w3id.org/sirius/ontology/development/06/data/>

SELECT DISTINCT ?option
WHERE {
    ?treatment tbox:develops ?option .
    ?option tbox:isClassifiedByLayer tbox:fitting ;
            tbox:isClassifiedByControlStage tbox:block .
}
```

***

## CQ_6.3
Which are the treatment options with a capital cost higher than 1000 and an annual cost lower than 100?

```SPARQL
PREFIX tbox: <https://w3id.org/sirius/ontology/development/06/schema/>
PREFIX abox: <https://w3id.org/sirius/ontology/development/06/data/>

SELECT ?option ?capital_cost ?annual_cost
WHERE {
    ?treatment tbox:develops ?option .
    ?option tbox:hasCapitalCost ?capital_cost ;
            tbox:hasAnnualCost ?annual_cost .
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
SELECT ?option ?note ?layer ?stage ?capital_cost ?annual_cost
WHERE {
    ?treatment tbox:develops ?option .
    ?option tbox:hasNote ?note ;
            tbox:isClassifiedByLayer ?layer ;
            tbox:isClassifiedByControlStage ?stage ;
            tbox:hasCapitalCost ?capital_cost ;
            tbox:hasAnnualCost ?annual_cost .
    FILTER(
      (
        ?layer = tbox:building ||
        ?layer = tbox:room
      ) &&
      (
        ?stage = tbox:avoid ||
        ?stage = tbox:detect
      ) &&
      (
        ?capital_cost > 50 &&
        ?annual_cost < 50
      )
    )
}
```
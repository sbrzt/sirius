# Informal Competency Questions
## Question 1

### Identifier
CQ_2.1

### Question
Return the risk summaries and the agents of deterioration of the risks assigned to the "Battistero degli Ariani".

### Expected outcome
List of: `risk`, `risk_summary`, `agent_of_deterioration`

### Results
* "Fragmentation of data", "Fragmentation of data related to previous incorrect monitoring and maintenance interventions provokes loss of important information related to the baptistery", `dissociation`
* "Walls erosion", "Floods and heavy rains induce erosion of the baptistery walls", `water`
* "Anthropic activity", "Various motivations cause the presence of graffiti and abandonment of objects in the area surrounding the baptistery", `theft-and-vandalism`

### Based on
Example 1

***

## Question 2

### Identifier
CQ_2.2

### Question
Return the hazards originating the risk that are related to the agent of deterioration "Physical forces".

### Expected outcome
List of: `risk`, `hazard`

### Results
* "Physical destruction", `traffic-induced-vibration`
* "Physical destruction", `civil-works`
* "Physical destruction", `earthquake`
* "Physical destruction", `subsidence`

### Based on
Example 1

***

## Question 3

### Identifier
CQ_2.3

### Question
Return the adverse effects of the risk that is related to the agents of deterioration "Pests", "Water" and "Fire".

### Expected outcome
List of: `risk`, `agent_of_deterioration`, `adverse_effect`

### Results
* "Animal and plant colonization", `pests`, `excrements`
* "Animal and plant colonization", `pests`, `overgrowth`
* "Walls erosion", `water`, `corrosion`
* "Fires due to equipment malfunction", `fire`, `non-assessable`

### Based on
Example 1

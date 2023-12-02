# Informal Competency Questions
## Question 1

### Identifier
CQ_2.1

### Question
Return the textual descriptions assigned to the risks, the agents of deterioration that classify them, and their types.

### Expected outcome
List of: `risk`, `agent_of_deterioration`, `risk_type`, `risk_summary`

### Results
* `risk-01`, `"physical-forces`, `cumulative`, "";
* `risk-02`, `dissociation`, `rare`, "Fragmentation of data related to previous incorrect monitoring and maintenance interventions provokes loss of important information related to the baptistery";
* `risk-03`, `pests`, `common`, "";
* `risk-04`, `water`, `rare`, "Floods and heavy rains induce erosion of the baptistery walls".

### Based on
Example 1

***

## Question 2

### Identifier
CQ_2.2

### Question
Return the risks identified within the layers `site` or `region`, their types, the documents documenting them, and the start and end dates of the time intervals they have been identified in.

### Expected outcome
List of: `risk`, `risk_type`, `document`, `start_date`, `end_date`

### Results
* `risk-02`, `rare`, `document-b`, "2020-10-10T00:00:00Z", "2020-10-10T23:59:59Z";
* `risk-03`, `common`, `document-a`, "2020-10-11T00:00:00Z", "2020-10-11T23:59:59Z"
* `risk-04`, `rare`, `document-b`, "2020-10-10T00:00:00Z", "2020-10-10T23:59:59Z".

### Based on
Example 1

# Informal Competency Questions
## Question 1

### Identifier
CQ_7.1

### Question
What are the steps that are part of the workflow for the risk assessment of the museum? What is their duration? What are the activities they were executed in?

### Expected outcome
List of: `step`, `duration`, `activity`

### Results
* `context-step`, 10, `context-description-activity`
* `identify-step`, 30, `identification-activity`
* `analyze-step`, 5, `analysis-activity`
* `evaluate-step`, 30, `evaluation-activity`
* `treat-step`, 20, `treatment-activity`

### Based on
Example 1

***

## Question 2

### Identifier
CQ_7.2

### Question
What are the activities involved in the event executing the workflow? What are the time interval in which they respectively are executed?

### Expected outcome
List of: `activity`, `start_date`, `end_date`

### Results
* `context-description-activity`, "2023-01-10", "2023-01-20"
* `identification-activity`, "2023-01-20", "2023-02-20"
* `analysis-activity`, "2023-02-20", "2023-02-25"
* `evaluation-activity`, "2023-02-25", "2023-03-25"
* `treatment-activity`, "2023-03-25", "2023-04-15"

### Based on
Example 1

***

## Question 3

### Identifier
CQ_7.3

### Question
What does each assessment activity target? What does it assess?

### Expected outcome
List of: `activity`, `heritage_asset`, `element`

### Results
* `context-description-activity`, `museum`, `value-01`
* `identification-activity`, `museum`, `risk-01`
* `analysis-activity`, `museum`, `risk-01`
* `evaluation-activity`, `museum`, `risk-01`
* `treatment-activity`, `museum`, `risk-01`

### Based on
Example 1

***

## Question 4

### Identifier
CQ_7.4

### Question
Who participated in each assessment activity? When? What did it target? What did it assess? What is it documented by?

### Expected outcome
List of: `activity`, `agent`, `start_date`, `end_date`, `heritage_asset`, `element`, `source`

### Results
* `context-description-activity`, `marta-cosentini`, "2023-01-10", "2023-01-20", `museum`, `value-01`, `museum-catalogue-record`
* `identification-activity`, `marta-cosentini`, "2023-01-20", "2023-02-20", `museum`, `risk-01`, `museum-historic-record`
* `analysis-activity`, `marta-cosentini`, "2023-02-20", "2023-02-25", `museum`, `risk-01`, None 
* `evaluation-activity`, `marta-cosentini`, "2023-02-25", "2023-03-25", `museum`, `risk-01`, None
* `treatment-activity`, `marta-cosentini`, "2023-03-25", "2023-04-15", `museum`, `risk-01`, None

### Based on
Example 1
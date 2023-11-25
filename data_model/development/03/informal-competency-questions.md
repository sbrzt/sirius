# Informal Competency Questions
## Question 1

### Identifier
CQ_3.1

### Question
Return all the risks with type "Cumulative process", the asset they are assiged to, the layers they exist within, and the documents that document them.

### Expected outcome
List of: `risk`, `asset`, `layer`, `document`

### Results
* `risk-1`, `baptistery`, `building`, `document-a`
* `risk-6`, `museum`, `room`, `document-c`

### Based on
Example 1, Example 2

***

## Question 2

### Identifier
CQ_3.2

### Question
Return all the risks existing with the layers "Region" or "Site", the asset they are assiged to, their type, and the start and end dates of the time intervals they exist in.

### Expected outcome
List of: `risk`, `asset`, `type`, `time_interval_start`, `time_interval_end`

### Results
* `risk-2`, `baptistery`, `rare-event`, "2020-10-10T00:00:00Z", "2020-10-10T23:59:59Z"
* `risk-3`, `baptistery`, `common-event`, "2020-10-11T00:00:00Z", "2020-10-11T23:59:59Z"
* `risk-7`, `museum`, `rare-event`, "2020-10-11T00:00:00Z", "2020-10-11T23:59:59Z"

### Based on
Example 1, Example 2

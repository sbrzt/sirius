# Informal Competency Questions
## Question 1
### Identifier
CQ 3.1

### Question
What are the probable estimates of the A-score, B-score, and C-score for each risk affecting each heritage asset, along with the documentation and textual content that record them?

### Expected outcome
List of: `risk`, `heritage_asset`, `risk_component`, `probable_estimate`, `note`, `knowledge_source`

### Result
* `museum-fire`, `museum`, `frequency`, 2.5, "National statistics from different countries show that the average time between large fire events for museums with basic fire control measures is about 300 years. The A-score in this case would be A=2½, indicating an expectation of a large fire once every 300 years.", `national-statistics`
* `museum-fire`, `museum`, `fractional-value-loss`, 5, "Considering the combustible nature of the museum building and its contents, a total or almost total loss of value is expected in each item affected by the fire."
* `museum-fire`, `museum`, `exposure`, 5, "Given the characteristics of the building and its contents, it is expected that all or most of the heritage asset and its value would be affected in the event of a large fire."
* `museum-theft`, `museum`, `frequency`, 3.5, "Staff memory indicates that the collection has suffered 3 theft events affecting objects on display in the past 75 years, estimating an average time of 25 years between theft events.", `staff-notes`
* `museum-theft`, `museum`, `fractional-value-loss`, 5, "A stolen item results in a complete loss of value for the museum and its public."
* `museum-theft`, `museum`, `exposure`, 2, "The most probable scenario is the opportunistic theft of a small, original object of the collection displayed without protection."
* `archive-deterioration`, `archive`, `frequency`, 3.5, "Deterioration by exposure to volatile substances released by cardboard boxes is a 'cumulative process' risk. For a period of 30 years, the A-score is A=3½."
* `archive-deterioration`, `archive`, `fractional-value-loss`, 2, "Observations on similar archival collections in the same kind of boxes show a tiny loss of value in each item affected over 30 years."
* `archive-deterioration`, `archive`, `exposure`, 2, "Only a tiny fraction of the heritage asset value is expected to be affected per event."

### Based on 
Example 01, Example 02, Example 03

***

## Question 2
### Identifier
CQ 3.2

### Question
What are the low, probable, and high estimates of the magnitudes of risk for each risk associated with each heritage asset?

### Expected outcome
List of: `risk`, `heritage_asset`, `low_estimate`, `probable_estimate`, `high_estimate`

### Result
* `museum-fire`, `museum`, 12, 12.5, 13
* `museum-theft`, `museum`, 10, 10.5, 11
* `archive-deterioration`, `archive`, 7, 7.5, 8

### Based on 
Example 01, Example 02, Example 03

***

## Question 3
### Identifier
CQ 3.3

### Question
What are the low, probable, and high estimates of the A-score, B-score, C-score, and magnitude of risk for each risk affecting each heritage asset?

### Expected outcome
List of: `risk`, `measure`, `low_estimate`, `probable_estimate`, `high_estimate`

### Result
* `museum-fire`, `frequency`, 2, 2.5, 3
* `museum-fire`, `fractional-value-loss`, 4.5, 5, 5
* `museum-fire`, `exposure`, 4.5, 5, 5
* `museum-fire`, `magnitude`, 12, 12.5, 13
* `museum-theft`, `frequency`, 3, 3.5, 4
* `museum-theft`, `fractional-value-loss`, 4.5, 5, 5
* `museum-theft`, `exposure`, 1.5, 2, 2.5
* `museum-theft`, `magnitude`, 10, 10.5, 11
* `archive-deterioration`, `frequency`, 3, 3.5, 4
* `archive-deterioration`, `fractional-value-loss`, 1.5, 2, 2.5
* `archive-deterioration`, `exposure`, 1.5, 2, 2.5
* `archive-deterioration`, `magnitude`, 7, 7.5, 8

### Based on 
Example 01, Example 02, Example 03
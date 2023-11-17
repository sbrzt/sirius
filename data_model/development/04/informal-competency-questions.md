# Informal Competency Questions
## Question 1
### Identifier
CQ 4.1

### Question
Return the probable estimate of the A-score, B-score, C-score for each risk affecting each heritage asset, as well as the sources of knowledge that witness them.

### Expected outcome
List of: `risk`, `heritage_asset`, `risk_component`, `probable_estimate`, `note`, `knowledge_source`

### Result
* `museum-fire`, `museum`, `frequency-or-rate`, 2.5, "National statistics from different countries show that the average time between large fire events for museums with basic fire control measures is about 300 years. The A-score in this case would be A=2½, indicating an expectation of a large fire once every 300 years.", `national-statistics`
* `museum-fire`, `museum`, `loss-of-value-per-item`, 5, "Considering the combustible nature of the museum building and its contents, a total or almost total loss of value is expected in each item affected by the fire."
* `museum-fire`, `museum`, `loss-of-value-per-asset`, 5, "Given the characteristics of the building and its contents, it is expected that all or most of the heritage asset and its value would be affected in the event of a large fire."
* `museum-theft`, `museum`, `frequency-or-rate`, 3.5, "Staff memory indicates that the collection has suffered 3 theft events affecting objects on display in the past 75 years, estimating an average time of 25 years between theft events.", `staff-notes`
* `museum-theft`, `museum`, `loss-of-value-per-item`, 5, "A stolen item results in a complete loss of value for the museum and its public."
* `museum-theft`, `museum`, `loss-of-value-per-asset`, 2, "The most probable scenario is the opportunistic theft of a small, original object of the collection displayed without protection."
* `archive-deterioration`, `archive`, `frequency-or-rate`, 3.5, "Deterioration by exposure to volatile substances released by cardboard boxes is a 'cumulative process' risk. For a period of 30 years, the A-score is A=3½."
* `archive-deterioration`, `archive`, `loss-of-value-per-item`, 2, "Observations on similar archival collections in the same kind of boxes show a tiny loss of value in each item affected over 30 years."
* `archive-deterioration`, `archive`, `loss-of-value-per-asset`, 2, "Only a tiny fraction of the heritage asset value is expected to be affected per event."

### Based on 
Example 01, Example 02, Example 03

***

## Question 2
### Identifier
CQ 4.2

### Question
Return the low, probable, and high estimates of the magnitudes of risk for each risk of each heritage asset.

### Expected outcome
List of: `risk`, `heritage_asset`, `low_estimate`, `probable_estimate`, `high_estimate`

### Result
* `museum-fire`, `museum`, 12, 12.5, 13
* `museum-theft`, `museum`, 10, 10.5, 11
* `archive-deterioration`, `archive`, 7, 7.5, 8

### Based on 
Example 01, Example 02, Example 03
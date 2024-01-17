# Informal Competency Questions
## Question 1

### Identifier
CQ_5.1

### Question
Return the risks with catastrophic (15-13.5), extreme (13-11.5) or high (11-9.5) priority.

### Expected outcome
List of: `risk`, `priority`

### Results
* `museum-fire`, `extreme`
* `museum-theft`, `high`

### Based on
Example 1

***

## Question 2

### Identifier
CQ_5.2

### Question
Return the risks, their priorities, the criterions (and their values) used to set the priorities, the conditions values on which the criterions have been set, and their acceptance levels.

### Expected outcome
List of: `risk`, `priority`, `criterion`, `criterion_value`, `condition_value`, `acceptance_level`

### Results
- `museum-fire`, `extreme`, `museum-fire-mr`, 12.5, 10.0, `treat-asap`
- `museum-fire`, `extreme`, `museum-fire-uncertainty`, 1.4, 2.0, `treat-asap`
- `museum-theft`, `high`, `museum-theft-mr`, 10.5, 10.0, `review-asap`
- `museum-theft`, `high`, `museum-theft-uncertainty`, 2.0, 2.0, `review-asap`
- `museum-deterioration`, `low`, `museum-deterioration-mr`, 7.5, 10.0, `no-action`
- `museum-deterioration`, `low`, `museum-deterioration-uncertainty`, 0.7, 2.0, `no-action`

### Based on
Example 1

***

## Question 3

### Identifier
CQ_5.3

### Question
Return the values of the magnitudes and the uncertainties used as criterions, the values of their conditions, the priorities assigned to their respective risks, and their acceptance levels.

### Expected outcome
List of: `risk`, `magnitude_value`, `magnitude_condition_value`, `uncertainty_value`, `uncertainty_condition_value`, `priority`, `acceptance_level`

### Results
- `museum-fire`, 12.5, 10.0, 1.4, 2.0, `extreme`, `treat-asap`
- `museum-theft`, 10.5, 10.0, 2.0, 2.0, `high`, `review-asap`
- `museum-deterioration`, 7.5, 10.0, 0.7, 2.0, `low`, `no-action`

### Based on
Example 1
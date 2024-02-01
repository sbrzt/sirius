# Informal Competency Questions
## Question 1

### Identifier
CQ_6.1

### Question
What are the treatment options developed for each risk? For each option, what are its layer of enclosure, stage of control, capital cost, annual cost, and notes?

### Expected outcome
List of: `option`, `note`, `layer`, `stage`, `capital_cost`, `annual_cost`

### Results
* `option-01`, "Attach the objects to their base (support, BLOCK), with a capital cost of 3000 and an annual cost of 0", `support`, `block`, 3000, 0
* `option-02`, "Display the objects inside showcases (fittings, BLOCK), with a capital cost of 2000 and an annual cost of 100", `fitting`, `block`, 2000, 100
* `option-03`, "Install security cameras in the display rooms (room, DETECT), with a capital cost of 6500 and an annual cost of 50", `room`, `detect`, 6500, 50
* `option-04`, "Forbid the entrance of visitors carrying bags, backpacks, suitcases inside the museum (building, AVOID), with a capital cost of 100 and an annual cost of 10", `building`, `avoid`, 100, 10

### Based on
Example 1

***

## Question 2

### Identifier
CQ_6.2

### Question
Which are the treatment options existing in the "fitting" layer and at the BLOCK stage of control?

### Expected outcome
List of: `option`

### Results
- `option-02`

### Based on
Example 1

***

## Question 3

### Identifier
CQ_6.3

### Question
Which are the treatment options with a capital cost higher than 1000 and an annual cost lower than 100?

### Expected outcome
List of: `option`, `note`, `capital_cost`, `annual_cost`

### Results
- `option-01`, "Attach the objects to their base (support, BLOCK), with a capital cost of 3000 and an annual cost of 0", 3000, 0
- `option-03`, "install security cameras in the display rooms (room, DETECT), with a capital cost of 6500 and an annual cost of 50", 6500, 50

### Based on
Example 1

***

## Question 4

### Identifier
CQ_6.4

### Question
Which are the treatment options existing in the "building" or "room" layer and at the AVOID or DETECT stage of control, with a capital cost higher than 50 and an annual cost lower than 50?

### Expected outcome
List of: `option`, `note`, `layer`, `stage`, `capital_cost`, `annual_cost`

### Results
- `option-04`, "Forbid the entrance of visitors carrying bags, backpacks, suitcases inside the museum (building, AVOID), with a capital cost of 100 and an annual cost of 10", `building`, `avoid`, 100, 10

### Based on
Example 1